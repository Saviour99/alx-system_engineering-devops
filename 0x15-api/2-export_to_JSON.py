#!/usr/bin/python3
"""Python script that returns information using a REST API"""

import json
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

        data = {user_id: []}
        for todo in todos:
            task_title = todo.get("title")
            completed_status = todo.get("completed")

            task_data = {
                "task": task_title,
                "completed": completed_status,
                "username": emp_name
            }
            data[user_id].append(task_data)

        file_name = f"{user_id}.json"
        with open(file_name, "w") as file:
            json.dump(data, file)

    except requests.exceptions.RequestException as e:
        print("Error fetching data: ", e)
        sys.exit(1)
