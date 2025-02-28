from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

def home(request):
    return HttpResponse("Hello world!")

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")


# Test this view using "http://127.0.0.1:8000/classroom/Math/"
def retrive_classroom(request, class_name):
    print("i have entered the retrive_classroom view!")
    students = [
        {"name": "Nada", "age": 20},
        {"name": "Salwa", "age": 25},
        {"name": "Ahmed", "age": 24}
    ]

    subjects = [
        {"name": "Math", "teacher": "Salma"},
        {"name": "Arabic", "teacher": "Nada"},
        {"name": "History", "teacher": "Mahmoud"}
    ]

    context = {
        "title": class_name,
        "description": "This is a description for the classroom" * 100,  # Long text for filtering
        "students": students,
        "subjects": subjects,
    }
    return render(request, "index.html", context)

def calculate_area(request):
    """Endpoint to calculate area from query parameters"""
    try:
        width = float(request.GET.get("width", 0))
        height = float(request.GET.get("height", 0))
        length = float(request.GET.get("length", 0))
        area = width * height * length
        return JsonResponse({"area": area})
    except ValueError:
        return JsonResponse({"error": "Invalid input"}, status=400)
