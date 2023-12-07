from django.shortcuts import render
from .models import Transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import MoneyhubForm
from django.contrib import messages
import json
import requests  

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'myapp/transaction_list.html', {'transactions': transactions})





def home(request):
    if request.method == 'POST':
        form = MoneyhubForm(request.POST)
        if form.is_valid():
            client_id = form.cleaned_data['client_id']
            secret_key = form.cleaned_data['secret_key']

            print(f"Fetching transactions for client_id: {client_id}")

            moneyhub_api_url = 'https://api.moneyhub.co.uk/v2.0/transactions'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {secret_key}',
            }

            response = requests.get(moneyhub_api_url, headers=headers)

            if response.status_code == 200:
                transactions_data = response.json()

                if transactions_data:
                    print(f"Transactions fetched successfully: {transactions_data}")

                    for transaction_data in transactions_data:
                        Transaction.objects.create(
                            client_id=client_id,
                            amount=transaction_data.get('amount'),
                            description=transaction_data.get('description'),
                        )

                    messages.success(request, 'Transactions fetched successfully')
                    return render(request, 'myapp/transaction_list.html', {'transactions': transactions_data})
                else:
                    print("No transactions found.")
                    messages.info(request, 'No transactions found.')

            else:
                print(f"Failed to fetch transactions. Status code: {response.status_code}")
                if response.status_code == 401:
                    messages.error(request, 'Authentication failed. Please check client_id and secret_key.')
                else:
                    messages.error(request, f"Failed to fetch transactions. Status code: {response.status_code}")

    else:
        form = MoneyhubForm()

    return render(request, 'myapp/home.html', {'form': form})


@csrf_exempt
def webhook_receiver(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received webhook data:", data)

            if data.get('event') == 'TRANSACTION_CREATED':
                client_id = data.get('client_id')
                # transaction_id = data.get('transaction_id')
                amount = data.get('amount')
                description = data.get('description')

                Transaction.objects.create(
                    # transaction_id=transaction_id,
                    client_id=client_id,
                    amount=amount,
                    description=description,
                )

                return JsonResponse({'message': 'Transaction webhook received and processed successfully'})


            return JsonResponse({'message': 'Webhook received and processed successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request'}, status=400)

    return JsonResponse({'error': 'Method Not Allowed'}, status=405)
