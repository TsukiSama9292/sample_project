from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone


def index(request):
    context = {'title': '這是網頁標題', 'message': '這是網頁內容'}
    return render(request, 'ai/index.html', context)


def trigger(request):
    """Simple API view that returns a JSON response when triggered from the UI.

    Uses GET so the front-end can call it without dealing with CSRF in this demo.
    """
    now = timezone.now()
    data = {
        'status': 'ok',
        'message': '按鈕觸發成功',
        'time': now.isoformat(),
    }
    return JsonResponse(data)