from customer import Customer
from cart import Cart
from order import Order
from product import Product


def main():
    print("--Kullanıcı Girişi--")
    name = input("Adınızı giriniz: ")
    email = input("E-posta adresinizi giriniz: ")
    customer = Customer(name, email)

    cart = Cart()


    products = {
        "Ütü": Product("Ütü", 2000, 15),
        "Bulaşık Makinesi": Product("Bulaşık Makinesi", 18000, 5),
        "Airfryer": Product("Airfryer", 3500, 20)
    }

    while True:
        print("\n=== Alışveriş Sistemi ===")
        print("1. Ürünleri Listele")
        print("2. Sepete Ürün Ekle")
        print("3. Sepetten Ürün Çıkar")
        print("4. Sepeti Görüntüle")
        print("5. Siparişi Tamamla")
        print("6. Çıkış")

        choice = input("Seçiminizi yapınız: ")

        if choice == "1":
            print("\nMevcut Ürünler:")
            for product in products.values():
                print(product)

        elif choice == "2":
            product_name = input("Eklemek istediğiniz ürünün adını giriniz: ")
            if product_name in products:
                quantity = int(input("Kaç adet eklemek istiyorsunuz?: "))
                cart.add_product(products[product_name], quantity)
                print(f"{quantity} adet {product_name} sepete eklendi!")
            else:
                print("Bu isimde bir ürün bulunamadı!")

        elif choice == "3":
            product_name = input("Çıkarmak istediğiniz ürünün adını giriniz: ")
            cart.remove_product(product_name)
            print(f"{product_name} sepetten çıkarıldı!")

        elif choice == "4":
            print("\nSepetiniz:")
            cart.display_cart()

        elif choice == "5":
            order = Order(customer, cart)
            order.place_order()
            break

        elif choice == "6":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
