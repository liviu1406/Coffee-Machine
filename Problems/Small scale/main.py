fl = []

while True:
    n = input()
    if n == ".":
        break
    fl.append(float(n))

print(min(fl))
