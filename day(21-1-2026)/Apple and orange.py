
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    a_count=0
    o_count=0
    for num in apples:
        ap=a+num
        if ap>=s and ap<=t:
            a_count+=1
    for num in oranges:
        oe = b + num
        if s <= oe <= t:
            o_count += 1
    print(a_count)
    print(o_count)
       
