"""
AI Resume Analyzer
==================

A small Streamlit app that compares a resume against a Job Description.

The whole workflow lives in this one file:

    Step 1  Read the uploaded resume (PDF or DOCX) as plain text
    Step 2  LLM call #1  ->  turn the resume + JD into structured JSON
    Step 3  LLM call #2  ->  turn that JSON into a readable report
    Step 4  Show the report and offer a Markdown download
"""

import json
import os

import streamlit as st
from docx import Document
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# Read the .env file so the API key stays out of the source code.
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# The five sections of the final report: (JSON key from LLM call #2, heading).
# One list is used both for showing the report and for building the download.
REPORT_SECTIONS = [
    ("strengths", "Strengths"),
    ("gaps", "Gaps"),
    ("missing_or_weak_skills", "Missing or Weak Skills"),
    ("improvement_suggestions", "Improvement Suggestions"),
    ("overall_summary", "Overall Summary"),
]


def extract_resume_text(uploaded_file):
    """Return the plain text of an uploaded PDF or DOCX resume."""
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        pages = []
        for page in reader.pages:
            # extract_text() gives None for pages that have no text layer,
            # for example a page that is really just a scanned image.
            pages.append(page.extract_text() or "")
        return "\n".join(pages).strip()

    if file_name.endswith(".docx"):
        document = Document(uploaded_file)
        paragraphs = []
        for paragraph in document.paragraphs:
            paragraphs.append(paragraph.text)
        return "\n".join(paragraphs).strip()

    return ""


def analyze_resume(resume_text, job_description):
    """LLM call #1: turn the resume and the JD into structured JSON."""
    client = OpenAI(api_key=API_KEY)

    instructions = """You compare resumes against job descriptions.

Reply with JSON only, using exactly these keys. Every value is a list of short strings.

{
  "candidate_skills": [],
  "candidate_experience": [],
  "candidate_qualifications": [],
  "required_skills": [],
  "preferred_skills": [],
  "matching_skills": [],
  "missing_skills": [],
  "gaps": []
}

Rules:
- Use only information that actually appears in the resume or the job description.
- Never invent skills, employers, job titles, dates, certifications or achievements.
- "missing_skills" means the job description asks for it and the resume does not mention it.
- Leave a list empty when the text gives you nothing to put in it.
"""

    # The word "JSON" has to appear in the input below, not only in the
    # instructions above, or the API rejects the json_object format.
    user_message = f"""Compare this resume against this job description and reply with JSON.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

    response = client.responses.create(
        model=MODEL,
        instructions=instructions,
        input=user_message,
        text={"format": {"type": "json_object"}},
    )

    # The model replies with JSON text, so turn it into a Python dictionary.
    return json.loads(response.output_text)


def generate_final_report(structured_analysis):
    """LLM call #2: turn the structured JSON into a readable report."""
    client = OpenAI(api_key=API_KEY)

    instructions = """You write short, honest resume feedback for a candidate.

You receive JSON that was built from a resume and a job description.
Reply with JSON only, using exactly these keys. Every value is a string.

{
  "strengths": "",
  "gaps": "",
  "missing_or_weak_skills": "",
  "improvement_suggestions": "",
  "overall_summary": ""
}

Rules:
- Write the first four values as Markdown bullet lists, one point per line ("- point").
- Write "overall_summary" as one short paragraph.
- Never leave a value empty. If a section has nothing to report, say so in one bullet,
  such as "- Nothing further was identified from the provided resume."
- Put specific tools and technologies in "missing_or_weak_skills", and put experience,
  qualifications and responsibilities in "gaps", so the two do not repeat each other.
- Base everything on the JSON you are given, and do not invent anything new.
- Never use the words "lacks", "lacking", "no experience", "no exposure",
  "does not know" or "does not have" anywhere, including the overall summary.
  You only know what this one resume mentions, not what the candidate can really do.
  Write "Apache Airflow was not identified in the provided resume" and
  "The resume does not show the 3+ years of analytics experience the role asks for".
- Do not give a numeric score or a percentage.
"""

    # The output of the first call becomes the input of the second call.
    # The word "JSON" has to appear here too, for the same reason as above.
    user_message = f"""Turn this structured data into resume feedback and reply with JSON.

{json.dumps(structured_analysis, indent=2)}
"""

    response = client.responses.create(
        model=MODEL,
        instructions=instructions,
        input=user_message,
        text={"format": {"type": "json_object"}},
    )

    report = json.loads(response.output_text)

    # The model is asked for strings, but it sometimes sends a list of points
    # instead. Tidy every section into a Markdown string here, so the rest of
    # the app can simply trust that all five sections are text.
    for key, _ in REPORT_SECTIONS:
        value = report.get(key)
        if isinstance(value, list):
            value = "\n".join("- " + str(point) for point in value)
        report[key] = value or "Nothing was reported for this section."

    return report


def create_downloadable_report(final_report):
    """Build the Markdown text for the resume_analysis.md download."""
    lines = ["# Resume Analysis"]
    for key, heading in REPORT_SECTIONS:
        lines.append("## " + heading)
        lines.append(final_report[key])
    return "\n\n".join(lines)


def main():
    st.set_page_config(page_title="AI Resume Analyzer")
    st.title("AI Resume Analyzer")
    st.write(
        "Upload your resume and paste a Job Description to identify strengths, "
        "gaps and improvement opportunities."
    )

    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])
    job_description = st.text_area("Paste the Job Description", height=250)

    if st.button("Analyze Resume"):
        # Check everything we need before spending money on an API call.
        # st.stop() ends this run of the script, so nothing below it happens.
        if uploaded_file is None:
            st.warning("Please upload your resume.")
            st.stop()

        if not job_description.strip():
            st.warning("Please paste the Job Description.")
            st.stop()

        # Step 1: Convert the uploaded resume into plain text
        resume_text = extract_resume_text(uploaded_file)

        if not resume_text:
            st.warning(
                "No text could be read from this file. This app works with "
                "text-based PDFs and DOCX files, not scanned or image-only PDFs."
            )
            st.stop()

        if not API_KEY:
            st.error(
                "No OpenAI API key found. Copy .env.example to .env and "
                "add your OPENAI_API_KEY."
            )
            st.stop()

        with st.spinner("Analyzing your resume..."):
            try:
                # Step 2: Ask the LLM to turn the resume and JD into structured information
                structured_analysis = analyze_resume(resume_text, job_description)

                # Step 3: Use that structured information to write a readable report
                final_report = generate_final_report(structured_analysis)
            except Exception as error:
                st.error(f"The analysis failed: {error}")
                st.stop()

        # Streamlit re-runs this file on every click, including the download
        # click, so keep the report here instead of losing it.
        st.session_state["final_report"] = final_report

    # Step 4: Display the results
    if "final_report" in st.session_state:
        final_report = st.session_state["final_report"]

        st.divider()
        st.subheader("Analysis Results")

        for key, heading in REPORT_SECTIONS:
            st.markdown("### " + heading)
            st.markdown(final_report[key])

        st.download_button(
            "Download Report",
            data=create_downloadable_report(final_report),
            file_name="resume_analysis.md",
        )


if __name__ == "__main__":
    main()
