
# Module Lab: Building a Python Command-Line Interface Tool

module-lab-python-cli-tool/
│
├── lib/
│   ├── __init__.py
│   ├── models.py
│   └── cli_tool.py
│
├── testing/
│   ├── __init__.py
│   └── test_cli_tool.py
│
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── .gitignore

## Learning Goals

- Build modular and user-friendly command-line applications using `argparse`.
- Apply object-oriented programming (OOP) to map real-world objects to CLI commands.
- Validate user input and provide helpful feedback.
- Structure CLI tools for maintainability and scalability.

## Introduction

In this lab, you'll design and implement a Python Command-Line Interface (CLI) tool that models real-world behavior using OOP. You'll use Python's built-in `argparse` module to define commands, and object-oriented classes to manage task-related actions.

The CLI tool will allow users to:

- Add tasks to a user account via `add-task`
- Mark tasks as complete via `complete-task`
- Display feedback directly in the terminal

This lab combines CLI architecture with OOP principles to help you build intuitive and testable developer tools.

## Setup Instructions

### Fork and Clone the Repository

1. Go to the provided GitHub repository link.
2. Fork the repository to your GitHub account.
3. Clone the forked repository to your local machine using:

```bash
git clone <repo-url>
cd module-lab-python-cli-tool
```

### Install Python and Dependencies

Ensure Python is installed:

```bash
python --version
```

Optionally, create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

# 3. Install dependencies (pytest)
pip install pytest
# (Alternatively, if you have pipenv installed: pipenv install)
---

# runing

# Add a task for Alice
python -m lib.cli_tool add-task Alice "Write unit tests"
# Expected Output: 📌 Task 'Write unit tests' added to Alice.

# Complete the task for Alice
python -m lib.cli_tool complete-task Alice "Write unit tests"
# Expected Output: ✅ Task 'Write unit tests' completed.

# Test error handling: User not found
python -m lib.cli_tool complete-task Bob "Write unit tests"
# Expected Output: ❌ User not found.

# Test error handling: Task not found
python -m lib.cli_tool complete-task Alice "Nonexistent task"
# Expected Output: ❌ Task not found.

# Test help menu (no arguments provided)
python -m lib.cli_tool
# Expected Output: Displays the argparse help menu.

# pytest
pytest testing/test_cli_tool.py -v

## Tasks

### Task 1: Define the Problem

Build a CLI tool that allows users to:

- Add tasks to their name
- Mark tasks as complete
- See helpful feedback after actions

The tool should simulate how users interact with a task manager, mapping commands to behavior using classes.

---

### Task 2: Determine the Design

Your application will be split into:

- A `Task` class to represent individual tasks
- A `User` class to group tasks under a user's name
- A CLI controller using `argparse` with `subparsers` to route actions

This design keeps your logic modular, object-oriented, and easy to extend.

---

### Task 3: Develop the CLI Tool

#### Step 1: Define Your Classes in `lib/models.py`

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")
```

#### Step 2: Create the CLI in `lib/cli_tool.py`

```python
import argparse
from lib.models import Task, User

users = {}

def add_task(args):
    user = users.get(args.user) or User(args.user)
    users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    user = users.get(args.user)
    if user:
        for task in user.tasks:
            if task.title == args.title:
                task.complete()
                return
        print("❌ Task not found.")
    else:
        print("❌ User not found.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    complete_parser = subparsers.add_parser("complete-task", help="Complete a task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

---

### Task 4: Run and Test the CLI Tool

```bash
# Add a task
python lib/cli_tool.py add-task Alice "Write unit tests"

# Complete a task
python lib/cli_tool.py complete-task Alice "Write unit tests"
```

---

## Best Practices

- Use `argparse` to guide the user experience.
- Validate input with helpful error messages.
- Keep CLI and OOP logic modular and separated.
- Document your script and commands clearly in the README.
- Use the `__main__` guard to make your CLI script reusable.

---

## Conclusion

After completing this lab, you will:

✅ Build structured and modular CLI tools in Python  
✅ Map real-world entities using object-oriented design  
✅ Create terminal experiences with helpful input/output  
✅ Apply argparse and OOP to real development workflows

These skills help you build maintainable CLI tools that scale with complexity and support real-world use cases.
