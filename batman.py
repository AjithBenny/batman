
n=int(input("Enter the number of Patients Escaped : "))
x=int(input("What step of the first patient Batman started : "))
def BatMan(n,x):
    step=0
    for i in range (n,0,-1):
        i=(i*x)*2
        step=step+i
    print("Batman took total of ",step,"steps")
BatMan(n,x)
