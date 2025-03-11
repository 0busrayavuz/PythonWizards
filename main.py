from customer import Customer
from cart import Cart
from order import Order
from product import Product


def main():
    print("-- Kullanıcı Girişi --")
    name = input("Adınızı giriniz: ")
    email = input("E-posta adresinizi giriniz: ")
    customer = Customer(name, email)

    cart = Cart()

    products = {
        "Airfryer": Product("Airfryer", 20000, 5),
        "Ütü": Product("Ütü", 15000, 10),
        "Kurutma Makinesi": Product("Kurutma Makinesi", 500, 20)
    }

    while True:
        print("\n-- Alışveriş Sistemi --")
        print("1. Sepete Ürün Ekle")
        print("2. Sepetten Ürün Çıkar")
        print("3. Sepeti Görüntüle")
        print("4. Siparişi Tamamla")
        print("5. Çıkış")

        choice = input("Seçiminizi yapınız: ")
        if choice == "1":
            product_name = input("Eklemek istediğiniz ürünün adını giriniz: ")
            if product_name in products:
                quantity = int(input("Kaç adet eklemek istiyorsunuz?: "))
                cart.add_product(products[product_name], quantity)
                print(f"{quantity} adet {product_name} sepete eklendi!")
            else:
                print("Bu isimde bir ürün bulunamadı!")

        elif choice == "2":
            product_name = input("Çıkarmak istediğiniz ürünün adını giriniz: ")
            cart.remove_product(product_name)
            print(f"{product_name} sepetten çıkarıldı!")

        elif choice == "3":
            print("\nSepetiniz:")
            cart.display_cart()

        elif choice == ("4"):
            order = Order(customer, cart)
            order.place_order()
            break

        elif choice == "5":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
