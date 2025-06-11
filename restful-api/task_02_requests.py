#!/usr/bin/python3
import requests
import csv


"""Function to retrieve and display post titles"""


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    """Displays HTTP status code"""
    print(f"Status Code: {response.status_code}")

    """If the request is successful (code 200), the data is processed."""
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post.get("title"))


"""Function to retrieve posts and save them in a CSV file"""


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    """If the request is successful (code 200)"""
    if response.status_code == 200:
        data = response.json()

        """Definition of CSV file column names"""
        fieldnames = ["id", "title", "body"]

        """Writing data to the posts.csv file"""
        with open("posts.csv", "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in data:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })


"""Calls the two main functions if this file is run directly"""
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
