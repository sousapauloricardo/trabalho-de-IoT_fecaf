import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=3308
    )
    print("✅ SUCESSO: O Python conseguiu falar com o Docker!")
    conn.close()
except Exception as e:
    print(f"❌ ERRO: {e}")