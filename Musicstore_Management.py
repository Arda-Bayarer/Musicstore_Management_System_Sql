import sqlite3

class Guitar:
    def __init__(self, brand, model, color, type_, magnetic, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.type_ = type_
        self.magnetic = magnetic
        self.price = price
        self.is_sold = False

    def show_info(self):
        print(f"""
            Brand: {self.brand}
            Model: {self.model}
            Price: {self.price}
            Color: {self.color}
            Type: {self.type_}
            Magnetic Sorting: {self.magnetic}
        """)

class Amplifier:

    def __init__(self, brand, model, watt, price):
        self.brand = brand
        self.model = model
        self.watt = watt
        self.price = price

    def show_info(self):
        print(f"""
            Brand: {self.brand}
            Model: {self.model}
            Watt: {self.watt}
            Price: {self.price}
        """)

class MusicStore:
    def __init__(self):
        self.cnn = sqlite3.connect("C:/Users/Lenovo/Desktop/MusicStore.db")
        self.cursor = self.cnn.cursor()

    def _create_tables(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS GUITAR(ID INTEGER PRIMARY KEY AUTOINCREMENT, BRAND VARCHAR(50), MODEL VARCHAR(50), PRICE INT, COLOR VARCHAR(50), G_TYPE VARCHAR(50), MAGNETICSORT VARCHAR(50))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS AMPLIFIER(ID INTEGER PRIMARY KEY AUTOINCREMENT, BRAND VARCHAR(50), MODEL VARCHAR(50), WATT VARCHAR(50), PRICE INT)')
        self.cnn.commit()

    def add_guitar(self):
        print("Add Guitar:")
        brand = input("Brand: ")
        model = input("Model: ")
        color = input("Color: ")
        g_type = input("Type: ")
        magnetic = input("Magnetic Sorting: ")
        price = int(input("Price: "))
        self.cursor.execute('INSERT INTO GUITAR(BRAND, MODEL, PRICE, COLOR, G_TYPE, MAGNETICSORT) VALUES(?,?,?,?,?,?)', (brand, model, price, color, g_type, magnetic))
        self.cnn.commit()
        print(f"{brand} {model} successfully added the system.")

    def add_amplifier(self):
        print("Add Amplifier:")
        brand = input("Brand: ")
        model = input("Model: ")
        watt = input("Watt: ")
        price = int(input("Price: "))
        self.cursor.execute('INSERT INTO AMPLIFIER(BRAND, MODEL, WATT, PRICE) VALUES(?,?,?,?)', (brand, model, watt, price))
        self.cnn.commit()
        print(f"{brand} {model} successfully added the system. ")



    def delete_guitar(self, ıd):
        self.cursor.execute('DELETE FROM GUITAR WHERE ID=?', (ıd,))
        self.cnn.commit()
        print(f"ID:{ıd} succesfully deleted.")

    def delete_amplifier(self, ıd):
        self.cursor.execute('DELETE FROM AMPLIFIER WHERE ID=?', (ıd,))
        self.cnn.commit()
        print(f"ID:{ıd} successfully deleted.")

    def show_all_guitars(self):
        rows = self.cursor.execute('SELECT * FROM GUITAR').fetchall()
        for row in rows:
            guitar = Guitar(row[1], row[2], row[3], row[4], row[5], row[6])
            guitar.show_info()

    def show_all_amplifiers(self):
        rows = self.cursor.execute('SELECT * FROM AMPLIFIER').fetchall()
        for row in rows:
            amplifier = Amplifier(row[1], row[2], row[3], row[4])
            amplifier.show_info()

    def search_guitar(self, model):
        row = self.cursor.execute('SELECT * FROM GUITAR WHERE MODEL=?', (model,)).fetchone()
        if row:
            return Guitar(row[1], row[2], row[3], row[4], row[5], row[6])
        return None

    def search_amp(self, model):
        row = self.cursor.execute('SELECT * FROM AMPLIFIER WHERE MODEL =?', (model,)).fetchone()
        if row:
            return Amplifier(row[1], row[2], row[3], row[4])
        return None


    def close_connection(self):
        self.cnn.close()



musicstore = MusicStore()
musicstore._create_tables()

while True:

    print("*"*20, "Music Store Management Program", "*"*20)

    print("""
        Processes:
            
            1. Add Guitar
            2. Add Amplifier
            3. Delete Guitar
            4. Delete Amplifier
            5. Show all guitars
            6. Show all amplifiers
            7. Search Guitar (You can see ID)
            8. Search Amplifier (You can see ID)
            9. Exit system
    """)

    proc = input("Choose process: ")

    if proc == "1":
        musicstore.add_guitar()
    elif proc == "2":
        musicstore.add_amplifier()
    elif proc == "3":
        ıd = int(input("Please write ID of the target guitar: "))
        musicstore.delete_guitar(ıd)
    elif proc == "4":
        ıd = int(input("Please write ID of the target amplifier: "))
        musicstore.delete_amplifier(ıd)
    elif proc == "5":
        musicstore.show_all_guitars()
    elif proc == "6":
        musicstore.show_all_amplifiers()
    elif proc == "7":
        model = input("Please write the model of the guitar: ")
        guitar = musicstore.search_guitar(model)
        if guitar:
            guitar.show_info()
        else:
            print("Not Found!!!")
    elif proc == "8":
        model = input("Please write the model of amplifier: ")
        musicstore.search_amp(model)
    elif proc == "9":
        print("Turning of the system...")
        break


musicstore.close_connection()














