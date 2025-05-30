import sys

def main():
    task_list = []
    if sys.argv[1] == 'add':
        num = len(task_list) + 1
        task_list.append([num, sys.argv[2], 'todo'])
        print(f'Task added succrssfully (ID: {num})')
    if sys.argv[1] == 'update':
        find_num = int(sys.argv[2]) - 1
        task_list[find_num][1] = sys.argv[3]
    if sys.argv[1] == 'delete':
        find_num = int(sys.argv[2]) - 1
        task_list.remove(task_list[find_num])
    if sys.argv[1] == 'mark-in-progress':
        find_num = int(sys.argv[2]) - 1
        task_list[find_num][3] = 'in progress'
    if sys.argv[1] == 'done':
        find_num = int(sys.argv[2]) - 1
        task_list[find_num][3] = 'done'
    if sys.argv[1] == 'list':
        for task in task_list:
            print(task)


    























if __name__ == "__main__":
    main()