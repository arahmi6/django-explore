import redis
import pymongo
import psycopg2

# Koneksi ke MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["djangoCustomer"]
transaksi_collection = mongo_db["transaksi"]

# Koneksi ke PostgreSQL
postgres_conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="dataDummy",
    user="postgres",
    password="aulia"
)
postgres_cursor = postgres_conn.cursor()

# Koneksi ke Redis
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

# Mendapatkan data pelanggan dari Postgres
postgres_cursor.execute("SELECT id, nama FROM public.customer_customer")
customer_data = postgres_cursor.fetchall()

# Mendapatkan data transaksi dari MongoDB
transaksi_data = transaksi_collection.find()

# Memasukkan data ke Redis
for transaksi in transaksi_data:
    customer_id = transaksi["id"]
    customer_nama = None
    
    # Mencari nama pelanggan dari data pelanggan yang telah diambil dari Postgres
    for customer in customer_data:
        if customer[0] == customer_id:
            customer_nama = customer[1]
            break
    
    if customer_nama is not None:
        # Format data sesuai dengan yang Anda inginkan
        data_redis = f"{customer_nama}, {transaksi['tahun']}, {transaksi['Total']}"
        
        # Simpan data ke Redis
        redis_key = f"transaksi:{customer_id}"
        redis_client.set(redis_key, data_redis)

# Tutup koneksi ke Postgres
postgres_cursor.close()
postgres_conn.close()
