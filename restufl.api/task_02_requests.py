#!/usr/bin/python3
import requests
import csv

"""
This module provides functions to interact with a REST API and process the data.

Functions:
    fetch_and_print_posts():
        Fetches posts from a REST API and prints their titles.

    fetch_and_save_posts():
        Fetches posts from a REST API, filters the data, and saves it to a CSV file.
"""


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    if response.ok:
        result = response.json()
        for post in result:
            print(post["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.ok:
        result = response.json()
        filtered_posts = []
        for post in result:
            new_post = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            filtered_posts.append(new_post)
            with open("posts.csv", "w+") as file:
                writer = csv.DictWriter(
                    file, fieldnames=["id", "title", "body"])
                writer.writeheader()
                writer.writerows(filtered_posts)
