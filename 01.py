def fun1(n,b):
    if n<b:
        return n
    else:
        return str(fun1(n//b,b)) + str(n%b)
n ,b = map(int,input().split())
print(fun1(n,b))    