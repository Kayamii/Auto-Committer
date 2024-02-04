# main.py
import os
import time
from github import Github
from kivy.app import App
from kivy.uix.button import Button

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

class GitHubCommitApp(App):

    def build(self):
        button = Button(text='Commit File', on_press=self.commit_file)
        return button

    def commit_file(self, *args):
        g = Github(get_github_token())
        repo = g.get_user().get_repo("prv")

        filename = f"commit_{int(time.time())}.txt"
        with open(filename, 'w') as file:
            file.write("Auto commit")
        repo.create_file(filename, "auto commit", "", branch="master")
        print(f"Committed file {filename}")
        os.remove(filename)

if __name__ == '__main__':
    GitHubCommitApp().run()
