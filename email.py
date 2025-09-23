from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("Masukkan API ID dan API Hash dari my.telegram.org")
api_id = int(input("API ID: "))
api_hash = input("API HASH: ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("LOGIN Nomor HP Telegram (contoh: +628xxx)")
    print("Setelah itu cek kode OTP di Telegram/SMS.")
    print("\n🔑 String Session kamu:\n")
    print(client.session.save())
    
