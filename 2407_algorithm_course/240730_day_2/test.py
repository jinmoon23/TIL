data = [0,4,1,3,1,2,4,1]
counts = [] * (max(data))
for i in range(len(data)):
    counts[data[i]] += 1
print(counts)