# PyGithub -> github
from github import Github
import pickle

with open('credentials.dat', 'rb') as file:
    data = pickle.load(file)
    username, password = data['username'], data['password']

git = Github(username, password)
user = git.get_user()

# It's time to create a file, ...
repo = user.get_repo('botRepo')
repo.create_file(path="readme.md", message="Created by BOT. ", content="Hello World", branch="master")
print("File Created Successfully~!!")
