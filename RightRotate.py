def rightRotate(a,n):
    temp = a[n-1]
    for i in range(n-1,0,-1):
        a[i] = a[i-1]
    a[0] = temp
def printArr(a,n):
    for i in range(n):
        print(a[i],end=" ")
    print()
def main():
    t=int(input())
    while t>0:
        n,m=map(int,input().split())
        a=list(map(int, input().split()))
        for i in range(m):
            rightRotate(a,n)
        printArr(a,n)
        t=t-1
if __name__ == '__main__':
    main()
        
