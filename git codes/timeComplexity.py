import time

time_array = []
times_run = 50


for _ in range(times_run):
    start = time.time()
    total = 0
    for i in range(1000):
        total += i
    stop = time.time()
    time_taken = (stop-start)/(times_run)
    time_array.append(time_taken)

sum = 0
for t in time_array:
    sum += t
average = sum/times_run

print(total)
print(average)