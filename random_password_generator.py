import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "1234567890"
symbols = "!?=#$%&*"

string = lower + upper + numbers + symbols
length = 7
password = "".join(random.sample(string, length))

print("Your password is", password)
