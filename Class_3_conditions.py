 # Conditionnal statements

# if statement

# if condition:
#     code to execute
# elif condition:
#     code to execute
# else:


tools = ["AWS", "Azure",  "Docker", "Kubernetes"]
# if "AWS" in tools:
#     print("AWS is in the list")
# else:
#     print("AWS is not in the list")

# if "GCP" in tools:
#     print("GCP is in the list")
# else:
#     print("GCP is not in the list")

# if "GCP" in tools:
#     print("GCP is in the list")
# elif "AWS" in tools:
#     print("AWS is in the list")
# else:
#     print("GCP and AWS are not in the list")
age = int(input("Enter your age: "))
if age >= 18: 
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")