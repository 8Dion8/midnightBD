from utils.db import DBHandler

import random
from faker import Faker

fake = Faker('ru_RU')
handler = DBHandler()

def generate_fake_data(num_records):
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

        data.append({
            "Name": name,
            "Phone Number": phone_number,
            "Telegram ID": telegram_id,
            "VK ID": vk_id,
            "Avito Link": avito_link,
            "WhatsApp": whatsapp
        })
    return data
    
    

fake_data = generate_fake_data(64)
for record in fake_data:
    print(record)
    print(record.values())
    handler.insert_single_row('clients', list(record.values()))
    