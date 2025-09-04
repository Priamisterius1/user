# login_session_old.py
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

# Masukkan API ID dan API HASH Telegram kamu
api_id = 28092269          # ganti dengan API ID kamu
api_hash = '786a4745d4e4691b527f7d101c1955c3'  # ganti dengan API HASH kamu

# Masukkan session string lama yang sudah kamu simpan
session_string = input("Masukkan session string lama: ").strip()

async def main():
    # Login pakai session string lama
    client = TelegramClient(StringSession(session_string), api_id, api_hash)

    async with client:
        me = await client.get_me()
        print(f"Login berhasil! Nomor akun: {me.phone}")

if __name__ == "__main__":
    asyncio.run(main())
