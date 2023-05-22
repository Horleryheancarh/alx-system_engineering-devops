#!/usr/bin/python3
"""
Script that fetches info from API
"""
import requests
import sys

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'

    users = '{}users/{}'.format(api_url, sys.argv[1])
    resp = requests.get(users)
    obj = resp.json()
    print("Employee {} is done with tasks".format(obj.get('name')), end="")

    todos = '{}todos?userId={}'.format(api_url, sys.argv[1])
    resp = requests.get(todos)
    tasks = resp.json()
    tasks_list = []
    for task in tasks:
        if task.get('completed') is True:
            tasks_list.append(task)

    print("({}/{}):".format(len(tasks_list), len(tasks)))
    for task in tasks_list:
        print("\t {}".format(task.get('title')))
