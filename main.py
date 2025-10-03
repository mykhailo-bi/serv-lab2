import hashlib

class User:
    __max_id = -1
    def __init__(self, username, email, password):
        User.__max_id += 1
        self.__id = User.__max_id
        self.username = username
        self.email = email
        h = hashlib.sha512()
        h.update(password.encode('utf-8'))
        self.__password_hash = h.hexdigest()
        self.__cart = {}

    @staticmethod
    def max_id():
        return User.__max_id
        
    @property
    def id(self):
        return self.__id
        
    @property
    def password_hash(self):
        return self.__password_hash
    
    @property
    def cart(self):
        return self.__cart
    
    def add_to_cart(self, store, product_id, count):
        if count <= 0:
            raise ValueError('Count must be greater than zero')
        if count > store.products.get(product_id, store.products[0]).count:
            raise ValueError('Not enough products in store')
        self.__cart[product_id] = self.__cart.get(product_id, 0) + count
        store.products[product_id].count -= count

    def set_cart(self, store, product_id, count):
        current_count = self.__cart.get(product_id, 0)
        if count < 0:
            raise ValueError('Count must be greater than or equal to zero')
        else:
            self.__cart[product_id] = count
        store.products[product_id].count = store.products.get(product_id, store.products[0]).count + current_count - count
    
    def total_cart_price(self):
        total = 0.0
        for k, v in self.__cart.items():
            total += store.products[k].price * v
        return total
    
    def buy(self, store):
        store.balance += self.total_cart_price()
        self.__cart = {}
    
class Store:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.products = {}

class Product:
    __max_id = -1
    def __init__(self, store, name, description, price, count):
        Product.__max_id += 1
        self.__id = Product.__max_id
        self.name = name
        self.description = description
        self.price = price
        self.count = count
        store.products[self.__id] = self

    @staticmethod
    def max_id():
        return User.__max_id
        
    @property
    def id(self):
        return self.__id
    
    def work(self):
        print(self.description + '\n' + 'Hello! I am empty product My price ist ' + str(self.price))

class Phone(Product):
    def __init__(self, store, name, description, price, pamiec, count):
        Product.__init__(self, store, name, description, price, count)
        self.description = 'Phone ' + self.description
        self.pamiec = pamiec

    def work(self):
        print(self.description + '\n' + 'Hello! I am phone My price ist ' + str(self.price))

class Camera(Product):
    def __init__(self, store, name, description, price, megapixels, count):
        Product.__init__(self, store, name, description, price, count)
        self.description = 'Camera ' + self.description
        self.megapixels = megapixels

    def work(self):
        print(self.description + '\n' + 'Hello! I am camera My price ist ' + str(self.price))

class CameraPhone(Phone, Camera):
    def __init__(self, store, name, description, price, pamiec, megapixels, count):
        Phone.__init__(self, store, name, description, price, pamiec, count)
        Camera.__init__(self, store, name, description, price, megapixels, count)
        self.description = 'CameraPhone ' + self.description
        
    def work(self):
        print(self.description + '\n' + 'Hello! I am cameraphone My price ist ' + str(self.price))

store = Store('store')

null_product = Product(store, '', '', 0, 0)
camera = Camera(store, 'Nikon', 'Nikon camera veri gut ja', 15000.00, 69, 30)
phone = Phone(store, 'Redmi note 4', 'Mido', 5000.00, 32, 30)
cameraphone = CameraPhone(store, 'Pixel 10 pro max', 'Pixil 10 promax Very camera phone', 50000.00, 512, 108, 15)

print(camera.id, camera.name, camera.description, camera.price, camera.megapixels, camera.count)
print(phone.id, phone.name, phone.description, phone.price, phone.pamiec, phone.count)
print(cameraphone.id, cameraphone.name, cameraphone.description, cameraphone.price, cameraphone.pamiec, cameraphone.megapixels, cameraphone.count)

user1 = User('user1', 'user1@example.com', '')
print(user1.id, user1.username, user1.email, user1.password_hash)
user1.add_to_cart(store, 1, 3)
print(user1.cart)
user1.add_to_cart(store, 2, 3)
print(user1.cart)
user1.set_cart(store, 1, 3)
print(user1.cart)
print(user1.total_cart_price())
print(User.max_id())

print(camera.id, camera.name, camera.description, camera.price, camera.megapixels, camera.count)
print(phone.id, phone.name, phone.description, phone.price, phone.pamiec, phone.count)
print(cameraphone.id, cameraphone.name, cameraphone.description, cameraphone.price, cameraphone.pamiec, cameraphone.megapixels, cameraphone.count)

user2 = User('user2', 'user2@example.com', '')
print(user2.id, user2.username, user2.email, user2.password_hash)
user2.add_to_cart(store, 1, 3)
print(user2.cart)
user2.add_to_cart(store, 1, 3)
print(user2.cart)
user2.set_cart(store, 2, 3)
print(user2.cart)
print(user2.total_cart_price())
print(User.max_id())

print(camera.id, camera.name, camera.description, camera.price, camera.megapixels, camera.count)
print(phone.id, phone.name, phone.description, phone.price, phone.pamiec, phone.count)
print(cameraphone.id, cameraphone.name, cameraphone.description, cameraphone.price, cameraphone.pamiec, cameraphone.megapixels, cameraphone.count)

camera.work()
phone.work()
cameraphone.work()

print('=== BUYING ===')

user1.buy(store)
user2.buy(store)
print(store.balance)
print(user1.cart)
print(user1.total_cart_price())
print(user2.cart)
print(user2.total_cart_price())

print(camera.__id)