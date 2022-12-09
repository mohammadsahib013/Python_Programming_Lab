fname = open("Text.rtf", 'w+')
print("Enter three lines")
i = 1
while i <= 3:
    data = input()
    fname.write(f"{data}\n")
    i += 1
fname = open("Text.rtf")
data = fname.read()
print(data)
fname.close() 
