import random

if __name__ == '__main__':
    f = open("poem.txt", 'r')
    poem = f.readlines()

print()
for i in range(len(poem), 0, -1):
    index = str(i)
    line = poem[i-1]
    print(index + ":" + line)

print()
lines = [ line for line in poem ]
random.shuffle(lines)
for line in lines:
    print(line)
