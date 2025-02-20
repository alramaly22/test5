from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
import json

def index(request):
    return render(request, 'accounts/index.html')

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
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("✅ Payment Data Received:", data)

            # تأكد أن الدفع ناجح من بيانات البوابة
            payment_status = data.get("status")  # عدّل المفتاح حسب استجابة البوابة
            if payment_status == "paid":  # تأكد أن الحالة تعني الدفع ناجح
                return HttpResponseRedirect('/form/')  # توجيه المستخدم إلى صفحة الفورم بعد الدفع
                
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"status": "received"}, status=200)
