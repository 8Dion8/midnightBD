from utils.db import DBHandler

import random
import datetime
from faker import Faker

fake = Faker('ru_RU')
handler = DBHandler()


def generate_fake_client_data(num_records):
    data = []
    for _ in range(num_records):
        name = fake.name()
        phone_number = f"+7{fake.numerify('##########')}"
        telegram_id = f"@{fake.user_name()}" if random.choice([True, False]) else ''
        vk_id = f"https://vk.com/{fake.user_name()}" if random.choice([True, False]) else ''
        avito_link = f"https://www.avito.ru/brands/{fake.random_number()}" if random.choice([True, False]) else ''
        whatsapp = f"+7{fake.numerify('##########')}" if random.choice([True, False]) else ''

        # Ensure at least one contact method is filled
        if not (telegram_id or vk_id or avito_link or whatsapp):
            telegram_id = f"@{fake.user_name()}"
            
        rating = str(random.choices([1, 2, 3, 4, 5], weights=[0.1, 0.2, 0.3, 0.4, 0.5])[0])

        data.append({
            "Name": name, 
            "Phone Number": phone_number, 
            "Telegram ID": telegram_id, 
            "VK ID": vk_id, 
            "Avito Link": avito_link, 
            "WhatsApp": whatsapp,
            "Rating": rating,
            "Notes": ""
        })
    return data

