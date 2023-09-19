from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient
from .models import Customer
import redis

def menu(request):
    return render(request, 'customer/base.html')

def get_customer_data(request):
    customers = Customer.objects.all()
    customer_data = [{"id": customer.id, "nama": customer.nama, "kota": customer.kota} for customer in customers]
    # return JsonResponse({"customers": customer_data})
    return render(request, 'customer/customer_postgres.html', {'hasil_input': customer_data,})

def get_transaksi_data(request):
    mongo_client = MongoClient("mongodb://localhost:27017/")
    db = mongo_client["djangoCustomer"]
    transaksi_collection = db["transaksi"]
    
    transaksi_data = list(transaksi_collection.find())
    print(transaksi_data)
    
    return render(request, 'customer/transaction_mongodb.html', {'hasil_input': transaksi_data,})

def get_redis_data(request):
    redis_client = redis.StrictRedis(host="localhost", port=6379, db=0)
    keys = redis_client.keys("transaksi:*")
    
    redis_data = {}
    
    for key in keys:
        data = redis_client.get(key)
        key_parts = key.decode("utf-8").split(":")
        customer_nama = key_parts[1]
        redis_data[customer_nama] = data.decode("utf-8")
    
    #return JsonResponse({"redis_data": redis_data})
    return render(request, 'customer/customer_redis.html', {'hasil_input': redis_data,})