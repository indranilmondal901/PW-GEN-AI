"""
1. Virtual env
2. installing packages
3. importing modules
4. create resusable module
5. Introducing multi threading

"""

# ============================================================================
# Virtual Environment
# ============================================================================

"""
-------------------------------------------------------------------------------
Why different env is needed ?

[BASE ENV]
-all packages here
numpy
langchain
panda
--> conflict in between packages

# venv
If I am doing 3 project I need to use 3 different env -
suppose 1 project need panda --- need env only with panda
suppose 2 project need panda and numpy --- need env only with panda and numpy
--> easy conflict resolve
---------------------------------------------------------------------------------

commands and usuages
pip list - 
pip install <module_name> -
"""
# -----------------------------------------------------------
# Making of a VENV
# -----------------------------------------------------------
# python -m venv myenv
# -----------------------------------------------------------
# For activat venv :
# -----------------------------------------------------------
# myenv\Scripts\activate
# -----------------------------------------------------------
# For deactivating :
# -----------------------------------------------------------
# deactivate

# ============================================================================
# Importing Modules
# ============================================================================
# import pandas; # ModuleNotFoundError: No module named 'pandas' --> panda present in base but not in myEnv(venv)

# ============================================================================
# Installing Modules
# ============================================================================
# pip install pandas
import pandas
# pip instal request==2.3.3
# In every project there is requirements.txt
# pip install -r <file_name> # here -> <file_name> = requirement.txt

# ============================================================================
# Creating Reusable module 
# ============================================================================
# script6.py
def add (a,b):
    return a+b;

def sub (a,b):
    return a-b;


# script.py 
'''
import script6;
result = script6.add(5,2);
print(result)

import script6 as cal;
result = cal.add(5,2);
print(result)

from script6 import sub;
result = sub(5,2);
print(result)
'''

# ============================================================================
# multi threading concept
# ============================================================================

import time

def task(name):
    print(f"{name} started..")
    time.sleep(3)
    print(f"{name} finished.")

# --------------------------------------------------------------

# start = time.time()

# task("Misc-Task1")
# task("Misc-Task2")
# task("Misc-Task3")
# task("Misc-Task4")
# task("Misc-Task5")

# end = time.time()

# print("Normal execution time:", end-start)

# -------------------------------------------------------------   

import threading    

thread1 = threading.Thread(
    target=task,
    args = ("Task1",) # it should be tuple
)

thread2 = threading.Thread(
    target=task,
    args = ("Task2",)
)

thread3 = threading.Thread(
    target=task,
    args = ("Task3",)
)

thread4 = threading.Thread(
    target=task,
    args = ("Task4",)
)

thread5 = threading.Thread(
    target=task,
    args = ("Task5",)
)

start = time.time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

end = time.time()

print("Normal execution time:", end-start)


import time;

def dealyListPrinter (list):
    for index,element in enumerate(list):
        print(f'element --> {element} position {index}');
        time.sleep(1);


list1 =["indra","ram","lucky"];
list2 =["a","b","c"];
list3 =[10,11,12];

start=time.time();

# dealyListPrinter(list1);
# dealyListPrinter(list2);
# dealyListPrinter(list3);

import threading;

thread1 = threading.Thread(
    target=dealyListPrinter,
    args= (list1,)
)


thread2 = threading.Thread(
    target=dealyListPrinter,
    args= (list2,)
)


thread3 = threading.Thread(
    target=dealyListPrinter,
    args= (list3,)
)

thread1.start();
thread2.start();
thread3.start();

thread1.join();
thread2.join();
thread3.join();

end = time.time()

print("Normal execution time:", end-start);



# ============================================================================
#                  PYTHON ENVIRONMENT, MODULES & THREADING
# ============================================================================