def generate_fake_build_data(num):
    cpus = ["Intel Core i9-13900K", "Intel Core i7-13700K", "Intel Core i5-13600K", "AMD Ryzen 9 7950X", "AMD Ryzen 7 7700X", "AMD Ryzen 5 7600X", "Intel Core i9-12900K", "Intel Core i7-12700K", "Intel Core i5-12600K", "AMD Ryzen 9 5950X", "AMD Ryzen 7 5800X", "AMD Ryzen 5 5600X", "Intel Core i9-11900K", "Intel Core i7-11700K", "Intel Core i5-11600K", "AMD Ryzen 9 5900X", "AMD Ryzen 7 5800X", "AMD Ryzen 5 5600X", "Intel Core i9-10900K", "Intel Core i7-10700K", "Intel Core i5-10600K", "AMD Ryzen 9 3950X", "AMD Ryzen 7 3800X", "AMD Ryzen 5 3600X", "Intel Core i9-9900K", "Intel Core i7-9700K", "Intel Core i5-9600K", "AMD Ryzen 7 2700X", "AMD Ryzen 5 2600X", "Intel Core i9-8700K", "Intel Core i7-8700K", "Intel Core i5-8600K", "AMD Ryzen 7 1800X", "AMD Ryzen 5 1600X", "Intel Core i9-7900X", "Intel Core i7-7800X", "Intel Core i5-7600K", "AMD Ryzen 9 5980HS", "AMD Ryzen 9 5900HS", "AMD Ryzen 7 5800HS", "Intel Core i9-12900HK", "Intel Core i7-12800H", "Intel Core i5-12600H", "AMD Ryzen 9 6980HX", "AMD Ryzen 9 6900HS", "AMD Ryzen 7 6800H", "Intel Core i9-11980HK", "Intel Core i7-11800H", "Intel Core i5-11400H"]
    gpus = ["Nvidia GeForce RTX 4090", "Nvidia GeForce RTX 4080", "Nvidia GeForce RTX 4070 Ti", "Nvidia GeForce RTX 4070", "AMD Radeon RX 7900 XTX", "AMD Radeon RX 7900 XT", "Nvidia GeForce RTX 3090 Ti", "Nvidia GeForce RTX 3090", "AMD Radeon RX 6950 XT", "AMD Radeon RX 6900 XT", "Nvidia GeForce RTX 3080 Ti", "Nvidia GeForce RTX 3080", "AMD Radeon RX 6800 XT", "AMD Radeon RX 6800", "Nvidia GeForce RTX 3070 Ti", "Nvidia GeForce RTX 3070", "AMD Radeon RX 6700 XT", "AMD Radeon RX 6600 XT", "Nvidia GeForce RTX 3060 Ti", "Nvidia GeForce RTX 3060", "AMD Radeon RX 6600", "Nvidia GeForce RTX 2080 Ti", "Nvidia GeForce RTX 2080 Super", "Nvidia GeForce RTX 2080", "Nvidia GeForce RTX 2070 Super", "Nvidia GeForce RTX 2070", "Nvidia GeForce RTX 2060 Super", "Nvidia GeForce RTX 2060", "AMD Radeon RX 5700 XT", "AMD Radeon RX 5700", "AMD Radeon RX 5600 XT", "AMD Radeon RX 5500 XT", "Nvidia GeForce GTX 1660 Ti", "Nvidia GeForce GTX 1660 Super", "Nvidia GeForce GTX 1660", "Nvidia GeForce GTX 1650 Super", "Nvidia GeForce GTX 1650", "AMD Radeon RX 590", "AMD Radeon RX 580", "AMD Radeon RX 570", "Nvidia GeForce GTX 1080 Ti", "Nvidia GeForce GTX 1080", "Nvidia GeForce GTX 1070 Ti", "Nvidia GeForce GTX 1070", "AMD Radeon RX Vega 64", "AMD Radeon RX Vega 56", "Nvidia GeForce GTX 1060", "AMD Radeon RX 480", "AMD Radeon RX 470", "Nvidia GeForce GTX 980 Ti", "Nvidia GeForce GTX 980", "AMD Radeon R9 390X", "AMD Radeon R9 390"]
    motherboards = ["Asus ROG Maximus Z790 Extreme", "MSI MEG Z790 ACE", "Gigabyte Z790 Aorus Master", "ASRock Z790 Taichi", "Asus ROG Strix Z790-E Gaming WiFi", "MSI MPG Z790 Edge WiFi", "Gigabyte Z790 Aorus Elite AX", "ASRock Z790 Steel Legend WiFi 6E", "Asus TUF Gaming Z790-Plus WiFi D4", "MSI PRO Z790-A WiFi", "Gigabyte Z790 UD AX", "ASRock Z790 Phantom Gaming 4", "Asus Prime Z790-P WiFi", "MSI PRO Z790-P WiFi", "Gigabyte Z790 Gaming X AX", "ASRock Z790 PG Riptide", "Asus ROG Crosshair X670E Extreme", "MSI MEG X670E ACE", "Gigabyte X670E Aorus Master", "ASRock X670E Taichi", "Asus ROG Strix X670E-E Gaming WiFi", "MSI MPG X670E Carbon WiFi", "Gigabyte X670E Aorus Elite AX", "ASRock X670E Pro RS", "Asus TUF Gaming X670E-Plus WiFi", "MSI Pro X670-P WiFi", "Gigabyte X670 Aorus Elite AX", "ASRock X670 Steel Legend", "Asus Prime X670-P WiFi", "MSI Pro X670-P WiFi DDR5", "Gigabyte B650 Aorus Elite AX", "ASRock B650E PG Riptide WiFi", "Asus TUF Gaming B650-Plus WiFi", "MSI Pro B650-P WiFi", "Gigabyte B650M Aorus Elite AX", "ASRock B650M-HDV/M.2"]
    rams = ["G.Skill Trident Z5 RGB DDR5-6400", "Corsair Dominator Platinum RGB DDR5-6200", "Crucial DDR5-5200", "Kingston Fury Beast DDR5-5600", "G.Skill Trident Z Neo DDR4-3600", "Corsair Vengeance RGB Pro DDR4-3200", "Crucial Ballistix DDR4-3600", "Kingston HyperX Fury DDR4-3466", "G.Skill Ripjaws V DDR4-3200", "Corsair Vengeance LPX DDR4-3000", "Crucial Ballistix Sport LT DDR4-2666", "Kingston HyperX Predator DDR4-3200", "G.Skill Aegis DDR4-3000", "Corsair Vengeance RGB Pro SL DDR4-3600", "Crucial Ballistix MAX DDR4-4400", "Kingston HyperX Fury RGB DDR4-3733", "G.Skill Trident Z Royal DDR4-4000", "Corsair Dominator Platinum RGB DDR4-3600", "Crucial Ballistix Elite DDR4-3466", "Kingston HyperX Predator RGB DDR4-4266"]
    psus = ["Corsair HX1000", "EVGA SuperNOVA 1000 GT", "Seasonic Prime TX-1000", "Cooler Master V1000 Platinum", "Thermaltake Toughpower GF1 1000W", "be quiet! Dark Power Pro 12 1000W", "NZXT C1000 Gold", "Antec HCG Extreme 1000W", "Silverstone ST1000-TI", "FSP Hyper M 1000W", "Enermax Revolution D.F. 1000W", "Phanteks Revolt Pro 1000W", "Fractal Design Ion+ 1000W Platinum", "Deepcool DQ1000M", "ASUS ROG Thor 1000W Platinum II", "MSI MPG A1000G", "Gigabyte AORUS P1000W", "ASRock Forge 1000W", "Lian Li Lancool III 1000W", "In Win Commander III 1000W"]
    ssds = ["Samsung 980 Pro", "WD Black SN850X", "Crucial P5 Plus", "Sabrent Rocket 4 Plus", "Seagate FireCuda 530", "SK hynix Platinum P41", "Adata XPG Gammix S70 Blade", "Teamgroup T-Force Cardea A440 Pro", "Corsair MP600 Pro XT", "Gigabyte Aorus Gen4 7000s", "Kingston Fury Renegade", "Silicon Power US70", "Patriot Viper VP4300", "Inland Performance Plus", "Mushkin Enhanced Helix-L", "Addlink S95", "Samsung 970 Evo Plus", "WD Black SN850", "Crucial P5", "Sabrent Rocket 4.0", "Seagate FireCuda 520", "SK hynix Gold P31", "Adata XPG SX8200 Pro", "Teamgroup T-Force Cardea Zero Z440", "Corsair MP600 Pro", "Gigabyte Aorus Gen4 7000s Prem", "Kingston KC3000", "Silicon Power US70 EVO"]
    cases = ["Lian Li O11 Dynamic Evo", "Corsair 4000D Airflow", "Fractal Design Torrent", "be quiet! Pure Base 500DX", "NZXT H7 Flow", "Phanteks Eclipse P360A", "Cooler Master MasterBox TD500 Mesh", "Thermaltake View 51 ARGB", "In Win A3", "Antec DF700 Flux", "Deepcool CK560 Mesh", "Montech Air 1000 Mesh", "Silverstone SETA A1", "Asus TUF Gaming GT301", "MSI MPG Gungnir 110R", "Gigabyte C200 Glass", "ASRock Mars 120", "Razer Tomahawk ATX", "EVGA DG-77", "Cougar Blazer", "Aerocool Bolt", "Zalman S5 TG", "SilverStone Primera PM02", "Kolink Citadel Mesh RGB", "Azza Pyramid 804V", "Anidees AI Crystal V3", "Jonsbo UMX4", "Musetex 905S4", "Xigmatek Venom X", "SilentiumPC Regnum RG6V TG"]
    cpu_coolers = ["Noctua NH-D15", "be quiet! Dark Rock Pro 4", "NZXT Kraken Z73", "Corsair iCUE H150i Elite LCD", "EVGA CLC 360mm", "Deepcool Assassin III", "Asus ROG Strix LC 360 RGB", "MSI MEG CoreLiquid S360", "Fractal Design Lumen S36 RGB", "Thermaltake ToughAir 510", "ID-Cooling SE-207-XT", "Scythe Fuma 2 Rev.B", "Cryorig R1 Ultimate", "Thermalright Peerless Assassin 120", "SilverStone Permafrost PF360-ARGB", "Arctic Liquid Freezer II 360", "Cooler Master MasterLiquid ML360 Mirror", "EK-AIO Elite 360 D-RGB", "Alphacool Eisbaer Aurora 360", "Phanteks Glacier One 360MPH", "Noctua NH-U12A", "be quiet! Shadow Rock 3", "NZXT Kraken M22", "Corsair H60 (2018)", "EVGA CLC 120mm", "Deepcool Gammaxx 400 V2", "Asus TUF Gaming LC 120 RGB", "MSI MAG CoreLiquid 120R"]
    case_fans = ["Noctua NF-A12x25 PWM", "be quiet! Silent Wings 3 120mm PWM High-Speed", "Corsair LL120 RGB 120mm", "NZXT Aer RGB 2 120mm", "Deepcool CF120 Plus", "Asus TUF Gaming AF120", "MSI Mag Silencio 120", "Fractal Design Prisma AL-12 PWM", "Thermaltake Toughfan 12 Turbo", "Antec TriCool 120mm", "SilverStone Air Blazer 120mm", "Cougar Vortex PWM 120mm", "Aerocool Frost 12 FRGB", "Zalman ZM-SF120", "Xigmatek XAF 120mm", "Enermax SquA RGB 120mm", "Phanteks PH-F120SK", "Lian Li UNI Fan AL120", "ID-Cooling ZF-12025 Argb", "Scythe Kaze Flex 120 RGB"]
    statuses = ["В ожидании железа", "Готов к сборке", "Собран", "Отдан", "Отдан", "Отдан"]
    
    data = []
    
    for _ in range(num):
        client = str(random.randint(1,32))
        cpu = random.choice(cpus)
        gpu = random.choice(gpus)
        motherboard = random.choice(motherboards)
        ram = random.choice(rams)
        psu = random.choice(psus)
        ssd = random.choice(ssds)
        cas = random.choice(cases)
        cooler = random.choice(cpu_coolers)
        fans = random.choice(case_fans)
        price = str(random.randint(30, 200) * 1000)
        status = random.choice(statuses)
        date_start = fake.date_between(datetime.date(2023, 1, 1)).strftime("%Y-%m-%d")
        date_end = fake.date_between(datetime.datetime.strptime(date_start, "%Y-%m-%d")).strftime("%Y-%m-%d") if status == "Отдан" else ""
        
        data.append([client, cpu, gpu, motherboard, ram, psu, ssd, cas, cooler, fans, date_start, date_end, price, status])
    
    return data
    
    
    

fake_data = generate_fake_client_data(32)
for record in fake_data:
    print(record)
    print(record.values())
    handler.insert_single_row('clients', list(record.values()))
    
fake_data = generate_fake_build_data(64)
for record in fake_data:
    print(record)
    handler.insert_single_row('orders_build', record)
