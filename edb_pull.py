#!/usr/bin/python
# Download all public exploits available in the exploit database with the string you designate in the name. Results can probably be narrowed further  

import os
import subprocess 

# Create directory and store its name in dir; create file named "str"_exploits, iterate through exploits and download to working directory

print('Creating directory to store exploits...\n')
dir = raw_input("Name of the directory to create and store exploits: ")
str = raw_input("String to grep from e-db: ")

# Creates directory, moves into directory, searches exploit-db, filters output to grab the numerical value of the exploit to use as input for searchsploit command
cmd = 'mkdir ~/' + dir + ' && cd ~/' + dir + ' && searchsploit ' + str + ' | grep "' + str + '" | cut -d "|" -f 2 | cut -d "/" -f 3 | cut -d "." -f 1 > ' + str + '_exploits'
returned_value = subprocess.call(cmd, shell=True)

# Opens newly created file and stores each line as value in a list 
with open('/root/' + dir + "/" + str + '_exploits') as f:
    lines = [line.rstrip() for line in f]

# Move the programs working directory to the directory created 
os.chdir('/root/' + dir)

# Create the reference file
ref = 'searchsploit ' + str + ' > reference_file.txt'
subprocess.call(ref, shell=True)

# Iterate through the grepped data and perform designated command on items in list; I.E. "searchsploit -m 12345"
print('Downloading exploits...')

for ex in lines:
    cmd1 = '/usr/bin/searchsploit -m ' + ex + ' 1>/dev/null'
    returned_value1 = subprocess.call(cmd1, shell=True)

# Remove previously created file	
cmd2 = 'rm /root/' + dir + '/' + str + '_exploits'
returned_value2 = subprocess.call(cmd2, shell=True)