'''
===============================================================================
TOPICS
===============================================================================

1. Virtual Environment
2. Installing Packages
3. Importing Modules
4. Creating Reusable Modules
5. Introducing Multithreading


===============================================================================
IMPORTANT TERMINOLOGY
===============================================================================

MODULE
-------
A Python file (.py) containing Python code.

Example:

calculator.py

A module can contain:
    - Variables
    - Functions
    - Classes
    - Statements


PACKAGE
-------
A collection of Python modules organized in a directory.

Example:

mypackage/
    __init__.py
    calculator.py
    user.py


LIBRARY
-------
A general term for a collection of reusable code.

A library may contain multiple packages and modules.


PACKAGE MANAGER
---------------
A tool used to install and manage Python packages.

Python's most commonly used package manager:

    pip


VIRTUAL ENVIRONMENT
-------------------
An isolated Python environment for a particular project.


===============================================================================
1. VIRTUAL ENVIRONMENT
===============================================================================

WHAT IS A VIRTUAL ENVIRONMENT?
-------------------------------------------------------------------------------

A Virtual Environment is an isolated Python environment created for a project.

It allows each project to have its own:

    - Python packages
    - Package versions
    - Dependencies

without affecting other projects or the system/global environment.


WHY DO WE NEED A VIRTUAL ENVIRONMENT?
-------------------------------------------------------------------------------

Suppose we have a BASE / GLOBAL environment:

    numpy
    pandas
    langchain
    requests
    flask

Now suppose we have three projects:

    Project 1:
        pandas

    Project 2:
        pandas
        numpy

    Project 3:
        langchain
        numpy

Different projects may require different versions of the same package.

Example:

    Project 1 needs:

        pandas == 2.0

    Project 2 needs:

        pandas == 2.2

If everything is installed in one global environment, package-version
conflicts can occur.


VIRTUAL ENVIRONMENT SOLUTION
-------------------------------------------------------------------------------

Create a separate environment for each project:

    Project 1
        |
        +-- venv
            +-- pandas 2.0


    Project 2
        |
        +-- venv
            +-- pandas 2.2
            +-- numpy


    Project 3
        |
        +-- venv
            +-- langchain
            +-- numpy


Therefore:

    Project 1 -> its own dependencies
    Project 2 -> its own dependencies
    Project 3 -> its own dependencies


MAIN ADVANTAGES
-------------------------------------------------------------------------------

1. Dependency isolation
2. Avoids package-version conflicts
3. Cleaner projects
4. Easier project setup
5. Easier deployment
6. Easier collaboration
7. Makes dependency management predictable


===============================================================================
2. CREATING A VIRTUAL ENVIRONMENT
===============================================================================

COMMAND:

    python -m venv myenv

Meaning:

    python
        -> Run Python

    -m
        -> Run a Python module

    venv
        -> Python's built-in virtual environment module

    myenv
        -> Name of the virtual environment


Example:

    python -m venv myenv


This creates a directory:

    myenv/


Inside it Python creates the required environment files.


===============================================================================
3. ACTIVATING VIRTUAL ENVIRONMENT
===============================================================================

WINDOWS - CMD
-------------------------------------------------------------------------------

    myenv\Scripts\activate


WINDOWS - PowerShell
-------------------------------------------------------------------------------

    .\myenv\Scripts\Activate.ps1


After activation, the terminal generally shows:

    (myenv)

Example:

    (myenv) C:\project>


This indicates that the virtual environment is active.


===============================================================================
4. DEACTIVATING VIRTUAL ENVIRONMENT
===============================================================================

COMMAND:

    deactivate


After running:

    deactivate

the terminal returns to the previous/global environment.


===============================================================================
5. CHECKING PYTHON / PIP
===============================================================================

We can check the Python version:

    python --version


Check pip version:

    pip --version


We can also check which Python executable is being used.

Windows:

    where python


This is useful when debugging virtual-environment problems.


===============================================================================
6. pip
===============================================================================

pip is Python's package installer.

It is commonly used to:

    - Install packages
    - Upgrade packages
    - Uninstall packages
    - View installed packages


===============================================================================
7. pip list
===============================================================================

COMMAND:

    pip list


Shows the packages currently installed in the active environment.

Example:

    Package       Version
    ------------- -------
    pip           ...
    pandas        ...
    numpy         ...


IMPORTANT:

The result depends on which Python environment is currently active.


===============================================================================
8. INSTALLING A PACKAGE
===============================================================================

COMMAND:

    pip install package_name


Example:

    pip install pandas


After installation:

    import pandas


Now pandas can be used in the active environment.


===============================================================================
9. INSTALLING A SPECIFIC VERSION
===============================================================================

We can install a specific package version.

Syntax:

    pip install package_name==version


Example:

    pip install requests==2.31.0


IMPORTANT:

The version must be a valid version released for that package.


===============================================================================
10. UPGRADING A PACKAGE
===============================================================================

COMMAND:

    pip install --upgrade package_name


Example:

    pip install --upgrade pandas


===============================================================================
11. UNINSTALLING A PACKAGE
===============================================================================

COMMAND:

    pip uninstall package_name


Example:

    pip uninstall pandas


===============================================================================
12. REQUIREMENTS.TXT
===============================================================================

A Python project commonly contains:

    requirements.txt


It contains the project's dependencies.

Example:

    requirements.txt

could contain:

    pandas==2.2.3
    requests==2.32.3
    numpy==2.1.3


WHY IS requirements.txt IMPORTANT?
-------------------------------------------------------------------------------

Suppose we give our project to another developer.

They can install the required dependencies using:

    pip install -r requirements.txt


This helps reproduce the project's Python environment.


===============================================================================
13. CREATING requirements.txt
===============================================================================

A common command is:

    pip freeze > requirements.txt


This writes the currently installed packages and versions into:

    requirements.txt


Then another developer can run:

    pip install -r requirements.txt


IMPORTANT:

    pip freeze
        -> Shows installed packages with versions

    pip freeze > requirements.txt
        -> Saves that output into a file


===============================================================================
14. MODULE NOT FOUND ERROR
===============================================================================

Suppose pandas is installed in the GLOBAL environment.

But our virtual environment does not contain pandas.

If we activate our virtual environment and run:

    import pandas

we may get:

    ModuleNotFoundError:
    No module named 'pandas'


WHY?

Because packages installed in one environment are not automatically
available in another isolated virtual environment.


Solution:

Activate the correct environment and install pandas:

    pip install pandas


===============================================================================
15. IMPORTING A MODULE
===============================================================================

A module can be imported using:

    import module_name


Example:

    import pandas


Then we can access things from the module using:

    module_name.something


Example:

    import math

    print(math.sqrt(25))


Output:

    5.0


===============================================================================
16. IMPORT WITH ALIAS
===============================================================================

We can give a module a shorter name using:

    import module_name as alias


Example:

    import pandas as pd


Now instead of:

    pandas.DataFrame()


we can write:

    pd.DataFrame()


Another example:

    import math as m

    print(m.sqrt(25))


===============================================================================
17. FROM ... IMPORT
===============================================================================

We can import a specific function / class / variable from a module.

Syntax:

    from module_name import item


Example:

    from math import sqrt

    print(sqrt(25))


Output:

    5.0


We don't need to write:

    math.sqrt()


because sqrt itself has been imported.


===============================================================================
18. FROM ... IMPORT MULTIPLE ITEMS
===============================================================================

We can import multiple items:

    from math import sqrt, factorial


Example:

    from math import sqrt, factorial

    print(sqrt(25))
    print(factorial(5))


===============================================================================
19. IMPORT *
===============================================================================

Example:

    from math import *


This imports many names from the module.

However, this style is generally NOT recommended because it can:

    - Make code harder to understand
    - Cause naming conflicts
    - Make it unclear where a name came from

Prefer:

    import math

or:

    from math import sqrt


===============================================================================
20. BUILT-IN MODULE EXAMPLE
===============================================================================

Python comes with many built-in / standard-library modules.

Examples:

    math
    time
    os
    sys
    json
    random
    datetime
    threading


Example:

    import math

    print(math.pi)
    print(math.sqrt(16))


===============================================================================
21. CREATING OUR OWN REUSABLE MODULE
===============================================================================

We can create our own Python module.

Suppose we create:

    script6.py


Inside script6.py:

    def add(a, b):
        return a + b


    def sub(a, b):
        return a - b


This file itself becomes a module named:

    script6


===============================================================================
22. IMPORTING OUR OWN MODULE
===============================================================================

Suppose:

    script6.py

contains:

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b


Another file:

    script.py

can import it.


Example:

    import script6

    result = script6.add(5, 2)

    print(result)


Output:

    7


===============================================================================
23. IMPORTING WITH ALIAS
===============================================================================

We can use:

    import script6 as cal


Then:

    result = cal.add(5, 2)

    print(result)


Output:

    7


===============================================================================
24. IMPORTING A SPECIFIC FUNCTION
===============================================================================

Instead of importing the complete module:

    from script6 import sub


Then:

    result = sub(5, 2)

    print(result)


Output:

    3


===============================================================================
25. MODULE EXAMPLE
===============================================================================

FILE: script6.py
-------------------------------------------------------------------------------

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


FILE: script.py
-------------------------------------------------------------------------------

import script6

result = script6.add(5, 2)

print(result)


OR:

import script6 as cal

result = cal.add(5, 2)

print(result)


OR:

from script6 import sub

result = sub(5, 2)

print(result)


===============================================================================
26. __name__ == "__main__"
===============================================================================

A very important concept when creating reusable modules is:

    if __name__ == "__main__":


Every Python module has a special variable:

    __name__


When a Python file is run directly:

    python script6.py

Python sets:

    __name__ = "__main__"


But when the file is imported:

    import script6

then:

    __name__ = "script6"


Therefore we can write:

    if __name__ == "__main__":
        print("This file is being executed directly.")


This prevents certain code from automatically running when the module
is imported.


Example:

FILE: calculator.py

def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))


If we run:

    python calculator.py

Output:

    30


If another file imports:

    import calculator

the function is available, but the code inside:

    if __name__ == "__main__":

does not execute.


===============================================================================
27. MULTITHREADING
===============================================================================

WHAT IS A THREAD?
-------------------------------------------------------------------------------

A Thread is a small unit of execution within a process.

A program can have:

    Process
       |
       +-- Thread 1
       +-- Thread 2
       +-- Thread 3


A process can contain multiple threads.


===============================================================================
28. WHAT IS MULTITHREADING?
===============================================================================

Multithreading means executing multiple threads within the same process.

Example:

    Thread 1 -> Task A
    Thread 2 -> Task B
    Thread 3 -> Task C


Instead of waiting for one task to completely finish before starting
another, multiple tasks can make progress concurrently.


===============================================================================
29. WHY USE MULTITHREADING?
===============================================================================

Multithreading can be useful when tasks spend time waiting.

Common examples:

    - Network requests
    - API calls
    - File I/O
    - Database operations
    - Downloading files
    - Reading/writing files
    - Waiting for external services


For I/O-bound tasks, threads can allow another task to run while one
task is waiting.


===============================================================================
30. IMPORTANT: CONCURRENCY vs PARALLELISM
===============================================================================

CONCURRENCY
-------------------------------------------------------------------------------

Multiple tasks make progress during overlapping periods.

Example:

    Task A -> waiting
              Task B runs
              Task A continues


PARALLELISM
-------------------------------------------------------------------------------

Multiple tasks actually execute at the same time on multiple CPU cores.


IMPORTANT:

Python's threading behavior is affected by the CPython Global Interpreter
Lock (GIL).

Therefore, Python threads are generally more useful for I/O-bound work
than CPU-bound work in standard CPython.

For CPU-heavy parallel computation, multiprocessing or other approaches
may be more appropriate.


===============================================================================
31. IMPORTING threading
===============================================================================

Python provides the threading module:

    import threading


Example:

    import threading

    print(threading.current_thread())


===============================================================================
32. SIMPLE FUNCTION FOR THREADING
===============================================================================

We will create a function:

    task(name)

The function will:

    1. Print when the task starts
    2. Wait for 3 seconds
    3. Print when the task finishes
'''

