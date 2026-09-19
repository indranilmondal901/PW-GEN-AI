"""
1. List
2. Tuples
3. Dictionaries
4. Set
"""

# ============================================================================
# List
# ============================================================================
mylst1 = list()
mylst2 = []

print(mylst1, mylst2)
# [],[]

print(type(mylst1)); # <class 'list'>
print(type(mylst2)); # <class 'list'>

random_list = ["muskan", "rohit", "rahul", 50, 20, 10] ; 

# ----------------------------------------------------------
# indexing in list
# ----------------------------------------------------------
# indexing like --> [negative indexing like string ]
# 0: muskan -------> -6
# 1: rohit  -------> -5
# 2: rahul  -------> -4
# 3: 50     -------> -3
# 4: 20     -------> -2
# 5: 10     -------> -1


print(random_list); #['muskan', 'rohit', 'rahul', 50, 20, 10]
# print(random_list.length)
print(random_list[0]); # muskan
print(random_list[5]); # 10

print(random_list[-1]); # 10
print(random_list[-6]); # muskan

# ----------------------------------------------------------
# update list value
# ----------------------------------------------------------
random_list[1] = "indra"; # "rohit" ---> "indra"
print("after update ----> ", random_list);

# ----------------------------------------------------------
# Slicing
# ----------------------------------------------------------
print(random_list);
# print(random_list[:1]); # print(random_list[0:1]); ---> splice start -> 0 and end at starting of 1st index ---> 0 index will be there
# print(random_list[2:1]); # [] --> it is actually wrong ---> splice start -> 2 and end at starting of 1st index
print(random_list[2:5]); # ['rahul', 50, 20] ---> splice start -> 2 and end at starting of 5th index ---> 2,3,4 indexes will be there

# ----------------------------------------------------------
# insert --> add in the particular index provided
# ----------------------------------------------------------
random_list.insert(0,"0 index")
random_list.insert(2,"2nd index")
print(random_list);

# ----------------------------------------------------------
# append --> add in the last index of list
# ----------------------------------------------------------
random_list.append("append");
print(random_list);

# ----------------------------------------------------------
#  extened --> we can add multiple item ata a time
# ----------------------------------------------------------
new_list = ["new1","new2","new30"];
random_list.extend(new_list);
print(random_list);

# ----------------------------------------------------------
#  remove
# ----------------------------------------------------------
