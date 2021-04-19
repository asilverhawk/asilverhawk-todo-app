#!/usr/bin/env python3
import sys

from methods import list_tasks, add_task, remove_task, complete_task

# Count the arguments
command = sys.argv

disc_msg = """
To run todo application please enter todo with an argument

Command Line Todo application
=============================

Command line arguments:
-l   Lists all the tasks EX: todo -l
-a   Adds a new task EX: todo -a "task title"
-r   Removes an task EX: todo -r int(task_id)
-c   Completes an task EX: todo -c int(task_id)
"""

supported_args = ['-a', '-l', '-c', '-r']


def error_message(command=None):
    if command:
        if command[1].lower() not in supported_args:
            print("Unsupported argument")
        elif command[1].lower() == '-a':
            if len(command) == 2:
                print("Unable to add: no task provided")
        elif command[1].lower() == '-r':
            if len(command) == 2:
                print("Unable to remove: no index provided")
            elif len(command) == 3 and not command[2].isdigit():
                print("Unable to remove: index is not a number")
        elif command[1].lower() == '-c':
            if len(command) == 2:
                print("Unable to check: no index provided")
            elif len(command) == 3 and not command[2].isdigit():
                print("Unable to check: index is not a number")

    print("-" * 10)
    print("Got invalid argument")
    print("-" * 10)
    print(disc_msg)


try:
    if len(command) == 1:
        print(disc_msg)
    elif command[1].lower() == '-l':
        """
        read from file
        list from file
        """
        if len(command) - 1 == 1:
            list_tasks()
        else:
            error_message()

    elif command[1].lower() == '-a':
        """
        append new task to list
        """
        if len(command) - 1 == 2:
            add_task(command[2])
        else:
            error_message(command)

    elif command[1].lower() == '-r':
        """
        read from file
        print content
        """
        if len(command) == 3 and command[2].isdigit():
            remove_task(command[2])
        else:
            error_message(command)

    elif command[1].lower() == '-c':
        """
        read
        """
        if len(command) - 1 == 2 and command[2].isdigit():
            complete_task(command[2])
        else:
            error_message(command)
    else:
        error_message(command)
except FileNotFoundError as e:
    print(f"Error: {str(e)}")
    print(">>> please create new file named tasks.txt")
except Exception as e:
    print(f"Error: {str(e)}")
print("Thanks for using todo app")
