import os
test = os.popen('python3 wordfreq.py < test.txt').read().split()
total = 0
odd = 0
new = []
for y in test:
    if y.isnumeric():
        total += int(y)
for x in range(len(test)):
    # print(x)
    if test[x].isnumeric():
        new.append(("*"*(int(test[x]) * 2)))
        new.append(int((int(test[x])/total)*100))

while odd != len(test):
    print(f"{test[odd]}              [{new[odd]}] {new[odd+1]}%")
    odd+=2


