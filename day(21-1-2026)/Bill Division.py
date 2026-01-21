def bonAppetit(bill, k, b):
    # Write your code here
    cost=0
    actual=0
    cost=sum(bill)
    actual=(cost-bill[k])//2
    if actual==b:
        print("Bon Appetit")
    else:
        print(b-actual)