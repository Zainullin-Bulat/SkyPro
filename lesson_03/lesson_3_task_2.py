from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 16 Pro", "+79000000000"))
catalog.append(Smartphone("Samsung", "S24 ultra", "+79111111111"))
catalog.append(Smartphone("Google", "Pixel 9", "+79222222222"))
catalog.append(Smartphone("Honor", "magic 6 pro", "+79333333333"))
catalog.append(Smartphone("Xiaomi", "17 pro max", "+79444444444"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
