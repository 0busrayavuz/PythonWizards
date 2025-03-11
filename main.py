from customer import Customer
from product import Product
from cart import Cart
from order import Order

product1 = Product("Ütü", 4000, 10)
product2 = Product("Airfryer", 3500, 20)
product3 = Product("Kurutma Makinesi", 21000, 5)

products = [product1, product2, product3]

name = input("Adınızı girin: ")
email = input("E-posta adresinizi girin: ")
customer = Customer(name, email)

cart = Cart()

while True:
    print("\n---- MENÜ ----")
    print("1. Ürün Ekle")
    print("2. Ürün Çıkar")
    print("3. Sepeti Görüntüle")
    print("4. Sipariş Oluştur")
    print("5. Çıkış")

    choice = input("Bir seçenek girin: ")

    if choice == '1':
        print("\nMevcut Ürünler:")
        for idx, prod in enumerate(products, 1):
            print(f"{idx}. {prod}")
        product_choice = int(input("\nEklemek istediğiniz ürünün numarasını girin: "))
        quantity = int(input(f"{products[product_choice - 1].name} için eklemek istediğiniz miktarı girin: "))
        cart.add_product(products[product_choice - 1], quantity)

    elif choice == '2':
        print("\nSepetinizdeki Ürünler:")
        for idx, item in enumerate(cart.items.values(), 1):
            print(f"{idx}. {item['product'].name} - {item['quantity']} adet")
        remove_choice = int(input("\nÇıkarmak istediğiniz ürünün numarasını girin: "))
        product_name = list(cart.items.keys())[remove_choice - 1]
        cart.remove_product(product_name)

    elif choice == '3':
        print("\nSepetiniz:")
        cart.display_cart()

    elif choice == '4':
        order = Order(customer, cart)
        order.place_order()
        break

    elif choice == '5':
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçenek! Tekrar deneyin.")
