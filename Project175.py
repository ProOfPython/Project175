import matplotlib.pyplot as plt
import psutil as p

names = []
percents = []
exNames = []
exPercents = []
count = 0

for process in p.process_iter():
    count += 1
    if count <= 6:
        name = process.name()
        usage = p.cpu_percent()
        print(str(name) + ', ' + str(usage))
        names.append(name)
        percents.append(usage)

exNames.append(min(names))
exNames.append(max(names))
exPercents.append(min(percents))
exPercents.append(max(percents))

plt.figure(figsize = (15, 7))
plt.xlabel('App')
plt.ylabel('Usage')
plt.bar(exNames, exPercents, width = 0.6, color = ('blue', 'orange', 'pink'))
plt.show()