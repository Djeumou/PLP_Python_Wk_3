def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        price = price - (price*discount_percent)/100
    return price

price = float(input('Please enter the original price of your item '))
discount = float(input('Please, enter the discount that you receive '))

new_price = calculate_discount(price, discount)
print(f'Your new prive is {new_price}')