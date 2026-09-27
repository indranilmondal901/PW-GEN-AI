import streamlit as st
'''
run - streamlit run streamlit.py
'''
# Page configuration
st.set_page_config(
    page_title="Python Crash Course",
    page_icon="🐍",
    layout="wide"
)

# Title, header, subheader and text
st.title("Python Applications Crash Course")
st.header("Streamlit Basics")
st.subheader("Build simple web applications with Python")

st.write("Streamlit lets us turn Python code into an interactive web application.")
st.markdown("### Markdown also works here.")
st.caption("This is a small caption.")


# code, json and metric
st.code("print('Mera dost Omkar!!')", language="python")
st.json({
    "Course": "Python",
    "level": "Beginner"
})
st.metric("Students", 25, "+5")

# Sidebar
st.sidebar.title("Course Menu")
st.sidebar.write("Choose an option below:")

topic = st.sidebar.selectbox(
    "Choose a topic",
    ["Python", "Pandas", "NumPy", "AI Applications"]
)

st.write(f"Selected topic: {topic}")


# Text input
name = st.text_input("What is your name?")

if name:
    st.write(f"Hello, {name}")

# Number input
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=18
)    

st.write(f"Your age is: {age}")


# slider
confidence = st.slider(
    "Choose a confidence score",
    min_value=0,
    max_value=100,
    value=50
)

st.write(f"Confidence score: {confidence}")

# Checkbox
show_details = st.checkbox("Show course details")

if show_details:
    st.info("This course prepares you to build Python applications for AI.")


# radio buttons
experience = st.radio(
    "Your Python experience",
    ["Beginner", "Intermediate", "Advanced"]
)

st.write(f"Selected experience: {experience}")


# selectedbox and multiselect

language = st.selectbox(
    "Choose a programming language:",
    ["Python", "JAVA", "JavaScript", "C++"]
)

skills = st.multiselect(
    "Choose your skills:",
    ["Python", "Pandas", "Numpy", "Streamlit", "Git"]
)

st.write(f"Language: {language}")
st.write(f"Skills: {skills}")


# Button
if st.button("Click Me"):
    st.success("Button clicked successfully!!")


# Form
with st.form("Student_form"):
    st.write("Student Registration")

    student_name = st.text_input("Student Name")
    student_email = st.text_input("Email")

    submitted = st.form_submit_button("Register")

    if submitted:
        st.success(f"Registration received for {student_name}")


# columns
col1, col2, col3 = st.columns(3)                

with col1:
    st.info("Python")

with col2:
    st.info("Pandas")

with col3:
    st.info("Numpy")        


# Expander
with st.expander("Show more info:"):
    st.write("Expanders are useful when we want to hide details until needed.")


# Status messages
st.success("Success message")    
st.info("Information based message")
st.warning("Warning message")
st.error("Error message")


# progress bar
st.progress(95)

# file uploader
uploaded_file = st.file_uploader(
    "Upload a text file",
    type=["txt"]
)

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area(f"Uploaded content", content, height=150)


# Download button
sample_text = "Hello from our PW GenAI batch."        

st.download_button(
    label = "Download sample text",
    data = sample_text,
    file_name = "sample.txt",
    mime = "text/plain"
)