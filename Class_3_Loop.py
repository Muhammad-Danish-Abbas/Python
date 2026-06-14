# # # Loop
# # # A repeat a block of code multiple times. 
# # # It is used to perform a task repeatedly 
# # # until a certain condition is met.

# # # Example 1: Using a for loop to print numbers from 1 to 5

# # # For Loop
# # # Syantx 
# # # for item in iterable:
# # #     code to execute
# #  #    print("Hello World")

# # # for i in range(1, 6):
# # #     print(i)

# # # Range(10)--> 0,1,2,3,4,5,6,7,8,9
# # # Range(1, 6)--> 1,2,3,4,5
# # # for i in range(10):
# # #     print(i)

# # # tools = ["AWS", "Azure", "GCP", "Docker", "Kubernetes"]
# # # for tool in tools:
# # #     print(tool)

# # # for i in range(10,15):
# # #     print(i)

# # # tool = "Python"
# # # for char in tool:
# # #     print(char)
# # # output:
# # # P 
# # # y
# # # t
# # # h
# # # o
# # # n

# # # tools = ["AWS", "Azure", "GCP", "Docker", "Kubernetes"]
# # # for i in range(tools):
# # #     print(i)

# # # By using Range Function
# # # tools = ["AWS", "Azure", "GCP", "Docker", "Kubernetes"]
# # # for i in range(5):
# # #     print(tools[i])

# # # Looping thorugh the dictionary



# # Client = {
# #     "name": "Danish",
# #     "age": 30,
# #     "city": "Karachi"
# # }

# # # print(Client.keys())

# # # print(Client.values())

# # # for value in Client.values():
# # #     print(value)

# # # print(Client.items())

# # for key in Client.items():
# #     print(key)

# # Break and Continue
# # for i in range(10):
# #     break
#     # if i == 5:
#     #     break
#     # print(i)

# # for i in range(10):
# #  print(i)

# #  if i == 5:
# #    print("i is 5, skipping the rest of the code in this iteration")
# #    break

# # COntinue
# # for i in range(10):
# #     if i == 5:
# #         print("i is 5, skipping the rest of the code in this iteration")
# #         continue
# #     print(i)


# # While loop: A while loop repeats a block of code as long as a condition is True.
# # while condition:
# #     code to execute
# # i = 1
# # while i <= 5:
# #     print(i)
# #     i += 1

# # Break and Continue in while loop
# # i = 1
# # while i <= 10:
# #     if i == 5:
# #         print("i is 5, breaking the loop")
# #         break
# #     print(i)
# #     i += 1
# # # continue
# # i = 1
# # while i <= 10:
# #     if i == 5:
# #         print("i is 5, skipping the rest of the code in this iteration")
# #         continue
# #     print(i)
# #     i += 1

# # Nested Loops: A nested loop is a loop inside another loop.
# #  The inner loop will be executed one time for each iteration of the outer loop.
# # ******
# # ******
# # ******
# # ******

# # for i in range(5):
# #     for j in range(5):
# #         print(i,j)

# for i in range(5):
#     for j in range(5):
#         print("*", end="")
#     print()


# lists = [
#     [2, 11, 7, 12],
#     [5, 2, 9, 15],
#     [8, 3, 10, 42]
# ]

# for sublist in lists:
#     row_sum = 0

#     for item in sublist:
#         row_sum += item

#     print("Row sum:", row_sum)

sentence = input("Enter a sentence: ")
word_count = 0

for word in sentence.split():
    word_count += 1

print("Word count:", word_count)
