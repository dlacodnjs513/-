def get_fixed_price(discount_rate, discounted_price):
    return discounted_price / (1 - discount_rate / 100)

discount_rate = float(input("할인율은? "))
discounted_price_a = float(input("A 상품의 할인된 가격은? "))
discounted_price_b = float(input("B 상품의 할인된 가격은? "))

fixed_price_a = get_fixed_price(discount_rate, discounted_price_a)
fixed_price_b = get_fixed_price(discount_rate, discounted_price_b)

print("A 상품의 정가는", round(fixed_price_a), "원")
print("B 상품의 정가는", round(fixed_price_b), "원")
