'''
Exercise 2: Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire docu-
ment and count the total number of characters and display the count
of the number of characters at the end of the document.
'''

import socket

url = input("Enter a site: ")

try:
    urlSplit = url.split('/')
    host =  urlSplit[2]
except:
    print("Bad url")
    quit()

try:
    mysock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET '+url+' HTTP/1.0\r\n\r\n'
    mysock.send(cmd.encode())
except:
    print("Non exist url")
    quit()

di = dict()
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    line = data.decode()
    print(line,end='')
    words=line.split()
    for word in words:
        if count >= 3000:
            break
        count += 1
        di[word]=di.get(word,0) + 1

newlist = list()
for k,v in di.items():
    newtuple = (v,k)
    newlist.append(newtuple)

newlist.sort(reverse=True)

for v,k in newlist:
    print(v,k)