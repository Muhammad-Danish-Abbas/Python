## 📁 Files Overview
 
| File | Topic |
|------|-------|
| `conditionals.py` | If / Elif / Else statements |
| `loops.py` | For loop, While loop, Break, Continue, Nested Loops |
 
---
 
## 📌 1. Conditional Statements (`if / elif / else`)
 
### Syntax
```python
if condition:
    # code to execute
elif condition:
    # code to execute
else:
    # code to execute
```
 
### How it works
- `if` — pehla condition check karta hai
- `elif` — agar pehla False ho, toh yeh check hota hai
- `else` — agar sab False ho, toh yeh run hota hai
### Examples from file
 
**Check karna ke koi item list mein hai ya nahi:**
```python
tools = ["AWS", "Azure", "Docker", "Kubernetes"]
 
if "AWS" in tools:
    print("AWS is in the list")
else:
    print("AWS is not in the list")
```
 
**Multiple conditions (elif):**
```python
if "GCP" in tools:
    print("GCP is in the list")
elif "AWS" in tools:
    print("AWS is in the list")
else:
    print("GCP and AWS are not in the list")
```
 
**User input ke saath (Voting eligibility):**
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```
 
### Key Points
- Condition ke baad `:` (colon) zaroori hai
- Indentation (4 spaces) zaroori hai — warna error aayega
- `in` keyword list mein item dhundhne ke liye use hota hai
- `int(input())` se user se number liya jaata hai
---
 
## 📌 2. Loops
 
### 🔁 For Loop
 
**Syntax:**
```python
for item in iterable:
    # code to execute
```
 
**`range()` function ke examples:**
```python
range(10)      # → 0, 1, 2, ..., 9
range(1, 6)    # → 1, 2, 3, 4, 5
range(10, 15)  # → 10, 11, 12, 13, 14
```
 
**List loop karna:**
```python
tools = ["AWS", "Azure", "GCP", "Docker", "Kubernetes"]
for tool in tools:
    print(tool)
```
 
**String ke characters loop karna:**
```python
tool = "Python"
for char in tool:
    print(char)
# Output: P y t h o n (ek ek line pe)
```
 
**Dictionary loop karna:**
```python
Client = {"name": "Danish", "age": 30, "city": "Karachi"}
 
for key in Client.keys():
    print(key)
 
for value in Client.values():
    print(value)
 
for item in Client.items():
    print(item)   # → (key, value) tuples
```
 
---
 
### ⏸️ Break & Continue
 
**`break`** — loop ko turant band kar deta hai:
```python
for i in range(10):
    if i == 5:
        break       # 5 pe aake loop ruk jaayega
    print(i)        # Output: 0 1 2 3 4
```
 
**`continue`** — current iteration skip karta hai, loop chalti rehti hai:
```python
for i in range(10):
    if i == 5:
        continue    # 5 skip ho jaayega
    print(i)        # Output: 0 1 2 3 4 6 7 8 9
```
 
---
 
### 🔄 While Loop
 
**Syntax:**
```python
while condition:
    # code to execute
```
 
**Example:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1     # i = i + 1 — yeh zaroori hai warna infinite loop
```
 
**While loop mein break:**
```python
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
```
 
> ⚠️ **Warning:** While loop mein counter update karna mat bhoolo, warna loop kabhi band nahi hoga!
 
---
 
### 🔲 Nested Loops
 
Loop ke andar loop — har outer iteration ke liye inner loop puri chalta hai.
 
**Star pattern print karna:**
```python
for i in range(5):
    for j in range(5):
        print("*", end="")   # end="" se newline nahi aata
    print()                  # row ke baad newline
# Output:
# *****
# *****
# *****
# *****
# *****
```
 
**2D list (matrix) ka row sum nikalna:**
```python
lists = [
    [2, 11, 7, 12],
    [5, 2, 9, 15],
    [8, 3, 10, 42]
]
 
for sublist in lists:
    row_sum = 0
    for item in sublist:
        row_sum += item
    print("Row sum:", row_sum)
```
 
---
 
### 📝 Word Count Program (Practical Example)
 
```python
sentence = input("Enter a sentence: ")
word_count = 0
 
for word in sentence.split():
    word_count += 1
 
print("Word count:", word_count)
```
 
- `.split()` — sentence ko words mein tod deta hai (spaces pe)
- Har word pe counter `+1` hota hai
---
 
## 🧠 Quick Summary Table
 
| Concept | Keyword | Use Case |
|---------|---------|----------|
| Condition check | `if / elif / else` | Decision making |
| List mein dhundna | `in` | Membership check |
| Fixed iterations | `for` | List, range, string loop |
| Condition based loop | `while` | Jab pata nahi kitni bar chalega |
| Loop band karna | `break` | Early exit |
| Iteration skip karna | `continue` | Skip specific case |
| Loop andar loop | Nested loop | Matrix, patterns |
 
---
 
## 💡 Common Mistakes to Avoid
 
1. **Colon bhoolna** → `if age >= 18` ❌ | `if age >= 18:` ✅
2. **Indentation galat karna** → Python mein indent hi block define karta hai
3. **While mein counter update na karna** → Infinite loop aa jaayega
4. **`range(list)` use karna** → `range(len(list))` ya seedha `for item in list` use karo
5. **`int()` wrap karna input pe** → `input()` hamesha string deta hai, number chahiye toh `int()` zaroori hai
---
 
*Made with ❤️ for Python Basics practice*