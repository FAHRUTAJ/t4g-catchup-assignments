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