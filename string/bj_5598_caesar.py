original = "".join([chr((ord(w)-65-3)%26 + 65) for w in input()])
print(original)