# Assignment 2
## Part 1- Users and Groups
Two users were created:
dev_alice and dev_bob
#Commmands used to add users:
sudo adduser [username]
#This command gives you the right to add some features to the user you are creating.
## Creating group 
The backend_team was created using :
sudo groupadd backend_team

Both users were added using 
sudo usermod -aG backend_team [username]

# The etc command explanation
command used:
cat /etc/passwd

UID->the users id number
GID->the users group id
comments
home_directory-> users home folder
shell->Default login shell



## Part 2
## File Permissions
## Permission set using:
chmod 600 project_config.txt

Meaning:
-Owner->read and writes only
-Group->has no access
-Others->has no access


### Permission set for shared_docs Directory
chmod 750 shared_docs
Meaning:
-Owner->full access to read,write and execute
-Group->write and execute
-Others-> has no access

SGIDensures files created inside inherit the group ownership.


## runner.sh
shebang added
#!/bin/bash
Execute permission added using:
chmod u+x runner.sh
which gave permission to only the user to execute. 
