def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    budget=-1
    for k in keyboards:
        for d in drives:
            a=k+d
            if a<=b and a>budget:
                budget=a
    return budget