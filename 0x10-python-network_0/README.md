ALX Higher Level Programming - 0x10. Python - Network #0

This repository contains tasks related to basic networking concepts using the curl command in Bash.
Tasks
0. cURL body size

Filename: 0-body_size.sh

Description: A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

Usage:

sh

./0-body_size.sh <URL>

Example:

sh

guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$

1. cURL to the end

Filename: 1-body.sh

Description: A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response only if the status code is 200.

Usage:

sh

./1-body.sh <URL>

Example:

sh

guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$

2. cURL Method

Filename: 2-delete.sh

Description: A Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

Usage:

sh

./2-delete.sh <URL>

Example:

sh

guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$

3. cURL only methods

Filename: 3-methods.sh

Description: A Bash script that takes in a URL and displays all HTTP methods the server will accept.

Usage:

sh

./3-methods.sh <URL>

Example:

sh

guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$

4. cURL headers

Filename: 4-header.sh

Description: A Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable X-School-User-Id must be sent with the value 98.

Usage:

sh

./4-header.sh <URL>

Example:

sh

guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$

5. cURL POST parameters

Filename: 5-post_params.sh

Description: A Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable email must be sent with the value test@gmail.com and a variable subject must be sent with the value I will always be here for PLD.

Usage:

sh

./5-post_params.sh <URL>

Example:

sh

guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$

6. Find a peak

Filename: 6-peak.py, 6-peak.txt

Description: Write a function that finds a peak in a list of unsorted integers.

Prototype:

python

def find_peak(list_of_integers):

Requirements:

    You are not allowed to import any module
    Your algorithm must have the lowest complexity

Example:

sh

guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$

7. Only status code

Filename: 100-status_code.sh

Description: Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response. You are not allowed to use any pipe, redirection, etc.

Usage:

sh

./100-status_code.sh <URL>

Example:

sh

guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
guillaume@ubuntu:~/0x10$
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
guillaume@ubuntu:~/0x10$

8. cURL a JSON file

Filename: 101-post_json.sh

Description: Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request.

Usage:

sh

./101-post_json.sh <URL> <filename>

Example:

sh

guillaume@ubuntu:~/0x10$ cat my_json_0
{
    "name": "John Doe",
    "age": 33
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON
guillaume@ubuntu:~/0x10$
guillaume@ubuntu:~/0x10$ cat my_json_1
I'm a JSON! really!
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$
guillaume@ubuntu:~/0x10$ cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$

9. Catch me if you can!

Filename: 102-catch_me.sh

Description: Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

Usage:

sh

./102-catch_me.sh

Example:

sh

guillaume@ubuntu:~/0x10$ ./102-catch_me.sh ; echo ""
You got me!
guillaume@ubuntu:~/0x10$

Repository

    GitHub repository: alx-higher_level_programming
    Directory: 0x10-python-network_0

Make sure you test each script in the provided sandbox environment using the web server running on port 5000.

