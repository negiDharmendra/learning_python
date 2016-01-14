

f = open('basic_learning.py', 'r') # by default the mode is read-only
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line), # note the comma to avoid automatic new line
f.close()