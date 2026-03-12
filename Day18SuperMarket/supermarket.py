# -----------------------------------------------------
#  1.Store Input -Tuple
# ------------------------------------------------------

store_info = ('SuperMart', 'Hyd','9090909090')

print("Welcome to", store_info[0])
print("Location is", store_info[1])
print("Contactus", store_info[2])


print("------------------------------------------")

# -------------------------------------------------------------------
# 2. Create products-Dictonary
# --------------------------------------------------------------------

products = {
    'milk' : 40,
    'bread' : 35,
    'eggs' : 10,
    'rice' : 55,
    'coffeepowder' : 200,
    'chocolate' : 30


}
print("Availabe Items:")
for item,price in products.items():
    print(item.capitalize(),"-",price)

print("------------------------------------------")

# --------------------------------------------------
# Membership - set
# ---------------------------------------------------

members = {'F12','T45','N78','B01'}
member_id = input("Enter Memebership: ").strip().upper()


if member_id in members:
    print("Welcome back to Members🌟🌟🌟🌟🌟")
    is_member =  True
else:
    print("Nee member Added")
    members.add(member_id)
    is_member = False

print(members)

print("--------------------------------------------------------")


# -------------------------------------------------------
#  shopping cart - List
# -------------------------------------------------------
cart = []

print("Start shopping")
print("Type 'done' to stop the shopping")


while True:
    item = input("Enter the product name : ")

    item = item.strip().lower()

    if item == 'done':
        break
    
    if item in products:
        cart.append(item)
        print(item.capitalize(),"Added to the cart")
    else:
        print('Prodcut not found')
print("-----------------------------------------")
print("Cart Items", cart)


# ---------------------------------------------------------
# 5. Billing..............
# --------------------------------------------------------

total = 0
print("\n ---------------BILL---------------------")

unique_items =  set(cart)
for item in unique_items:
    quantity = cart.count(item)
    price =products.get(item)
    item_total= quantity*price
    print(item.capitalize(),"x", quantity, "=", item_total)
    total += item_total

print("---------------------------------------------")
print("Total items: ", len(cart))
print("Total Bill: ", total)



# --------------------------------------------------------
# Membership Discount
# -----------------------------------------


if is_member:
    discount = total * 0.10
    total = total-discount
    print("Membership discount : 10%")

print("-------------------------------")
print("Final Amount:", total)

print("\n Visit Again😊😊❤️")

