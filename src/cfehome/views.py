from django.shortcuts import render


def home_view(request):
    return render(request, "home.html", {"files_": []})