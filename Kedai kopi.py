class AnandaCoffee:
    def __init__(self):
        self.__listmenu = {
            "a": {"nama": "ES Kopi Susu", "harga": 11000},
            "b": {"nama": "ES Kopi Coklat", "harga": 12000},
            "c": {"nama": "ES Kopi Hitam", "harga": 11000},
            "d": {"nama": "Ice Americano", "harga": 14000}
        }
        self.__pilihan = "y"
    
    def display_menu(self):
        print("""
        ==============================
        Ananda Coffe
        List Menu Minuman Kopi
        ==============================
        A. ES Kopi Susu : Rp 11.000
        B. ES Kopi Coklat : Rp 12.000
        C. ES Kopi Hitam : Rp 11.000
        D. Ice Americano : Rp 14.000
        ==============================
        """)

    def get_menu(self, pesan):
        if pesan in self.__listmenu:
            return self.__listmenu[pesan]
        else:
            return None
    
    def get_harga(self, pesan, jumlahpesan):
        menu = self.get_menu(pesan)
        if menu is None:
            return None
        
        harga = menu["harga"] * jumlahpesan
        ppn = harga * 0.1
        
        if jumlahpesan >= 5:
            diskon = harga * 0.2
            totalharga = harga - diskon + ppn
        else:
            diskon = 0
            totalharga = harga + ppn
        
        return harga, diskon, ppn, totalharga

    def run(self):
        while self.__pilihan == "y":
            self.display_menu()
            pesan = input("masukkan list abjad menu kopi = ")
            jumlahpesan = int(input("masukkan jumlah pesanan = "))
            menu = self.get_menu(pesan)
            if menu is None:
                self.__pilihan = input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N = ")
                continue
            
            listnama = menu["nama"]
            harga, diskon, ppn, totalharga = self.get_harga(pesan, jumlahpesan)
            
            print("--------------------------")
            print("Ananda Coffe")
            print("--------------------------")
            print("Menu :", listnama)
            print("Jumlah Pesan :", jumlahpesan)
            print("Harga :", harga)
            print("Diskon :", diskon)
            print("PPN :", ppn)
            print("--------------------------")
            print("Jumlah Bayar :", totalharga)
            print("--------------------------")
            self.__pilihan = input("apakah anda ingin order kembali Y/N = ")

ananda_coffee = AnandaCoffee()
ananda_coffee.run()
