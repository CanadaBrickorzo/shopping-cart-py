shop_cart = [];
def addItem(item):
    shop_cart.append(item)
    print(shop_cart)
def removeItem(item):
    if item not in shop_cart:
        print("Item doesn't exist!")
    else:
        shop_cart.remove(item)
        print(shop_cart)
def checkCart():
    if not shop_cart:
        print("Shopping cart is empty!")
    else:
        print(shop_cart)

while True:
    print('-----------------------')
    task = input('Task to perform:\n>>> ')

    if task == 'add':
        i = input('Item to add: ')
        addItem(i)
    elif task == 'remove':
        i = input('Item to remove: ')
        removeItem(i)
    elif task == 'check':
        checkCart()
    else:
        print('Invalid option!')
