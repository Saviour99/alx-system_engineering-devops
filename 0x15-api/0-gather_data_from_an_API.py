#!/usr/bin/python3
"""Python script that returns information using a REST API"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users/{user_id}"
    todos_url = f"{users_url}/todos"

    response = requests.get(users_url).json()
    emp_name = response.get("name")

    todos = requests.get(todos_url).json()
    count = 0

    for todo in todos:
        if todo.get("completed"):
            count += 1

    total_todos = len(todos)

    print("Employee {emp_name} is done with tasks"
          + "({count}/{total_todos}): ")
    for todo in todos:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")
