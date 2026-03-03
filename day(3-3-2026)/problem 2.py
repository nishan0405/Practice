def angryProfessor(k, a):
    # Write your code here
    on_time=0
    late=0
    for num in a:
        if num<=0:
            on_time+=1
        elif num>0:
            late+=1
    if on_time>=k:
        return "NO"
    else:
        return "YES"