from django.shortcuts import render
from django.http import JsonResponse
def index(request):
    return render(request, 'accounts/index.html')  # تأكد أن اسم القالب صحيح

def about(request):
    return render(request, 'accounts/about.html')

def form(request):
    return render(request, 'accounts/form.html')

def calc(request):
    return render(request, 'accounts/calc.html')

def calc2(request):
    return render(request, 'accounts/calc2.html')

def card(request):
    return render(request, 'accounts/card.html')

def wheel(request):
    return render(request, 'accounts/wheel.html')

def book(request):
    return render(request, 'accounts/book.html')

def paid_webhook(request):
    data = request.body.decode('utf-8')
    print("✅ Payment Successful:", data)
    return JsonResponse({"status": "received"}, status=200)