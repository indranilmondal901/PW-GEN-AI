# 1. writing your first python script
# 2. Print Statement
# 3. Comments
# 4. Escape Sequences
# 5. Debugging Basics
# 6. small practice exercises

# function --> print() --> print function is used to print the output on the console

# Print statement
print("Hello World!")  
print("This is my first python script")
# hvjhchjvs -- NameError: name 'hvjhchjvs' is not defined
# print(hello world) -- SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Last line of the script")

# This is a comment, it will not be executed by Python

# \n	New line	            ---->   "Hello\nWorld"	    ---->   Hello World
# \t	Tab	                    ---->   "Hello\tWorld"	    ---->   Hello World
# \\	Backslash	            ---->   "C:\\Users\\Admin"	---->   C:\Users\Admin
# \'	Single quote	        ---->   'It\'s good'	    ---->	It's good
# \"	Double quote	        ---->    "He said \"Hi\""	---->	He said "Hi"
# \b	Backspace	            ---->   "ABC\bD"	        ---->	ABD*
# \r	Carriage return	        ---->   "Hello\rHi"	        ---->	Hi**

'''
aaa
nn 
kkk
kkk
'''
# need to use escape sequence
name="indra";
age=21;
city="kolkata"
skill="python"
print("======","\nMy Profile", "\n======","Name:\t",name,"\nAge:\t",age,"\nCity:\t",city,"\nSkill:\t",skill) # explanation - \ is used to escape the special characters