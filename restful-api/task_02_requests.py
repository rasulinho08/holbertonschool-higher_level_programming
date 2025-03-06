# task_02_requests.py
import requests
import csv

# Function to fetch posts and print the titles
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the JSON response
        posts = response.json()

        # Iterate through the posts and print the title of each post
        for post in posts:
            print(post['title'])

# Function to fetch posts and save them to a CSV file
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        posts = response.json()

        # Prepare the data in the required format (list of dictionaries)
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Write the data into a CSV file
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)

        print("Posts have been saved to posts.csv")

