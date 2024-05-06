#!/usr/bin/python3
"""Python script that returns information using a REST API"""

import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    try:
        users = requests.get(users_url).json()
        todos = requests.get(todos_url).json()

        data = {}

        for user in users:
            user_id = user["id"]
            emp_name = user["name"]

            user_todos = [
                {
                    "username": emp_name,
                    "task": todo["title"],
                    "completed": todo["completed"],
                }
                for todo in todos
                if todo["userId"] == user_id
            ]

            data[str(user_id)] = user_todos

        file_name = "todo_all_employees.json"
        with open(file_name, "w") as file:
            json.dump(data, file)

    except requests.exceptions.RequestException as e:
        print("Error fetching data: ", e)
        sys.exit(1)
