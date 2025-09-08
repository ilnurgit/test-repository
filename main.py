import json
import os
import asyncio
import aiohttp
from datetime import datetime
from config import HEADERS
from auth import authorize_sheet
from cashback import load_cashback
from updater import prepare_existing_data
from parser import parse_orders
from reviews import load_reviews, process_reviews

async def main():
    sheet_name = input("Введите название листа: ").strip()
    folder_path = os.path.join(".", sheet_name)

    if not os.path.exists(folder_path):
        print(f"[ERROR] Папка «{sheet_name}» не найдена. Создайте папку с таким названием и добавьте туда JSON-файлы.")
        return
