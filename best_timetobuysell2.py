prices = [1,2,3,4,5,6]

profit = 0

for i in range(1,len(prices)):
    if prices[i] > prices[i-1]:
        profit += prices[i] - prices[i-1]
        
print(profit)