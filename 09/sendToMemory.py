#TODO: dict, ktery ma keys INT a chova se jako dynamicky list¨

memory = {}

def sendToMemory(adress, value):
    if adress in memory.keys():
        memory[adress] = value
    else:
        memory.setdefault(adress, value)

for i in range(10):
    sendToMemory(i%5, i+1)

print(memory)