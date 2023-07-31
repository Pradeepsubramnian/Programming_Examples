para = []
print("Enter a Para: ")

while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
print(para)
output = '\n'.join(para)
print(output)

