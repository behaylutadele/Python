def calculate_discount():
    original = input('Enter the original amount: ')
    discount = input('Enter the discount percent: ')
    original = float(original)
    discount = float(discount)
    final_price = original - ((original * discount) / 100)
    return final_price

print("The final Price after applying the discount is:", calculate_discount())
