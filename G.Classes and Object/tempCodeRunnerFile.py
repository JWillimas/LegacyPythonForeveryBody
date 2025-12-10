class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

#Magic Method--Python uses them internally for built-in operations.

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]#use it as index operation

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

cart = Cart()

cart.add('Laptop')

print(len(cart))   # 1

print('Laptop' in cart) # True

print(cart[0])#Laptop

print('Laptop' in cart)