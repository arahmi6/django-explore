from django.shortcuts import render, redirect
from .models import Customer, Transaction


def menu(request):
    return render(request, 'bank/menu.html')


def input_customer(request):
    hasil_input = None
    error_message = None

    if request.method == 'POST':
        name = request.POST['name']

        # Cek apakah customer dengan account_id tersebut sudah ada
        customer_data = Customer.objects.filter(name=name)

        if customer_data.exists():
            hasil_input = customer_data[0]
        else:
            # Simpan data customer ke basis data
            customer = Customer(name=name)
            customer.save()
            hasil_input = customer

    return render(request, 'bank/input_customer.html', {'hasil_input': hasil_input, 'error_message': error_message})


def input_transaction(request):
    hasil_input = None
    error_message = None

    if request.method == 'POST':
        account_id = request.POST['account_id']
        transaction_date = request.POST['transaction_date']
        description = request.POST['description']
        debit_credit_status = request.POST['debit_credit_status']
        amount = request.POST['amount']

        # Mencari data customer berdasarkan account_id
        try:
            customer = Customer.objects.get(id=account_id)
        except Customer.DoesNotExist:
            error_message = "Data nasabah dengan account ID tersebut tidak ada."
            customer = 'None'

        if Transaction.objects.filter(transaction_date=transaction_date).exists():
            error_message = "Transaksi tidak valid."
        else:
            # Simpan data transaction ke basis data
            transaction = Transaction(
                account_id_id=account_id,
                transaction_date=transaction_date,
                description=description,
                debit_credit_status=debit_credit_status,
                amount=amount
            )
            transaction.save()
            hasil_input = transaction

    return render(request, 'bank/input_transaction.html', {'hasil_input': hasil_input, 'error_message': error_message})

def point_nasabah(request):
    hasil_input = None
    error_message = None
    total_points = 0

    if request.method == 'POST':
        name = request.POST['name']
        if name != "":
            # Cek apakah customer dengan nama tersebut ada
            customer_data = Customer.objects.filter(name=name)

            if customer_data.exists():
                customer = customer_data[0]

                # Mengambil transaksi "Beli Pulsa" nasabah
                beli_pulsa_transactions = Transaction.objects.filter(
                    account_id=customer.id,
                    description="Beli Pulsa"
                )

                # Menghitung poin berdasarkan transaksi "Beli Pulsa"
                for transaction in beli_pulsa_transactions:
                    amount = transaction.amount
                    if amount > 10000:
                        if amount > 30000:
                            check = 30000
                            amount -= 30000
                            total_points += (check - 10000) // 1000
                            total_points += amount * 2 // 1000
                        else:
                            total_points += (amount - 10000) // 1000

                # Mengambil transaksi "Beli Pulsa" nasabah
                beli_listrik_transactions = Transaction.objects.filter(
                    account_id=customer.id,
                    description="Beli Listrik"
                )

                # Menghitung poin berdasarkan transaksi "Beli Pulsa"
                for transaction in beli_listrik_transactions:
                    amount = transaction.amount
                    if amount > 50000:
                        if amount > 100000:
                            check = 100000
                            amount -= 100000
                            total_points += (check - 50000) // 2000
                            total_points += amount * 2 // 2000
                        else:
                            total_points += (amount - 50000) // 2000

                hasil_input = customer
        else:
            # Cek apakah customer dengan nama tersebut ada
            customer_data = Customer.objects.all()
            count = 0

            for customer in customer_data:
                customer = customer_data[0]

                # Mengambil transaksi "Beli Pulsa" nasabah
                beli_pulsa_transactions = Transaction.objects.filter(
                    account_id=customer.id,
                    description="Beli Pulsa"
                )

                # Menghitung poin berdasarkan transaksi "Beli Pulsa"
                for transaction in beli_pulsa_transactions:
                    amount = transaction.amount
                    if amount > 10000:
                        if amount > 30000:
                            check = 30000
                            amount -= 30000
                            total_points += (check - 10000) // 1000
                            total_points += amount * 2 // 1000
                        else:
                            total_points += (amount - 10000) // 1000

                # Mengambil transaksi "Beli Pulsa" nasabah
                beli_listrik_transactions = Transaction.objects.filter(
                    account_id=customer.id,
                    description="Beli Listrik"
                )

                # Menghitung poin berdasarkan transaksi "Beli Pulsa"
                for transaction in beli_listrik_transactions:
                    amount = transaction.amount
                    if amount > 50000:
                        if amount > 100000:
                            check = 100000
                            amount -= 100000
                            total_points += (check - 50000) // 2000
                            total_points += amount * 2 // 2000
                        else:
                            total_points += (amount - 50000) // 2000

                hasil_input[count] = customer
                count+=1
    return render(request, 'bank/point_nasabah.html', {'hasil_input': hasil_input, 'error_message': error_message, 'total_points': total_points})


def report_nasabah(request):
    # Membuat daftar untuk menyimpan baris laporan
    report_rows = []

    if request.method == 'POST':
        account_id = request.POST.get('account_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Mengambil transaksi sesuai dengan AccountId, StartDate, dan EndDate
        transactions = Transaction.objects.filter(
             account_id=account_id,
             transaction_date__gte=start_date,
             transaction_date__lte=end_date
             ).order_by('transaction_date')

        # Menginisialisasi saldo awal
        initial_balance = 0

        for transaction in transactions:
            # Menghitung saldo (Balance)
            if transaction.debit_credit_status == 'C':
                initial_balance += transaction.amount
            else:
                initial_balance -= transaction.amount

            # Menambahkan baris laporan
            report_row = {
                'transaction_date': transaction.transaction_date,
                'description': transaction.description,
                'debit': transaction.amount if transaction.debit_credit_status == 'D' else '',
                'credit': transaction.amount if transaction.debit_credit_status == 'C' else '',
                'balance': initial_balance
            }
            report_rows.append(report_row)

    return render(request, 'bank/report_nasabah.html', {'report_rows': report_rows})
