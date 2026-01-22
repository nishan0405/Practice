def utopianTree(n):
    # Write your code here
    a=1
    for i in range(n):
        if i%2==0:
            a*=2
        else:
            a+=1
    return a