from django.shortcuts import render
from .forms import ParcelForm
from .models import Parcel
from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParcelSerializer
from .mongodb import parcel_collection
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Home Page
def home(request):
    return render(request, "index.html")


# Add Parcel Page
def add_parcel(request):

    if request.method == "POST":

        form = ParcelForm(request.POST)

        if form.is_valid():

            parcel = form.save()

            parcel_collection.insert_one({
                "tracking_id": parcel.tracking_id,
                "sender_name": parcel.sender_name,
                "sender_phone": parcel.sender_phone,
                "sender_address": parcel.sender_address,
                "receiver_name": parcel.receiver_name,
                "receiver_phone": parcel.receiver_phone,
                "receiver_address": parcel.receiver_address,
                "parcel_type": parcel.parcel_type,
                "weight": parcel.weight,
                "status": parcel.status,
            })

            return render(request, "success.html", {
                "tracking_id": parcel.tracking_id
            })

    else:
        form = ParcelForm()

    return render(request, "add_parcel.html", {
        "form": form
    })

# Tracking Page
def track(request):

    if request.method == "POST":

        tracking_id = request.POST.get("tracking_id")

        try:

            parcel = Parcel.objects.get(tracking_id=tracking_id)

            return render(request, "tracking.html", {
                "parcel": parcel
            })

        except Parcel.DoesNotExist:

            return render(request, "tracking.html", {
                "error": "Tracking ID Not Found!"
            })

    return render(request, "track.html")


# Dashboard
@login_required(login_url='admin_login')
def dashboard(request):
    query = request.GET.get("q")

    parcels = Parcel.objects.all().order_by("-booking_date")

    if query:
       parcels = parcels.filter(tracking_id__icontains=query)


    total = Parcel.objects.count()
    booked = Parcel.objects.filter(status="Booked").count()
    transit = Parcel.objects.filter(status="In Transit").count()
    delivered = Parcel.objects.filter(status="Delivered").count()

    return render(request, "dashboard.html", {
        "parcels": parcels,
        "total": total,
        "booked": booked,
        "transit": transit,
        "delivered": delivered,
    })

@login_required(login_url='admin_login')
def update_status(request, id):

    parcel = get_object_or_404(Parcel, id=id)

    if request.method == "POST":
        parcel.status = request.POST.get("status")
        parcel.save()

    return redirect("dashboard")

@api_view(["GET"])
def parcel_api(request):

    parcels = Parcel.objects.all()

    serializer = ParcelSerializer(parcels, many=True)

    return Response(serializer.data)

def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(request, "admin_login.html", {
            "error": "Invalid Username or Password"
        })

    return render(request, "admin_login.html")

def admin_logout(request):
    logout(request)
    return redirect("home")

def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "admin_login.html")

def logout_view(request):
    logout(request)
    return redirect("home")