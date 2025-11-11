from django.shortcuts import render

def index(request):
    context = {'title': '這是網頁標題', 'message': '這是網頁內容'}
    return render(request, 'ai/index.html', context)