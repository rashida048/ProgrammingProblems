def maxProfit(li):
    mp = 0
    for ind, i in enumerate(li):
        for j in li[(ind+1):]:
            mp =  max(mp, j-i)
    return mp

#print(maxProfit([7,1,5,3,6,4]))

def maxProfit1(price):
    mp = 0
    minP = price[0]
    for p in price:
        if p < minP:
            minP = p
        mp = max(mp, p - minP)
    return mp

print(maxProfit1([7,1,5,3,6,4]))

            

        
        