import time


def task(name):
    print(f"{name} started..")

    time.sleep(3)

    print(f"{name} finished.")


# ============================================================================
# 33. NORMAL / SEQUENTIAL EXECUTION
# ============================================================================

'''
First, let's execute the tasks normally.

The tasks run one after another:

    Task1
       |
       v
    wait 3 sec
       |
       v
    Task2
       |
       v
    wait 3 sec
       |
       v
    Task3
       |
       v
    ...

With 5 tasks and each task sleeping for 3 seconds,
the total time will be approximately 15 seconds.

Actual time may vary slightly.
'''

start = time.time()

task("Task1")
task("Task2")
task("Task3")
task("Task4")
task("Task5")

end = time.time()

print("Sequential execution time:", end - start)


# ============================================================================
# 34. CREATING A THREAD
# ============================================================================

'''
We create a Thread object using:

    threading.Thread()

Syntax:

    threading.Thread(
        target=function,
        args=(arguments,)
    )


target:
    The function that the thread should execute.


args:
    Tuple containing arguments passed to the target function.


IMPORTANT:

    args=("Task1",)

The comma is important because this is a one-element tuple.

Without the comma:

    ("Task1")

is simply a string inside parentheses, not a tuple.
'''

import threading


thread1 = threading.Thread(
    target=task,
    args=("Task1",)
)


