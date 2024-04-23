#!/usr/bin/python3
""" A Script that calls the JSONPlaceholder API"""

import csv
import requests as RQ
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    employee = '{}users/{}'.format(url, user_id)
    response = RQ.get(employee)
    json_data = response.json()
    name = json_data.get('username')

    todos = '{}todos?userId={}'.format(url, user_id)
    response = RQ.get(todos)
    tasks = response.json()
    task_list = []
    for task in tasks:
        task_list.append([user_id,
                          name,
                          task.get('completed'),
                          task.get('title')])

    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w') as F:
        employee_csv = csv.writer(F,
                                  delimiter=',',
                                  quotechar='"',
                                  quoting=csv.QUOTE_ALL)
        for task in task_list:
            employee_csv.writerow(task)
