#!/usr/bin/python3
"""
    Api REST
"""

import requests
import sys


def get_employee(id=None):
    """
    Retrieve and display the TODO list progress for a given employee ID.
    """
    if id is None:
        if len(sys.argv) > 1:
            try:
                id = int(sys.argv[1])
            except ValueError:
                return
        else:
            return

    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{id}")
    todos_response = requests.get(f"{base_url}/todos/?userId={id}")

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data from the API")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [todo["title"] for todo in todos_data if todo["completed"]]

    print(f"Employee {user_data['name']} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

    for title in completed_tasks:
        print(f"\t{title}")


if __name__ == "__main__":
    get_employee()
