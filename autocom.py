import os
import time
from github import Github

TOKEN_FILE = 'token.txt'

def get_github_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as file:
            return file.read().strip()
    else:
        token = input("Enter your GitHub token: ")
        with open(TOKEN_FILE, 'w') as file:
            file.write(token)
        return token


g = Github(get_github_token())


repo = g.get_user().get_repo("prv")

def commit_file():
    filename = f"commit_{int(time.time())}.txt"
    with open(filename, 'w') as file:
        file.write("Auto commit")
    repo.create_file(filename, "auto commit", "", branch="master")
    print(f"Committed file {filename}")
    os.remove(filename)

for i in range(6):
    
    commit_file()
    time.sleep(10)
    i+=1