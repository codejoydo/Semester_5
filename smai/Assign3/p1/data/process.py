with open('colon-cancer') as f:
    data = f.readlines()
data = [i.split() for i in data]
labels = [i[0] for i in data]
data = [i[1:] for i in data]
for i in range(len(data)):
    a = []
    for j in data[i]:
        a.append(j.split(':')[1])
    data[i] = a    
labelstr = '\n'.join(labels)
data = [' '.join(i) for i in data]
datastr = '\n'.join(data)
with open("colon_train.labels", "w") as f:
    f.write(labelstr)
with open("colon_train.data", "w") as f:
    f.write(datastr)