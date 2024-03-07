#!/usr/bin/env python3
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
    jsonplaceholder = 'https://jsonplaceholder.typicode.com/employee'
    url = f'{jsonplaceholder}/employee/{employee_ID}'

    # Make a GET request to API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        employee_name = response.json().get('name')
        todo_url = f'{url}/todo'
        retrieve_todo = request.get(todo_url)
        tasks = retrieve_todo.json()

        # Retrieve tasks
        complete_tasks = [task for taks in tasks if task.get('complete')]
        print("Employee {} is done with tasks({}/{})):".format(employee_name,
            len(complete_tasks), len(tasks)))
        for task in complete_tasks:
            print("\t{}".format(task.get('title')))
    # Error message if request was unsuccessful
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
