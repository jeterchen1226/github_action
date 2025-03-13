import datetime

def index(a, b):
    return a + b
index(10, 2)

with open("log.txt", "a") as f:
    f.write(f"Job ran at: {datetime.datetime.now()}\n")
