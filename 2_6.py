a,b=map(int,input().split())
c=int(input())
d=(b+c)//60
e=(b+c)%60
if a+d<=23:
    print(a+d, e)
elif a+d>23:
    print(int(a+d-24), e)