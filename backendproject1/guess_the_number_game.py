import sys
import random

sys.stdout.buffer.write(b'Input Minimum number: ')
sys.stdout.flush()
min = sys.stdin.buffer.readline()
sys.stdout.buffer.write(b'Input Max number: ')
sys.stdout.flush()
max = sys.stdin.buffer.readline()

min = int(min.decode())
max = int(max.decode())

if min > max:
    temp = max
    max = min
    min = temp

randomNum = random.randint(min, max)

sys.stdout.buffer.write(b'Guess the number: ')
sys.stdout.flush()
userAnser = sys.stdin.buffer.readline()
userAnser = int(userAnser.decode())

while randomNum != userAnser:
    print("Try again: ")
    sys.stdout.buffer.write(b'Guess the number: ')
    sys.stdout.flush()
    userAnser = sys.stdin.buffer.readline()
    userAnser = int(userAnser.decode())


print("Congratulation that is answer!")