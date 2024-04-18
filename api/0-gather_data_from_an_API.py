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
    if len(sys.argv) > 1:
        try:
            id = int(sys.argv[1])
        except ValueError:
            return

    if isinstance(id, int):
        base = "https://jsonplaceholder.typicode.com"
        user = requests.get(f"{base}/users/{id}").json()
        to_dos = requests.get(f"{base}/todos/?userId={id}").json()

        if user and to_dos:
            total_tasks = len(to_dos)

            titles_completed = [task["title"]
                                for task in to_dos
                                if task["completed"]]

            tasks_completed = len(titles_completed)

            print(f"Employee {user['name']} is done with tasks\
                    ({len(tasks_completed)}/{total_tasks}):")

            for title in titles_completed:
                print(f"\t {title}")


if __name__ == "__main__":
    get_employee()
