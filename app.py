import sys
import json

def main():
    # 读取任务列表
    try:
        with open("task_list.json", "r") as file:
            json_string = file.read()
            task_list = json.loads(json_string)
    except (FileNotFoundError, json.JSONDecodeError):
        task_list = []

    if len(sys.argv) < 2:
        print("Please provide a command.")
        return

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 3:
            print("Please provide a task description.")
            return
        task_id = task_list[-1][0] + 1 if task_list else 1
        task_list.append([task_id, sys.argv[2], 'todo'])
        print(f'Task added successfully (ID: {task_id})')

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Please provide task ID and new description.")
            return
        try:
            task_id = int(sys.argv[2])
            for task in task_list:
                if task[0] == task_id:
                    task[1] = sys.argv[3]
                    break
            else:
                print("Task ID not found.")
        except ValueError:
            print("Invalid task ID.")

    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Please provide task ID.")
            return
        try:
            task_id = int(sys.argv[2])
            task_list = [task for task in task_list if task[0] != task_id]
        except ValueError:
            print("Invalid task ID.")

    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Please provide task ID.")
            return
        try:
            task_id = int(sys.argv[2])
            for task in task_list:
                if task[0] == task_id:
                    task[2] = 'in progress'
                    break
            else:
                print("Task ID not found.")
        except ValueError:
            print("Invalid task ID.")

    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Please provide task ID.")
            return
        try:
            task_id = int(sys.argv[2])
            for task in task_list:
                if task[0] == task_id:
                    task[2] = 'done'
                    break
            else:
                print("Task ID not found.")
        except ValueError:
            print("Invalid task ID.")

    elif command == 'list':
        if len(sys.argv) < 3:
            for task in task_list:
                print(task)
        else:
            status = ['done', 'in-progress', 'todo']
            if sys.argv[2] not in status:
                print("Invalid status.")

            else:
                found = False
                if sys.argv[2] == 'done':
                    for task in task_list:
                        if task[2] == 'done':
                            print(f"ID: {task[0]} | Task: {task[1]} | Status: {task[2]}")
                            found = True
                    if found == False:
                        print("No task with status done.")
                elif sys.argv[2] == 'todo':
                    for task in task_list:
                        if task[2] == 'todo':
                            print(f"ID: {task[0]} | Task: {task[1]} | Status: {task[2]}")
                            found = True
                    if found == False:
                        print("No task with status todo.")
                elif sys.argv[2] == 'in-progress':
                    for task in task_list:
                        if task[2] == 'in progress':
                            print(f"ID: {task[0]} | Task: {task[1]} | Status: {task[2]}")
                            found = True
                    if found == False:
                        print("No task with status in progress.")  
                
                




    else:
        print("Unknown command.")

    # 保存更新
    with open("task_list.json", "w") as file:
        json.dump(task_list, file, indent=4)


if __name__ == "__main__":
    main()
