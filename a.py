R = '\u001b[41m'
Reset = '\u001b[0m'
def pattern():
    h=7
    center=(h+1)//2-1
    offset=(h-3)//2
    clset=3
    for i in range(5):
        for line in range(1,h):
            if offset!=0:
                print(Reset+'  '*offset+R+'  '*clset+Reset+'  '*(offset*2-1)+R+'  '*clset+Reset+' '*offset)
            else:  
                print(Reset+'  '*offset+R+'  '*clset+Reset+'  '*(offset*2-1)+R+'  '*(clset-1)+Reset+' '*offset)
            if line<center:
                offset-=1
                clset+=2
            else:
                offset+=1
                clset-=2
        offset=(h-3)//2
        clset=3
pattern()