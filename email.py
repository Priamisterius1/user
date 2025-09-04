from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

# Ganti dengan session string kamu
SESSION_STRING = "1BVtsOKEBuzCfdW1GI0INh-u-GZDUZhX5PQPGP2-UfENB4QhkJlaRPD4DRkhBAyr8Gtx_UmGwyH8BeavQi9inl0gOP8uX4C0kYMugBaCngOJl6bXkoKkNAfJcOYYbOy8ugPW8AQ93qgOVhT-2sNe6po52RRNlj9-i7ns626N5G0FZ039wj2-nzMmFx-TjyDlFD2gxezge1_bAIZ8Mb8j0hpg7bBF9NjgUvdYpnIfNhmO7540Uq7h1QQXj6g4wve0XmN4Xoblsciqyzo5-IF3Jvvf9RZOTOeiVp7QqQeuD51JmjCQjgnPFzSw2i6_wjIo8nCJz7c4K6XIWVxjIsS4hZtHAm0U-aFQ="

# API ID dan API HASH dari my.telegram.org
API_ID = 28092269      # ganti dengan API ID kamu
API_HASH = "786a4745d4e4691b527f7d101c1955c3"  # ganti dengan API HASH kamu

async def main():
    # Membuat client dengan session string
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        me = await client.get_me()
        # Menampilkan nomor dan email (jika tersedia)
        print(f"Nama: {me.first_name} {me.last_name if me.last_name else ''}")
        print(f"Nomor: {me.phone}")
        # Email bisa muncul jika diatur di Telegram
        if hasattr(me, 'email') and me.email:
            print(f"Email: {me.email}")
        else:
            print("Email tidak tersedia atau belum diatur di Telegram.")

# Menjalankan async
asyncio.run(main())
