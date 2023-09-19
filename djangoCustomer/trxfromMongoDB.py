import pymongo
import redis
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Mengakses database yang digunakan
db = client["djangoCustomer"]  # Ganti dengan nama database yang Anda gunakan

# Mengakses koleksi transaksi
transaksi_collection = db["transaksi"]  # Ganti dengan nama koleksi yang sesuai

# Mengambil data transaksi berdasarkan ID customer
customer_id = 1  # Ganti dengan ID customer yang sesuai
query = {"ID customer": customer_id}
transaksi_customer = transaksi_collection.find(query)

# Menampilkan hasil
for transaksi in transaksi_customer:
    print("ID customer:", transaksi["ID customer"])
    transaksi_id = transaksi["ID customer"]
    print("Tahun:", transaksi["tahun"])
    print("Total:", transaksi["Total"])

# --------------- REDIS -----------------
# Koneksi ke Redis
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)

# Menyimpan data transaksi ke Redis
transaksi_key = f"transaksi:{transaksi_id}"

transaksi_dict = {
    "ID customer": str(transaksi["ID customer"]),
    "tahun": transaksi["tahun"],
    "Total": transaksi["Total"]
}
# Mengonversi data transaksi menjadi JSON
transaksi_json = json.dumps(transaksi_dict)
# redis_client.set(transaksi_key, transaksi_json)
print("Data transaksi disimpan di Redis dengan kunci:", transaksi_key)

# Mengambil data transaksi dari Redis
transaksi_json_from_redis = redis_client.get(transaksi_key)

# Mengonversi kembali JSON menjadi dict
transaksi_dict_from_redis = json.loads(transaksi_json_from_redis)
print(transaksi_dict_from_redis)
