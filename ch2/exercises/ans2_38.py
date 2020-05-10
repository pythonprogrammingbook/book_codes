prices = {'002415': 32.03, '600519': 1296.25, '600036': 34.46, '002138': 22.78, '600584': 27.23}
prices_greater_than_30 = {
    key: value
    for key, value in prices.items() if value > 30
}  #股价大于30元的股票创建一个新的字典
print(prices_greater_than_30)
max_stock_index = max(prices_greater_than_30)
min_stock_index = min(prices_greater_than_30)
avg_price = sum(prices_greater_than_30.values()) / len(prices_greater_than_30)
print(f"Max:{max_stock_index};Min:{min_stock_index}; Average Price:{avg_price}.")