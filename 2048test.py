# 2048 game
#by yzy,ssm,lxr
#ssm:throw out the idea(the first "up" iterator ) and finally complete(including the code comments)
#yzy:debug and improve(add reverse,[[]*n for...] as well as extend the iterator)//for his great ideas to steal :)
#lxr:first finish one usable edition(This is not his version,if you want to see his version with gui,please contact him)
from random import*
print ("This is a simple 2048 game")
print ("You can use the following keys to control the direction")
print ("0: right")
print ("1: left")
print ("2: up")
print ("3: down")
print ("w: up")
print ("a: left")
print ("s: down")
print ("d: right")
print ("other keys: exit the game")
n=int(input("size="))
a=[[0]*n for i in range(n)]
dmap={"0":0,"1":1,"2":2,"3":3,"d":0,"a":1,"w":2,"s":3} # map the direction
def move(d):#d:direction
    def r():#r:reverse
        if d==0:
            for i in range(n):
                a[i].reverse()
        elif d==3:
            a.reverse()
    i,j,f={0:(0,1,[0,0]),1:(1,0,[0,0])}[d//2]
    #left/right: [0] i=0,j=1
    #up/down:    [1] i=1,j=0
    r()
    for f[i] in range(n):#wonderful iterator!
        for f[j] in range(n):
           x,y=f[0],f[1]
           if a[x][y]==0:
               continue
           dx,dy=x-i,y-j
           while dx*i+dy*j>=0:
               if a[x][y]==a[dx][dy]:#merge
                   a[dx][dy]*=-2
                   a[x][y]=0
                   break
               elif a[dx][dy]!=0:#There is a block
                   break
               dx-=i
               dy-=j
        
        num=[x,y]#the number of non-zero elements
        num[j]=0
        for f[j] in range(n):
            x,y=f[0],f[1]
            if a[x][y]!=0:
                a[num[0]][num[1]]=abs(a[x][y])
                if num[j]!=f[j]:
                    a[x][y]=0
                num[j]+=1
        #move the non-zero elements
    r()

step=0#how many steps you have taken
while True:
    step+=1
    print("Your step is ",step)
    rx=randint(0,n-1)
    ry=randint(0,n-1)
    while(a[rx][ry]!=0):
        rx=randint(0,n-1)
        ry=randint(0,n-1)
    a[rx][ry]=randint(1,2)*2

    for i in range(n):
        print(a[i])
    
    d=input("direction=") # 0=right,1=left,2=up,3=down
    if not d in ["0","1","2","3","w","a","s","d"]:
        print("Exit")
        break
    d=dmap[d]
    move(d)

    for i in range(n):
        print(a[i])
    print("score=",sum([sum(a[i]) for i in range(n)]))
    if min([min(a[i]) for i in range(n)])>0:
        print("Game Over")
        break
