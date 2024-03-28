Python Network Scripting Exercises

This repository contains a set of Python scripts that demonstrate various network scripting tasks using different libraries and APIs. Each script is designed to accomplish a specific task related to HTTP requests, API interactions, and network communication.

List of Scripts:

What's my status? #0 (0-hbtn_status.py):

Fetches the status of a given URL using the urllib package.
Displays the body of the response along with information about its type and content.

Response header value #0 (1-hbtn_header.py):

Takes a URL as input, sends a request, and displays the value of the X-Request-Id header in the response using the urllib package.

POST an email #0 (2-post_email.py):

Sends a POST request to a URL with an email parameter using the urllib package.
Displays the body of the response, decoding it in utf-8.

Error code #0 (3-error_code.py):

Takes a URL as input, sends a request, and displays the body of the response.
Manages urllib.error.HTTPError exceptions and prints the HTTP status code in case of an error.

What's my status? #1 (4-hbtn_status.py):

Fetches the status of a given URL using the requests package.
Displays the body of the response along with information about its type and content.

Response header value #1 (5-hbtn_header.py):

Takes a URL as input, sends a request, and displays the value of the X-Request-Id header in the response using the requests package.

POST an email #1 (6-post_email.py):

Takes a URL and an email address as input.
Sends a POST request to the URL with the email as a parameter using the requests package.
Displays the body of the response.

Error code #1 (7-error_code.py):

Takes a URL as input, sends a request, and displays the body of the response.
Prints the error code followed by the value of the HTTP status code if the status code is greater than or equal to 400.

Search API (8-json_api.py):

Takes a letter as input and sends a POST request to a URL with the letter as a parameter using the requests package.
Displays the id and name if the response body is properly JSON formatted and not empty.
Displays appropriate messages if the JSON is invalid or empty.

My GitHub! (10-my_github.py):

Takes GitHub credentials (username and password) as input.
Uses the GitHub API to display the user's id.
Implements Basic Authentication with a personal access token as the password.

Time for an interview! (100-github_commits.py):

Lists 10 commits (from the most recent to oldest) of a specified repository by a given user.
Uses the GitHub API to fetch the commit information.i
