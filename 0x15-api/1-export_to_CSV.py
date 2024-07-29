#!/usr/bin/python3
"""export data in the CSV format"""

import csv
from urllib import request
from sys import argv
from requests import *


if __name__ == "__main__":
    """export data in the CSV format"""
    # Retrieves the user ID from the first command-line argument
    user_id = argv[1]

    # send a request to retrieve user id
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    # store the response from the api in response variable
    response = get(url)

    # extract users username from response
    username = response.json().get("username")

    # send a request to retrieve user's todo list
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)

    # store the response from the api in response variable
    response = get(url)

    # extract todo list from response
    todo_list = response.json()

    # open a csv file for writing
    with open("{}.csv".format(user_id), "w") as file:
        # create a writer object
        for task in todo_list:
            # write the username, user id, task completed status, task title
            file.write('"{}","{}","{}","{}"\n'.format(
                user_id, username, task.get("completed"), task.get("title")))
