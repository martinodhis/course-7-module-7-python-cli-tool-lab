# lib/cli_tool.py

import argparse
from lib.models import Task, User

# Global dictionary to store users and their tasks (in-memory)
users = {}

def add_task(args):
    # Check if the user exists, if not, create one
    if args.user not in users:
        users[args.user] = User(args.user)
    
    user = users[args.user]
    # Create a new Task with the given title
    task = Task(args.title)
    # Add the task to the user's task list
    user.add_task(task)

def complete_task(args):
    # Look up the user by name
    user = users.get(args.user)
    if user:
        # Look up the task by title
        task = user.get_task_by_title(args.title)
        if task:
            # Mark the task as complete
            task.complete()
        else:
            # Print appropriate error messages if not found
            print("❌ Task not found.")
    else:
        # Print appropriate error messages if not found
        print("❌ User not found.")

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    # dest="command" ensures args.command is populated, helpful for debugging
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user", help="Name of the user")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user", help="Name of the user")
    complete_parser.add_argument("title", help="Title of the task")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    
    # Execute the mapped function if a valid command was provided
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()