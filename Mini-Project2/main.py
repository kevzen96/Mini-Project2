Price = int(input("ราคาเต็ม "))
dicount = int(input("ส่วนลด(%) "))
bath = (dicount/100)*Price
Payment = (Price-bath)
print("ส่วนลด %d"%bath)
print("ราคาหลังหักส่วนลด %d"%Payment)