# ============================================================================
# 35. CREATING MULTIPLE THREADS
# ============================================================================

thread1 = threading.Thread(
    target=task,
    args=("Task1",)
)

thread2 = threading.Thread(
    target=task,
    args=("Task2",)
)

thread3 = threading.Thread(
    target=task,
    args=("Task3",)
)

thread4 = threading.Thread(
    target=task,
    args=("Task4",)
)

thread5 = threading.Thread(
    target=task,
    args=("Task5",)
)


# ============================================================================
# 36. STARTING THREADS
# ============================================================================

'''
start()

Starts the thread.

IMPORTANT:

Use:

    thread.start()

NOT:

    thread.run()


Calling start() creates a separate thread and begins execution.

Calling run() directly does NOT create a new thread in the same way;
it simply executes the target in the current thread.
'''

start = time.time()

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()


# ============================================================================
# 37. join()
# ============================================================================

'''
join()

The main thread waits for another thread to finish.

Example:

    thread1.join()

means:

    "Wait until thread1 has completed."


Why do we need join()?

Suppose we calculate execution time:

    start = time.time()

    thread1.start()
    thread2.start()

    end = time.time()

If we don't use join(), the main thread may reach "end" before
thread1 and thread2 finish.

Therefore, for our timing example, we use join().
'''

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

