B = '\u001b[0m'
Y = '\u001b[43m'
Reset = '\u001b[0m'
for i in range(9):
    y = 9 - i 
    print(str(y) + " ", end = "")
    for j in range(10):
        x = j + 1
        if y == x + 1:
            print(Y+"   "+ Reset, end = "")
        else:
            print(B+"   "+ Reset, end = "")
    print('')
print('0  1  2  3  4  5  6  7  8  9')