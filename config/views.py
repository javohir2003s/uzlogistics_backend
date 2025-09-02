from django.shortcuts import render

def map_view(request):
    return render(request, "yandex_map.html")
