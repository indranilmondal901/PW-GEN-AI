# Dictionary
# key value pair

myDict = dict()
# new empty dictionary will be initiated
print(myDict)
# {}

"""
key -- always should be String
value -- any dataType
"""
# creating a Dictionary
myDict = {"name": "Rahul", "age": 28, "course": "Gen AI"}
print(myDict);

# fetch value or access value
name = myDict.get("name");
keyNotExist = myDict.get("keyNotExist","nhi h key");

print(name);# Rahul

print(keyNotExist); # nhi h key