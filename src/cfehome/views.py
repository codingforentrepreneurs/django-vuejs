from django.http import JsonResponse
from django.shortcuts import render


def home_view(request):
    return render(request, "home.html", {"files_": []})



def api_content_list_view(request):
    """
    Django Rest Framework -> https://cfe.sh/courses
    """
    content_list = [
        {"id": 1, "title": "Hello World"},
        {"id": 2, "title": "Hello World Again"},
    ] # -> json.dumps(content_list)
    return JsonResponse({"data": content_list})