vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()

print("Updated Vegetable Inventory:", vegetables)

if ("carrots" in vegetables):
    print("Carrots are alredy in the list.")
if ("cucumbers" in vegetables):
    print("Cucumbers are alredy in the list.")

