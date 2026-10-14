R = '\u001b[41m'
G = '\u001b[42m'
Y = '\u001b[43m'
Reset = '\u001b[0m'
def flag():
    pix='  '
    len=30
    height = 14
    for i in range(height):
        if i<height//2:
            print(G+pix*(len//3)+Y+pix*(len//3*2)+Reset)
        else:
            print(G+pix*(len//3)+R+pix*(len//3*2)+Reset)
flag()