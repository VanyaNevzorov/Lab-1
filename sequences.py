R = '\u001b[41m'
G = '\u001b[42m'
Y = '\u001b[43m'
Reset = '\u001b[0m'
def sequence():
    file = [float(i) for i in open('sequence.txt').readlines()]
    a1,a2,a3=[],[],[]
    for i in file:
        if 0<=i<=5:
            a1.append(i)
        if -5<=i<=0:
            a2.append(i)
        if i<-5 or i>5:
            a3.append(i)
    sm=len(a1)+len(a2)+len(a3)
    print("[0;5] "+R+" "*(int((len(a1)/sm)*100))+Reset+str(float(len(a1)/sm)*100)+"%")    
    print("[-5;0]"+G+" "*(int((len(a2)/sm)*100))+Reset+str(float(len(a2)/sm)*100)+"%") 
    print("Rest  "+Y+" "*(int((len(a3)/sm)*100))+Reset+str(float(len(a3)/sm)*100)+"%")     
sequence()