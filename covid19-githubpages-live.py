#!/usr/bin/python3

from requests_html import HTMLSession
from github import Github
import pickle

def update_cases():
    session = HTMLSession()
    data = session.get("https://www.worldometers.info/coronavirus/")

    cases = data.html.find("div[class='maincounter-number'] span")

    total = cases[0].text
    deaths = cases[1].text
    recovered = cases[2].text

    template = """
    <h1>covid19-scrapper</h1>
    <h1>Total Cases: {0}</h1>
    <h1>Deaths: {1}</h1>
    <h1>Recovered: {2}</h1>
    <a href="mailto:vivekascoder@gmail.com">Mail to admin.</a>
    """.format(total, deaths, recovered)

    # Lets Work on web part i.e github API
    with open("credentials.cred", "rb") as file:
        data = pickle.load(file)
        username, password = data['username'], data['password']

    git = Github(username, password)
    user = git.get_user()

    repo = user.get_repo('covid')
    content = repo.get_contents("index.html")
    repo.update_file(content.path, "Updated!", template, content.sha, branch='master')


