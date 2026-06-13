# 🐍 Python Notes — Lists, Dictionaries & String Methods

> Beginner-friendly Python notes covering core data structures and string manipulation.  
> Written during hands-on practice sessions. 🚀

---

## 📁 What's Covered

| Topic | Description |
|-------|-------------|
| 📋 **Lists** | Creating, indexing, slicing, appending, removing items |
| 📖 **Dictionaries** | Key-value pairs, nested dicts, modifying, updating |
| 🔤 **String Methods** | `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()` & more |
| 🔢 **Nested Structures** | Nested lists & nested dictionaries |

---

## 📚 Topics in Detail

### 📋 Lists
- What is a list? — Storing multiple items in one variable
- Indexing (positive & negative)
- Slicing with `[start:end:step]`
- Methods: `.append()`, `.pop()`, `.insert()`, `.remove()`

### 📖 Dictionaries
- Key-value pair concept
- Accessing values using keys & `.get()` method
- Modifying: update, add, delete keys
- Nested dictionaries

### 🔤 String Methods
- Case conversion: `.upper()`, `.lower()`, `.title()`, `.capitalize()`
- Cleaning: `.strip()`
- Manipulation: `.replace()`, `.split()`

---

## 🛠️ How to Run

```bash
# Make sure Python is installed
python --version

# Run any file
python filename.py
```

---

## 🧠 Quick Reference

```python
# List
tools = ["AWS", "Azure", "GCP", "Docker"]
tools.append("Git")       # Add item
tools.pop()               # Remove last item
tools[0:3]                # Slicing

# Dictionary
student = {"name": "Danish", "age": 20}
student["city"] = "Karachi"    # Add new key
student.get("grade", "N/A")    # Safe access

# String Methods
name = "  danish  "
name.strip().title()      # "Danish"
name.replace("danish", "ali")
```

---

## 👨‍💻 Author

**Muhammad Danish**  
Student — Faculty of Computing & Information Technology  
Indus University, Karachi  

---

## 📌 Notes

- All code examples are written and tested in Python 3
- Comments are included in the source files for easy understanding
- Great for beginners starting their Python journey!

---

⭐ *If this helped you, give it a star!*
