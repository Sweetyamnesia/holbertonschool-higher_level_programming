#!/usr/bin/python3
import requests
import json
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts", data={"key": "value"})
    print(response.status_code == 200)

def fetch_and_save_posts():
    fields = ["id", "title", "body"]
    with open("posts.csv", "w", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
