n =1260
coin_List = [500,100,50,10]
count = 0
for coin in coin_List:
    if n > coin:
        #count = count + n//coin
        count += n//coin
        #n = n%coin
        n %= coin
print(count)
