#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    # Check for employee ID as command-line argument
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_ID = sys.argv[1]
    jsonplaceholder = 'https://jsonplaceholder.typicode.com'
    users_endpoint = '/users'
    url = f'{jsonplaceholder}{users_endpoint}/{employee_ID}'
    todo_endpoint = '/todos?userID={employee_ID}'
    todo_url = f'{url}{todo_endpoint}'

    # Make a GET request to API
    response_url = requests.get(url)
    response_todo_url = requests.get(todo_url)

    # Check if the request was successful (status code 200)
    if response_url.status_code == 200\
            and response_todo_url.status_code == 200:
        user_data = response_url.json()
        todo_data = response_todo_url.json()

        complete_tasks = [task for task in todo_data if task.get('completed')]
        employee_name = user_data.get('name')

        # Retrieve tasks
        print("Employee {} is done with tasks({}/{})):".format(
            employee_name, len(complete_tasks), len(todo_data)))
        for task in complete_tasks:
            print("\t{}".format(task.get('title')))
    # Error message if request was unsuccessful
    else:
        print(f"Error: Unable to fetch data.\
            Status code: {response_url.status_code}")
