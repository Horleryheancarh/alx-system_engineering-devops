#!/usr/bin/python3
"""
Script that fetches info from API
"""
import requests
import sys
import json


if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    url = '{}users/{}'.format(api_url, user_id)
    resp = requests.get(url)
    obj = resp.json()
    name = obj.get('username')

    todos = '{}todos?userId={}'.format(api_url, user_id)
    resp = requests.get(todos)
    tasks = resp.json()
    tasks_list = []
    for task in tasks:
        task_dict = {"task": task.get('title'),
                "completed": task.get('completed'),
                "username": name}
        tasks_list.append(task_dict)

    task_d = {str(user_id): tasks_list}
    file_name = '{}.json'.format(user_id)
    with open(file_name, mode='w') as f:
        json.dump(task_d, f)
