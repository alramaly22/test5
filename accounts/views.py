from django.shortcuts import render
from django.http import JsonResponse
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

            # تحقق من حالة الدفع
            payment_status = data.get("status")  # تأكد من المفتاح الصحيح في استجابة بوابة الدفع
            if payment_status == "paid":
                return JsonResponse({"redirect": "/form/"}, status=200)  # إرسال أمر التوجيه
                
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"status": "received"}, status=200)
