def sockMerchant(n, ar):
    # Write your code here
    count=0
    unique=[]
    for num in ar:
        if num not in unique:
            unique.append(num)
        elif num in unique:
            count+=1
            unique.remove(num)
    return count