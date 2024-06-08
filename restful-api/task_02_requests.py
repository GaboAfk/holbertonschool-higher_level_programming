#!/usr/bin/python3
"""requests module
"""
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for post in response.json():
            print(post["title"])
    else:
        print("Error obtaining POSTS")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        j_list = []
        for post in response.json():
            j_list.append({"id": post["id"],
                           "title": post["title"],
                           "body": post["body"]})
        filename = "posts.csv"
        with open(filename, 'w', newline='') as csvfile:
            fields = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            writer.writeheader()
            writer.writerows(j_list)

            """for post in j_list:
                row = {"id": post["id"],
                       "title": post["title"],
                       "body": post["body"]}
                writer.writerow(row)"""

        print("Data saved in posts.csv")
    else:
        print("Error obtaining POSTS")
