#!/usr/bin/python3
"""Python script that returns information using a REST API"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users/{user_id}"
    todos_url = f"{users_url}/todos"

    try:
        response = requests.get(users_url).json()
        emp_name = response.get('name')

        todos = requests.get(todos_url).json()

        csv_filename = f"{user_id}.csv"

        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for todo in todos:
                emp = "'{}'".format(str(emp_name))
                user = "'{}'".format(str(user_id))
                completed_status = "'{}'".format(str(todo['completed']))
                task_title = "'{}'".format(str(todo['title']))

                writer.writerow([user, emp, completed_status, task_title])

    except requests.exceptions.RequestException as e:
        print("Error fetching data: ", e)
        sys.exit(1)