end = time.time()

print("Multithreading execution time:", end - start)


'''
Expected concept:

Sequential:

    Task1 -> 3 sec
    Task2 -> 3 sec
    Task3 -> 3 sec
    Task4 -> 3 sec
    Task5 -> 3 sec

    Approximately 15 seconds


Multithreading:

    Task1 ----\
    Task2 -----\
    Task3 ------> approximately 3 seconds
    Task4 -----/
    Task5 ----/


Actual timing may be slightly greater than 3 seconds because of
thread scheduling and system overhead.

IMPORTANT:

This does NOT mean every multithreaded program automatically becomes
faster.

The benefit depends on the type of work being performed.
'''


# ============================================================================
# 38. PRACTICAL MULTITHREADING EXAMPLE
# ============================================================================

'''
Let's create a function that prints each element of a list.

Each element takes 1 second to print.
'''

def delay_list_printer(my_list):

    for index, element in enumerate(my_list):

        print(
            f"element --> {element} position {index}"
        )

        time.sleep(1)


list1 = ["indra", "ram", "lucky"]
list2 = ["a", "b", "c"]
list3 = [10, 11, 12]


# ============================================================================
# 39. SEQUENTIAL EXECUTION OF LIST TASKS
# ============================================================================

'''
If we execute these normally:

    delay_list_printer(list1)
    delay_list_printer(list2)
    delay_list_printer(list3)

Each list takes approximately 3 seconds.

Total:

    approximately 9 seconds
'''

