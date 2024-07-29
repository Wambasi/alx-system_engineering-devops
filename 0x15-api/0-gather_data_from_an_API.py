#!/usr/bin/python3

"""
Gather data from an API
for a given employee ID, returns information about his/her
todo list progress.
"""


import requests
import sys


if __name__ == "__main__":
    """Gather data from an API"""

    # define the base url of rest api
    url = "https://jsonplaceholder.typicode.com"

    # send get request to api to get user info in dict format
    user = requests.get(url + "/users/" + sys.argv[1]).json()

    # send get request to api to get todo info in dict format
    todo = requests.get(url + "/todos?userId=" + sys.argv[1]).json()

    # get the number of completed tasks
    completed_tasks = [task for task in todo if task.get("completed") is True]

    # print the result, employee's name, completed tasks & total no of tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todo)))

    # print the title of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
