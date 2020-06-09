'''
f = open('dic.txt', "r")
words=[]
lines = sorted(f.readlines())
'''
with open('dic.txt', 'r') as r:
    for line in sorted(r):
        print(line, end='')