start = time.time()

# delay_list_printer(list1)
# delay_list_printer(list2)
# delay_list_printer(list3)

end = time.time()

print("Sequential execution time:", end - start)


# ============================================================================
# 40. MULTITHREADING WITH LISTS
# ============================================================================

'''
Create one thread for each list.
'''

thread1 = threading.Thread(
    target=delay_list_printer,
    args=(list1,)
)

thread2 = threading.Thread(
    target=delay_list_printer,
    args=(list2,)
)

thread3 = threading.Thread(
    target=delay_list_printer,
    args=(list3,)
)


# ============================================================================
# 41. STARTING LIST THREADS
# ============================================================================

start = time.time()

thread1.start()
thread2.start()
thread3.start()


# ============================================================================
# 42. WAITING FOR LIST THREADS
# ============================================================================

thread1.join()
thread2.join()
thread3.join()

end = time.time()

print("Multithreading execution time:", end - start)


'''
Expected concept:

Sequential:

    list1 -> 3 seconds
    list2 -> 3 seconds
    list3 -> 3 seconds

    Approximately 9 seconds.


Multithreading:

    list1 ----\
    list2 ----- > approximately 3 seconds
    list3 ----/


Again, actual timing depends on the system and thread scheduling.


===============================================================================
43. THREAD EXECUTION ORDER
===============================================================================

IMPORTANT:

The order in which threads start is NOT necessarily the order in which
their output appears.

Example:

    thread1.start()
    thread2.start()
    thread3.start()

does NOT guarantee:

    Task1
    Task2
    Task3

The output could be:

    Task2
    Task1
    Task3

or:

    Task1
    Task3
    Task2

because the operating system / Python runtime determines when threads
get execution time.


===============================================================================
44. start() vs run()
===============================================================================

thread.start()
    -> Starts a new thread
    -> Target function executes in that thread


thread.run()
    -> Calls the target function directly
    -> Does NOT provide the normal new-thread behavior


Example:

    thread = threading.Thread(target=task, args=("Task",))

    thread.start()


===============================================================================
45. start() vs join()
===============================================================================

start()
    -> Starts the thread


join()
    -> Makes the calling thread wait until that thread finishes


Example:

    thread.start()

    thread.join()

Meaning:

    Start thread
       |
       v
    Main thread waits
       |
       v
    Thread finishes
       |
       v
    Main thread continues


===============================================================================
46. MULTITHREADING WITH FUNCTION ARGUMENTS
===============================================================================

Example:

    def task(name, seconds):
        print(name)
        time.sleep(seconds)


Thread:

    thread = threading.Thread(
        target=task,
        args=("Download", 3)
    )


Here:

    target
        -> task

    args
        -> ("Download", 3)


===============================================================================
47. DAEMON THREAD
===============================================================================

A daemon thread is a background thread.

Example:

    thread = threading.Thread(
        target=task,
        args=("Background Task",),
        daemon=True
    )


A daemon thread does not normally keep the Python process alive after
all non-daemon threads have finished.

Use daemon threads carefully.

For important work such as saving data, database transactions, or
critical cleanup, do not rely on a daemon thread to finish its work.


===============================================================================
48. THREAD SAFETY
===============================================================================

When multiple threads access shared data, problems can occur.

Example:

    counter = 0

Multiple threads modifying the same shared variable can cause
race conditions.

Therefore, when threads share mutable data, synchronization may be
required.

Python provides synchronization tools such as:

    - Lock
    - RLock
    - Semaphore
    - Event
    - Condition


A Lock can be used to ensure that only one thread at a time enters
a critical section.


===============================================================================
49. BASIC LOCK EXAMPLE
===============================================================================
'''

