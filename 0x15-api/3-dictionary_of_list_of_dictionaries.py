#!/usr/bin/python3
"""
Script that fetches info from API
"""
import requests
import sys
import json


if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'

    url = '{}users'.format(api_url)
    resp = requests.get(url)
    users = resp.json()
    task_dict = {}

    for user in users:
        name = user.get('username')
        user_id = user.get('id')
        todos = '{}todos?userId={}'.format(api_url, user_id)
        resp = requests.get(todos)
        tasks = resp.json()
        tasks_list = []
        for task in tasks:
            task_dict = {"username": name,
                    "task": task.get('title'),
                    "completed": task.get('completed')}
            tasks_list.append(task_dict)

        task_dict[str(user_id)] = tasks_list
    file_name = 'todo_all_employees.json'
    with open(file_name, mode='w') as f:
        json.dump(task_dict, f)
