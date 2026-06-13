# # # # #  # list --> Save multiple items in a single variable
# # # # # # How to get the data from list
# # # # # tools = ["AWS,", "Azure", "GCP", "Terraform", "Ansible", "Docker", "Kubernetes"]
# # # # # #print(tools)
# # # # # #print(type(tools))
# # # # # #tools = [0]
# # # # # #tools = [0,1,2,3,4,5,6]
# # # # # # aws = 0
# # # # # # azure = 1
# # # # # # gcp = 2
# # # # # # terraform = 3
# # # # # # ansible = 4
# # # # # # docker = 5
# # # # # # kubernetes = 6


# # # # # # numbers = [1, 2, 3, 4, 5]
# # # # # # #print(numbers)
# # # # # # print(numbers[0])
# # # # # # print(numbers[4])
# # # # # # print(numbers)
# # # # # #print(numbers[5]) -- IndexError: list index out of range

# # # # # #print(type(numbers))

# # # # # #mixed_list = ["AWS,", 1, "Azure", 2, "GCP", 3, "Terraform", 4, "Ansible", 5, "Docker", 6, "Kubernetes", 7]
# # # # # #print(mixed_list)
# # # # # #print(type(mixed_list))

# # # # # # Negative indexing
# # # # # #print(tools[-1])  # Kubernetes
# # # # # #print(tools[-2])  # Docker
# # # # # #print(tools[-3])  # Ansible


# # # # # # list silicing
# # # # # #print(tools[0:3]) # inlcude start  but last exclude end

# # # # # #print(tools[:])

# # # # # number = [1, 2, 3, 4, 5]
# # # # # # # print(number[2:4]) # 3,4
# # # # # #  # 1,3,4
# # # # # #  # numbers[start : end : step]
# # # # # #  # steps by default is 1
# # # # # # print(number[0:5:2]) # 1,3,5
# # # # # # Append
# # # # # # If we want to add (append) new item in list
# # # # # tools.append("Git")
# # # # # print(tools)

# # # # # # POP 
# # # # # # If we want to remove item from list
# # # # # tools.pop() # remove last item from list
# # # # # print(tools)
# # # # # tools.pop(0) # remove item from index 0
# # # # # print(tools)

# # # # # # add
# # # # # # If we want to add item in list at specific index
# # # # # tools.insert(7, "Git")
# # # # # tools.insert(0, "AWS")
# # # # # print(tools)

# # # # # # Remove
# # # # # # If we want to remove item from list by name
# # # # # tools.remove("Git")     
# # # # # print(tools)


# # # # # Dictionary
# # # # # # Dictionary --> Save data in key value pair
# # # # # student = {
# # # # #     "name": "Danish",
# # # # #     "age": 20,
# # # # #     "city": "Karachi"
# # # # # }

# # # # # print(student)

# # # # clinet = {
# # # #     "name" : "Ali",
# # # #     "Industry" : "IT",
# # # #     "project" : "3",
# # # #     "Active" : "Yes"

# # # # }
# # # # print(clinet)

# # # # print(clinet["name"])
# # # # print(clinet["Industry"])
# # # # print(clinet["project"])
# # # # print(clinet["Active"])


# # # # # clinet ["inactive"] # Error: KeyError: 'inactive' -- because this key is not exist in dictionary
# # # # # print(clinet)

# # # # # Method 
# # # # # Get method
# # # # print(clinet.get("name")) # Return value of key "name"
# # # # clinet.get("inactive","NOt Found") # Return "NOt Found" because this key is not exist in dictionary
# # # # print(clinet.get("inactive")) # Return None because this key is not exist in dictionary

# # # # Modifying a Dictionary in Python

# # # from multiprocessing.connection import Client


# # # student = {
# # #     "name": "Danish",
# # #     "age": 20,
# # #     "city": "Karachi"
# # # }
# # # print(student)
# # # # 1. Change an Existing Value
# # # student["age"] = 21
# # # print(student)

# # # # 2. Add a New Key-Value Pair
# # # student["course"] = "Python"
# # # student["grade"] = "A"
# # # print(student)
# # # # 3. Remove a Key-Value Pair
# # # del student["course"]
# # # del student["grade"]
# # # print(student)

# # # # 4. Update Multiple Values
# # # student.update({"age": 22, "city": "Lahore"})
# # # print(student)

# # # # 5. Clear the Dictionary
# # # student.clear()
# # # print(student)

# # # # Short Note

# # # # Dictionary modification means changing existing values 
# # # # or adding new key-value pairs using the key name.


# # # # NEsted Dictionary
# # # Client = {
# # #     "daniyal": {
# # #         "name": "Daniyal",
# # #         "age": 25,
# # #         "city": "Karachi"
# # #     },
# # #     "ali": {
# # #         "name": "Ali",
# # #         "age": 30,
# # #         "city": "Lahore"
# # #     }
# # # }

# # # print(Client["daniyal"]["name"])

# # # Nested List
# # nasted_list = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ]
# # print(nasted_list[0])
# # print(nasted_list[0][1])
# # print(nasted_list[1][2]) # 6
# # print(nasted_list[2][0]) # 7
# # print(nasted_list)

# # String Methods
# # String methods are built-in functions in Python 
# # that help you work with and modify text (strings) easily.

# name = "  Danish  Abbas  "
# print(name.upper()) # Convert string to uppercase
# print(name.lower()) # Convert string to lowercase
# print(name.title()) # Convert string to title case
# print(name.strip()) # Remove whitespace from both ends
# print(name.replace("Danish", "Ali")) # Replace a substring
# print(name.capitalize()) # Capitalize the first letter of the string
# print(name.split()) # Split the string into a list of words
