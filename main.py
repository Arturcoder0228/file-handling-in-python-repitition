with open("pi.text") as file:
    pi = file.read()

pi = pi.rstrip()
pi = pi.replace("\n", "")


print(pi)

