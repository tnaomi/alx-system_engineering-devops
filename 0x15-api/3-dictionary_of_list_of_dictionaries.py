#!/usr/bin/python3
""" Call the JSONPlaceholder API, export data as JSON"""

import json
import requests as RQ
import sys


if __name__ == "__main__":
    users = RQ.get("https://jsonplaceholder.typicode.com/users")
    all_users = users.json()
    todos = RQ.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    
    all_todos = {}

    for user in all_users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {
                        "username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')
                        }
                task_list.append(task_dict)
        all_todos[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_todos, f)
