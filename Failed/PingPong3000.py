#!/usr/bin/env python
import socket
import re

s = socket.socket()
s.connect(('104.131.90.29', 8008))

If the integer is positive, remember it.
If the integer is 0, then print and forget the earliest number you remember.
Make sure to print a newline after every integer that you print.
If you try and print but the memory is empty, print 0.
Your code ends when -1 is inputted.

while True:
    data = s.recv(4096)
    if data != "":
        print("RECV>" + data)
        if 'Please give me the ' in data:
            regex = re.search(r"give me the '(.)' character '(.+)' times.+?'(.)'", data)
            ch = regex.group(1)
            numb = int(regex.group(2))
            returnString = ch*numb + regex.group(3);
            print returnString;
            s.send(returnString + "\n")
