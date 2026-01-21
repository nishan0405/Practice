def countingValleys(steps, path):
    # Write your code here
    count=0
    s=0
    for char in path:
        pre=count
        if char=='U':
            count+=1
        elif char=='D':
            count-=1
        if count<0 and pre==0:
            s+=1
    return s
         