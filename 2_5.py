a,b=map(int,input().split())

if b>=45:
    print(a, b-45)
elif a!=0 and 45>b:
    print(a-1, b+15)
elif a == 0 and 45>b:
    print(23, b+15)