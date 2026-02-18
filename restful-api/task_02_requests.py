#!/usr/bin/python3

"""
This module provides functions to interact with a REST API and
process the data.

Functions:
    fetch_and_print_posts():
        Fetches posts from a REST API and prints their titles.

    fetch_and_save_posts():
        Fetches posts from a REST API, filters the data, and saves
        it to a CSV file.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from a REST API and prints their titles.

    This function sends a GET request to the JSONPlaceholder API to retrieve
    a list of posts. It then prints the title of each post to the console.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
    except requests.RequestException:
        return

    print(f"Status Code: {response.status_code}")
    if response.ok:
        try:
            result = response.json()
        except ValueError:
            return
        for post in result:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts from a REST API, filters the data, and saves
    it to a CSV file.

    This function sends a GET request to the JSONPlaceholder API to
    a list of posts. It filters the data to include only the post ID, title,
    and body, and writes the filtered data to a CSV file named 'posts.csv'.

    Returns:
        None
    """
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
    except requests.RequestException:
        return
    if response.ok:
        try:
            result = response.json()
        except ValueError:
            return
        filtered_posts = []
        for post in result:
            new_post = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            filtered_posts.append(new_post)
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)
