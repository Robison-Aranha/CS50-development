n = ''
while (n.isnumeric() == False or int(n) < 1 or int(n) > 8):
    n = input("Hight: ")
n = int(n)
verificação = 0

for i in range(0, n):
    verificação += 1
    for j in range(n, verificação, -1):
        print(" ", end='')
    for c in range(0, verificação):
        print("#", end='')
    print("  " + "#" * verificação, end='')
    print("")