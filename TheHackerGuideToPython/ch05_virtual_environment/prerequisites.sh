!/bin/bash
sudo pip install virtualenv
virtualenv myenv
source myenv/bin/active
sudo pip install six
sudo pip -r installrequirements.txt
deactive

# using virtualenv python directly
myenv/bin/python hello.py


