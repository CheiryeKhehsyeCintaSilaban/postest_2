class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

class produk:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

# Data produk
daftarproduk = [
    produk(1, "Pohon Natal", 400, 50),
    produk(2, "Paket Aksesoris Pohon Natal", 75, 80),
    produk(3, "Balon Tema Natal", 30, 100),
    produk(4, "Topi Santa", 20, 100),
    produk(5, "Lonceng Natal", 10, 150)
]

def display_products():
    print("\nDaftar Produk:")
    for product in daftarproduk:
        print(f"{product.product_id}. {product.name}  | Harga: IDR {product.price}  | Stok: {product.stock}")


def add_product():
    print("\nMenambahkan Produk Baru:")
    product_id = len(daftarproduk) + 1
    name = input("Masukkan nama produk: ")
    price = float(input("Masukkan harga produk: "))
    stock = int(input("Masukkan stok produk: "))
    daftarproduk.append(produk(product_id, name, price, stock))
    print(f"Produk {name} telah ditambahkan.")

def update_product():
    display_products()
    product_id = int(input("Masukkan ID produk yang ingin diperbarui: "))
    
    for product in daftarproduk:
        if product.product_id == product_id:
            product.price = float(input(f"Masukkan harga baru untuk {product.name}: "))
            product.stock = int(input(f"Masukkan stok baru untuk {product.name}: "))
            print(f"{product.name} telah diperbarui.")
            return
    
    print("Produk tidak ditemukan.")

def delete_product():
    display_products()
    product_id = int(input("Masukkan ID produk yang ingin dihapus: "))
    
    for product in daftarproduk:
        if product.product_id == product_id:
            daftarproduk.remove(product)
            print(f"{product.name} telah dihapus.")
            return
    
    print("Produk tidak ditemukan.")

def user_transaction(user):
    display_products()
    product_id = int(input("Masukkan Nomor produk yang ingin dibeli: "))
    quantity = int(input("Masukkan jumlah produk yang ingin dibeli: "))

    for product in daftarproduk:
        if product.product_id == product_id:
            if quantity <= product.stock:
                total = product.price * quantity
                product.stock -= quantity
                print(f"Transaksi berhasil. Total biaya: Rp.{total}")
                
            else:
                print("Stok produk tidak mencukupi.")
            
   

#pengguna dan admin
users = [User("user1", "pw1"), User("user2", "pw2")]
admin = Admin("admin", "adminpw")

#Program utama
while True:
    print("============================================================================================================")
    print("\t\t\t\t Welcome To XmasWorld !!!")
    print("============================================================================================================")
    print("1. Login sebagai pengguna")
    print("2. Login sebagai admin")
    print("3. Keluar")

    choice = input("Masukkan pilihan Anda: ")

    if choice == '1':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # Validasi pengguna
        if any(user.username == username and user.password == password for user in users):
            print("Login sukses sebagai pengguna.")
            user_transaction(username)
        else:
            print("Login gagal. Username atau password salah.")
            break

    elif choice == '2':
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")

        # Validasi admin
        if admin.username == username and admin.password == password:
            print("Login sukses sebagai admin.")
            while True:
                print("\nMenu Admin:")
                print("1. Tampilkan Produk")
                print("2. Tambah Produk")
                print("3. Perbarui Produk")
                print("4. Hapus Produk")
                print("5. Keluar sebagai admin")

                admin_choice = input("Masukkan pilihan admin: ")

                if admin_choice == '1':
                    display_products()
                elif admin_choice == '2':
                    add_product()
                elif admin_choice == '3':
                    update_product()
                elif admin_choice == '4':
                    delete_product()
                elif admin_choice == '5':
                    print("Keluar dari mode admin.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    break

        else:
            print("Login gagal. Username atau password admin salah.")
            break

    elif choice == '3':
        print("Terima kasih, sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
