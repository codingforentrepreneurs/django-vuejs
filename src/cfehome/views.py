import json
from django.http import JsonResponse
from django.shortcuts import render

from contents.forms import ContentForm
from contents.models import Content

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


def api_content_create_view(request):
    if not request.method == "POST":
        return JsonResponse({}, status=400)
    data = {}
    try:
        data = json.loads(request.body)
    except:
        pass
    print(data)
    title = data.get('title') or None
    if 'abc' in title:
        return JsonResponse({'detail': f"{title} is invalid. please remove abc."}, status=400)
    form = ContentForm(data)
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj, request.user)
        obj.save()
        data = {
            "id": obj.id,
            "title": obj.title,
            "isCreated":True,
            "content": obj.content
        }
        return JsonResponse(data, status=201)
    errors = json.loads(form.errors.as_json())
    return JsonResponse(errors, status=400)