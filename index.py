import datetime

print("hello world.")
print("good")

with open("log.txt", "a") as f:
    f.write(f"Job ran at: {datetime.datetime.now()}\n")
