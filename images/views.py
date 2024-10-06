
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer
import random
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


@login_required
def image_list(request):
    images = Image.objects.all()
    return render(request, "image_list.html", {"images": images})


@login_required
def download_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    response = FileResponse(
        image.image.open(), as_attachment=True
    )  # Ensure image is opened properly
    return response


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def random_image(request):
    count = Image.objects.count()
    if count == 0:
        return Response({"error": "No images available"}, status=404)

    random_index = random.randint(0, count - 1)
    image = Image.objects.all()[random_index]
    serializer = ImageSerializer(image)
    return Response(serializer.data)


@login_required
def profile_view(request):
    return render(request, "profile.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("image_list")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("image_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
