#!/usr/bin/python3
"""
Script that fetches info from API
"""
import requests
import sys
import csv


if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    users = '{}users/{}'.format(api_url, user_id)
    resp = requests.get(users)
    obj = resp.json()
    name = obj.get('name')

    todos = '{}todos?userId={}'.format(api_url, user_id)
    resp = requests.get(todos)
    tasks = resp.json()
    tasks_list = []
    for task in tasks:
        tasks_list.append([user_id,
            name,
            task.get('completed'),
            task.get('title')])

    file_name = '{}.csv'.format(user_id)
    with open(file_name, mode='w') as f:
        writer = csv.writer(f,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_ALL)
        for task in tasks_list:
            writer.writerow(task)
