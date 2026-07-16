from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import XenditTransaction
import xendit
from xendit.apis import InvoiceApi
from xendit import ApiClient, XenditSdkException
import uuid

@login_required
def create_payment(request):
    if request.method == 'POST':
        # Ambil data dari form (misal: jumlah pembayaran)
        amount = int(request.POST.get('amount', 0))
        if amount <= 0:
            return render(request, 'store/error.html', {'message': 'Jumlah tidak valid'})
        
        # Generate Order ID unik
        order_id = f"ORDER-{request.user.id}-{uuid.uuid4().hex[:8]}"
        
        try:
            # Setup Xendit Client
            xendit.set_api_key(settings.XENDIT_SECRET_KEY)
            client = ApiClient()
            invoice_api = InvoiceApi(client)
            
            # Buat parameter invoice
            invoice_data = {
                'external_id': order_id,
                'amount': amount,
                'description': f'Pembayaran untuk order {order_id}',
                'invoice_duration': 86400,  # 24 jam (dalam detik)
                'customer': {
                    'given_names': request.user.username,
                    'email': request.user.email,
                },
                'currency': 'IDR',
                # Optional: tentukan metode pembayaran yang diizinkan
                # 'payment_methods': ['BANK_TRANSFER', 'EWALLET', 'QR_CODE'],
            }
            
            # Panggil API Xendit untuk membuat invoice
            response = invoice_api.create_invoice(invoice_data)
            
            # Simpan transaksi ke database
            transaction = XenditTransaction.objects.create(
                user=request.user,
                order_id=order_id,
                xendit_invoice_id=response.get('id'),
                amount=amount,
                status='PENDING',
                invoice_url=response.get('invoice_url')
            )
            
            # Redirect user ke halaman pembayaran Xendit
            return redirect(response.get('invoice_url'))
            
        except XenditSdkException as e:
            return render(request, 'store/error.html', {'message': str(e)})
    
    return render(request, 'store/checkout.html')