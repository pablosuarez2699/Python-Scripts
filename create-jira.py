import requests
import json

# Define the URL for creating a new issue
url = "https://pablosuarez2699.atlassian.net/rest/api/2/issue/"

# Define authentication credentials
auth = ("pablosuarez2699@gmail.com", "API_TOKEN_KEY")

# Define request headers
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# Define the payload (issue data)
payload = json.dumps( {
  "fields": {
    "summary": "Main order flow broken",
    "description": "Order entry fails when selecting supplier.",
    "issuetype": {
      "id": "10001"
    },
    "project": {
      "id": "10000"
    }
  },
  "update": {}
} )

# Send a POST request to create the issue
response = requests.post(url, data=payload, headers=headers, auth=auth)

# Print the response
print(json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": ")))
