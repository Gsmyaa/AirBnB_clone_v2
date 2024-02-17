
# AirBnB clone - The console


The AirBnB console aims to develop a minishell capable of functioning in both interactive and non-interactive modes. Essentially, this project serves as a fundamental replica of AirBnB, 

# command interpreter or console
The initial task involves working with a robust storage system. This storage engine serves as an intermediary between "My object" and its storage and persistence methods. 
#  how to start it:
To initiate the console, utilize the following command: ./console.py

# How to used:
- Perform object management tasks such as creation, updating, and deletion through a console or command interpreter.
- Save and retain objects to a file, specifically a JSON file.
- Available commands: create, show, destroy, all (displays all), update, help, quit.
### Example how to open:
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
