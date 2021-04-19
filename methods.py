import os


def file_len(fname):
    flag = False
    with open(fname) as f:
        for i, l in enumerate(f):
            flag = True
            pass
    return i + 2 if flag else 1


def list_tasks():
    exist = False
    with open("tasks.txt", 'r') as f:
        for line in f:
            exist = True
            print(line)
    if not exist:
        print("No todos for today! :)")


def add_task(task):
    file_name = "tasks.txt"
    line_count = file_len(file_name)
    with open(file_name, '+a') as f:
        f.write(f"{line_count} - [ ] {task}\n")
    print(f"Task {task} added")


def remove_task(task_id):
    tasks = open("tasks.txt", 'r')
    tasks_list = tasks.readlines()
    tasks.close()
    tasks = open("tasks.txt", 'w')
    delete = False

    for idx, _ in enumerate(tasks_list):
        if tasks_list[idx].startswith(str(task_id)):
            delete = True
        if delete:
            tasks_list[idx] = '' if idx == len(tasks_list) - 1 else f"{idx} - [{tasks_list[idx + 1].split(f' - [')[-1]}"
    # tasks = open("tasks.txt", 'w')
    tasks.writelines(tasks_list)

    if delete:
        print("Task deleted")
    else:
        print("Unable to remove: index is out of bound")

    tasks.close()


def complete_task(task_id):
    tasks = open("tasks.txt", 'r')
    tasks_list = tasks.readlines()
    tasks.close()
    tasks = open("tasks.txt", 'w')
    change = False
    for idx, _ in enumerate(tasks_list):
        if tasks_list[idx].startswith(f"{str(task_id)} - [ ]"):
            tasks_list[idx] = f'{str(task_id)} - [X] {tasks_list[idx].split(f"{str(task_id)} - [ ] ")[-1]}'
            change = True
            break

    tasks.writelines(tasks_list)

    if change:
        print("task completed!")
    else:
        print("Unable to check: index is out of bound")

    tasks.close()
