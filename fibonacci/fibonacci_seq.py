# 1 1 2 3 5 8 13

first=1
second=1
n=0

def fibonacci(first, second):
    global n
    next=first+second
    n=n+1
    return next

if __name__ == "__main__" :
    list=[]
    list.append(first)
    list.append(second)
    next=fibonacci(first,second)

    while(n<20):
        list.append(next)
        first=second
        second=next
        next=fibonacci(first,second)
    print(list)

    #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181