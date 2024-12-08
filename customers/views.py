from django.shortcuts import render
from .models import Lead

# Параметры представлений (views) - это настройки того, 
# как данные будут отображаться и обрабатываться

# gpt порекомендовал такой код
def lead_list(request):
    leads = Lead.objects.all()  # получаем все записи
    return render(request, 'leads/lead_list.html', {'leads': leads})