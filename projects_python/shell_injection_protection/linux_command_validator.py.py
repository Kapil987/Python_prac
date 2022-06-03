
import subprocess
import os
import re
import sys

# Get a list of valid commands
def valid_commands_fun():
    global command
    command = []
    with open('valid_commands.txt', 'r') as f:
        temp = f.readlines()  # has the list with elements having \n
        for items in temp:
            command.append(items.strip('\n'))

# Getting protected from shell injection
def check_commands(validate):
    global check
    check = []
    with open('wild_commands.txt', 'r') as f:
        temp = f.readlines()  # has the list with elements having \n
        for items in temp:
            check.append(items.strip('\n'))

    # txt = fr"{validate}"
    for index, items in enumerate(check):
        x = re.search(items, validate)
        if x is not None:
            print('Please enter a check command not this:: ', validate)
            sys.exit("Invalid Input")


valid_commands_fun()

for i in command:
    # print(i)
    check_commands(i)
    print('Starting************* for', i, '\n\n')
    res = subprocess.Popen(i, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, universal_newlines=True)

    abc = res.stdout.read()
    print(f'stdout for *******{i} is:: \n\n', abc)
    print(f'sterr for *******{i} is:: \n', res.stderr.read())
    """
        res = subprocess.Popen(i, shell=True)
        res.wait()
        if res.returncode == 0:
                print('********success for ',i)
        """

# Notes
# a) if res = subprocess.Popen(items, shell=True) is used then res.wait() is used else
# it will slightly hung up
#
# b) if res = subprocess.Popen(items, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) is
# used then no need to use res.wait(), also now the output will not be displayed on command line
# it will get stored in res.stdout.read()
#
# c) for reading stdout you can use res.stdout.read()
# d) use universal_newlines=True to decode the output into text form
