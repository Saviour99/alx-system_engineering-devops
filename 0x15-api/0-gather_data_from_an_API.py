#!/usr/bin/python3
"""Python script that returns information using a REST API"""

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
        count = 0

        for todo in todos:
            if todo.get("completed"):
                count += 1

        total_todos = len(todos)

        emp_name_adjusted = f"{emp_name[:18]:<18}"

        print("Employee {emp_name_adjusted} is done with tasks"
              + "({count:02d}/{total_todos}): ")
        for todo in todos:
            if todo.get("completed"):
                print(f"\t {todo.get('title')}")

    except requests.exceptions.RequestException as e:
        print("Error fetching data: ", e)
        sys.exit(1)
