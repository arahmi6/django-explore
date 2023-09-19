import pymongo

# Membuat koneksi ke server MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Ganti dengan URL MongoDB Anda

# Mengakses database yang digunakan
db = client["djangoCustomer"]  # Ganti dengan nama database yang Anda gunakan

# Membuat data transaksi
transaksi = {
    "ID customer": 2,
    "tahun": 2023,
    "Total": 5000.0
}

# Mengakses koleksi transaksi
transaksi_collection = db["transaksi"]  # Ganti dengan nama koleksi yang sesuai

# Menyimpan data transaksi
transaksi_id = transaksi_collection.insert_one(transaksi).inserted_id
print("Data transaksi disimpan dengan ID:", transaksi_id)

