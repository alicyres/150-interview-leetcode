prices = [1,4,7,3,6,4]
    
min_price = min(prices)
min_day = prices.index(min_price)

prices2 = prices[min_day:]

max_price = max(prices2)
max_day = prices2.index(max_price)

profit = max_price - min_price

print("best time to buy: ", min_day,min_price,"best time to sell:" , max_day,max_price,"profit:",profit)
