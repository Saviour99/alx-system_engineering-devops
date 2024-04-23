#!/usr/bin/env python3
# Python script that returns information using a REST API

import requests
import sys

# Dummy data representing employee information
employees_todo = {
    "1": {
        "EMPLOYEE_NAME": "Ervin Howell",
        "NUMBER_OF_DONE_TASKS": 6,
        "TOTAL_NUMBER_OF_TASKS": 20,
        "TASK_TITLE": "distinctio vitae autem"
    },
    "2": {
        "EMPLOYEE_NAME": "Patricia Lebsack",
        "NUMBER_OF_DONE_TASKS": 10,
        "TOTAL_NUMBER_OF_TASKS": 20,
        "TASK_TITLE": "odit optio omnis"
    }
}

def get_employee_todo_progress(employee_id):
    employee_data = employees_todo.get(employee_id)
    if employee_data:
        employee_name = employee_data.get('EMPLOYEE_NAME')
        num_done_tasks = employee_data.get('NUMBER_OF_DONE_TASKS')
        total_tasks = employee_data.get('TOTAL_NUMBER_OF_TASKS')
        task_title = employee_data.get('TASK_TITLE')
        print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
        print(f"\t{task_title}")
    else:
        print("Employee not found in the data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)

