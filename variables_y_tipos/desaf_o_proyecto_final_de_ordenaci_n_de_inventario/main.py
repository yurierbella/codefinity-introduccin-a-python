# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

category1 = categories[0:11]
category2 = categories[13:]

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

promotion_bubblegum = ("We have " + candy1 + " for " + bubblegum_price + " in the " + category1)
promotion_chocolate = ("We have " + candy2 + " for " + chocolate_price + " in the " + category1)
promotion_pasta = ("We have " + dry_goods + " for " + pasta_price + " in the " + category2)

print(promotion_bubblegum)
print(promotion_chocolate)
print(promotion_pasta)