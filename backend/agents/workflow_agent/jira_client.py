import requests
from requests.auth import HTTPBasicAuth

from config.settings import (
    ATLASSIAN_API_TOKEN,
    ATLASSIAN_USERNAME,
    ATLASSIAN_DOMAIN,
)

PROJECT_KEY = "WA"

all_issues = []

response = requests.get(
    f"https://{ATLASSIAN_DOMAIN}/rest/api/3/search/jql",
    auth=HTTPBasicAuth(ATLASSIAN_USERNAME, ATLASSIAN_API_TOKEN),
    headers={"Accept": "application/json"},
    params={
        "jql": f"project = {PROJECT_KEY} ORDER BY created DESC",
    }
)
data = response.json()
issue = data['issues'][0]['id']

url = f"https://{ATLASSIAN_DOMAIN}/rest/api/3/issue/{issue}"
response = requests.get(
    url,
    auth=HTTPBasicAuth(ATLASSIAN_USERNAME, ATLASSIAN_API_TOKEN),
    headers={"Accept": "application/json"},
)

data = response.json()
title = data['fields']['summary']
description = data['fields']['description']['content'][0]['content'][0]['text']
print(title)
print(description)