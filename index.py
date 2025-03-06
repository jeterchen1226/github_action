import datetime

print("hello world.")

with open("log.txt", "a") as f:
    f.write(f"Job ran at: {datetime.datetime.now()}\n")
    