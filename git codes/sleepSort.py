import time
sorted = []

def sleepSort(list):
    for i in range(max(list)+1):
        time.sleep(i)
        if i in list:
            sorted.append(i)
    return sorted


listen = []
listed = input('Enter a couple of numbers separated by space: ')
lister = listed.split()
for i in lister:
   listen.append(int(i))
        
        
print(sleepSort(listen))