lock = threading.Lock()

counter = 0


def increment():
    global counter

    for _ in range(1000):

        with lock:
            counter += 1


'''
Here:

    with lock:

ensures that the protected section is accessed safely by one thread
at a time.

This topic becomes more important when learning concurrent programming.


===============================================================================
50. WHEN TO USE MULTITHREADING?
===============================================================================

Good use cases:

    - API requests
    - Network operations
    - File operations
    - Database operations
    - Web scraping
    - Downloading files
    - Waiting for external services
    - I/O-bound applications


Generally not the first choice for:

    - Heavy CPU calculations
    - CPU-intensive data processing
    - CPU-heavy image/video processing

For CPU-bound work in standard CPython, multiprocessing or other
parallel/concurrent approaches may be more suitable.


===============================================================================
51. QUICK REVISION
===============================================================================

VIRTUAL ENVIRONMENT
-------------------

Create:

    python -m venv myenv

Activate - Windows CMD:

    myenv\Scripts\activate

Activate - Windows PowerShell:

    .\myenv\Scripts\Activate.ps1

Deactivate:

    deactivate


PIP
---

Show packages:

    pip list

Install:

    pip install pandas

Install specific version:

    pip install requests==2.31.0

Upgrade:

    pip install --upgrade pandas

Uninstall:

    pip uninstall pandas

Save dependencies:

    pip freeze > requirements.txt

Install dependencies:

    pip install -r requirements.txt


IMPORT
------

Import module:

    import math

Alias:

    import pandas as pd

Specific item:

    from math import sqrt


MODULE
------

A .py file containing reusable Python code.

Example:

    script6.py


REUSABLE MODULE
---------------

script6.py:

    def add(a, b):
        return a + b


script.py:

    import script6

    script6.add(5, 2)


MAIN CHECK
----------

    if __name__ == "__main__":
        ...


THREADING
---------

Import:

    import threading

Create:

    threading.Thread(
        target=function,
        args=(...)
    )

Start:

    thread.start()

Wait:

    thread.join()


IMPORTANT THREADING CONCEPTS
----------------------------

    Thread
    Multithreading
    Concurrency
    start()
    join()
    target
    args
    daemon
    Lock
    Race condition
    Thread safety


===============================================================================
52. QUICK COMPARISON TABLE
===============================================================================

+---------------------------+-----------------------------------------------+
| Concept                   | Meaning                                       |
+---------------------------+-----------------------------------------------+
| venv                      | Isolated Python environment                   |
| pip                       | Python package installer                      |
| pip list                  | Shows installed packages                     |
| pip install               | Installs a package                           |
| requirements.txt          | Project dependency list                      |
| module                    | Python file containing reusable code         |
| package                   | Collection of modules                        |
| import                    | Imports a module                             |
| from ... import           | Imports specific item                        |
| alias                     | Alternative name for imported module         |
| __name__                  | Special module variable                      |
| __main__                  | Indicates direct execution                  |
| thread                    | Unit of execution                            |
| threading                 | Python threading module                      |
| start()                   | Starts a thread                              |
| join()                    | Waits for a thread to finish                |
| target                    | Function executed by thread                  |
| args                      | Arguments passed to target function          |
| daemon                    | Background thread behavior                   |
| Lock                      | Synchronization mechanism                    |
| race condition            | Problem caused by unsafe shared access       |
+---------------------------+-----------------------------------------------+


===============================================================================
END OF CLASS NOTES
===============================================================================
'''