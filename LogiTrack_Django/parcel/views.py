from django.shortcuts import render, get_object_or_404, redirect
from .forms import ParcelForm
from .models import Parcel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ParcelSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from functools import wraps

# MongoDB lazy connection
from .mongodb import get_parcel_collection, get_user_collection


# ============================================================
# NORMAL USER ONLY
# ============================================================

def user_only(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        # Not logged in
        if not request.user.is_authenticated:
            return redirect("login")

        # Admin cannot book
        if request.user.is_staff:
            return redirect("dashboard")

        # Normal user
        return view_func(request, *args, **kwargs)

    return wrapper


# ============================================================
# ADMIN ONLY
# ============================================================

def admin_only(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        # Not logged in
        if not request.user.is_authenticated:
            return redirect("admin_login")

        # Normal user cannot access admin pages
        if not request.user.is_staff:
            return redirect("home")

        return view_func(request, *args, **kwargs)

    return wrapper


# ============================================================
# HOME PAGE
# ============================================================

def home(request):
    return render(request, "index.html")


# ============================================================
# ADD PARCEL
# NORMAL USER ONLY
# ============================================================

@user_only
def add_parcel(request):

    if request.method == "POST":

        form = ParcelForm(request.POST)

        if form.is_valid():

            parcel = form.save()

            # MongoDB connection only when required
            parcel_collection = get_parcel_collection()

            if parcel_collection:

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
                    "booking_date": parcel.booking_date.isoformat(),
                })

            return render(request, "success.html", {
                "tracking_id": parcel.tracking_id
            })

    else:

        form = ParcelForm()

    return render(request, "add_parcel.html", {
        "form": form
    })


# ============================================================
# DELETE PARCEL
# ADMIN ONLY
# ============================================================

@admin_only
def delete_parcel(request, id):

    parcel = get_object_or_404(Parcel, id=id)

    parcel.delete()

    return redirect("dashboard")


# ============================================================
# TRACK PARCEL
# NORMAL USER + ADMIN
# ============================================================

@login_required(login_url='login')
def track(request):

    if request.method == "POST":

        tracking_id = request.POST.get("tracking_id")

        try:

            parcel = Parcel.objects.get(
                tracking_id=tracking_id
            )

            return render(request, "tracking.html", {
                "parcel": parcel
            })

        except Parcel.DoesNotExist:

            return render(request, "tracking.html", {
                "error": "Tracking ID Not Found!"
            })

    return render(request, "track.html")


# ============================================================
# ADMIN DASHBOARD
# ADMIN ONLY
# ============================================================

@admin_only
def dashboard(request):

    query = request.GET.get("q")

    parcels = Parcel.objects.all().order_by("-booking_date")

    if query:

        parcels = parcels.filter(
            tracking_id__icontains=query
        )

    total = Parcel.objects.count()

    booked = Parcel.objects.filter(
        status="Booked"
    ).count()

    transit = Parcel.objects.filter(
        status="In Transit"
    ).count()

    delivered = Parcel.objects.filter(
        status="Delivered"
    ).count()

    return render(request, "dashboard.html", {

        "parcels": parcels,

        "total": total,

        "booked": booked,

        "transit": transit,

        "delivered": delivered,

    })


# ============================================================
# UPDATE PARCEL STATUS
# ADMIN ONLY
# ============================================================

@admin_only
def update_status(request, id):

    parcel = get_object_or_404(Parcel, id=id)

    if request.method == "POST":

        parcel.status = request.POST.get("status")

        parcel.save()

    return redirect("dashboard")


# ============================================================
# PARCEL API
# ============================================================

@api_view(["GET"])
def parcel_api(request):

    parcels = Parcel.objects.all()

    serializer = ParcelSerializer(
        parcels,
        many=True
    )

    return Response(serializer.data)


# ============================================================
# ADMIN LOGIN
# ============================================================

def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Only Admin can login"
            )

    return render(
        request,
        "admin_login.html"
    )


# ============================================================
# LOGOUT
# ============================================================

def admin_logout(request):

    logout(request)

    return redirect("home")


# ============================================================
# USER SIGNUP
# ============================================================

def signup(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # MongoDB connection only during signup
        user_collection = get_user_collection()

        if user_collection:

            user_collection.insert_one({
                "username": username,
                "email": email
            })

        return redirect("login")

    return render(
        request,
        "signup.html"
    )


# ============================================================
# USER LOGIN
# ============================================================

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("home")

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(
        request,
        "login.html"
    )