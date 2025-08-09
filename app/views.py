from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import requests
from django.shortcuts import render, redirect


from app.models import Plan_info


# Create your views here.
def index(request):

    return render(request, 'index.html')

@login_required()
def add_trip(request):

    if request.method == "POST":
        destination = request.POST.get('destination')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        adults = request.POST.get('adults')
        children = request.POST.get('children')
        tour_type = request.POST.get('tour_type')
        image = request.FILES.get('image')  # Must come from FILES, not POST

        Plan_info.objects.create(
            destination=destination,
            departure_date=departure_date,
            return_date=return_date,
            adults=adults,
            children=children,
            tour_type=tour_type,
            image=image
        )

    return render(request, 'add_trip.html')
# def results(request):
#     matching_trips = Plan_info.objects.all()
#
#     if request.method == "GET":
#         destination = request.GET.get('destination')
#         tour_type = request.GET.get('tour_type')
#
#         if destination:
#             matching_trips = matching_trips.filter(destination__icontains=destination)
#         if tour_type:
#             matching_trips = matching_trips.filter(tour_type__icontains=tour_type)
#
#     context = {
#         'trips': matching_trips,
#     }
#     return render(request, 'results.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_trip')
        else:
            return render(request, 'login.html')
    return render(request,'login.html')

def kenya_flights(request):
    API_KEY = "abd898207de884b15aad119a70b33858"
    url = f"http://api.aviationstack.com/v1/flights?airline_iata=KQ&access_key={API_KEY}"
    response = requests.get(url).json()

    flights = response.get("data", [])
    return render(request, "flights.html", {"flights": flights})

def results(request):
    matching_trips = Plan_info.objects.all()

    if request.method == "GET":
        departure_city = request.GET.get('departure_city', 'NBO')  # Default Nairobi
        destination = request.GET.get('destination', 'MBA')  # Default Mombasa
        tour_type = request.GET.get('tour_type')
        departure_date = request.GET.get('checkin')
        return_date = request.GET.get('checkout')

        if destination:
            matching_trips = matching_trips.filter(destination__icontains=destination)
        if tour_type:
            matching_trips = matching_trips.filter(tour_type__icontains=tour_type)

    API_KEY = "abd898207de884b15aad119a70b33858"
    base_url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "dep_iata": departure_city,
        "arr_iata": destination,
        "flight_date": departure_date
    }

    flight_data = []
    try:
        r = requests.get(base_url, params=params)
        data = r.json()
        flight_data = data.get("data", [])
    except Exception as e:
        print("Flight API error:", e)

    context = {
        "trips": matching_trips,
        "flights": flight_data,
        "destination": destination,
        "departure_city": departure_city,
        "departure_date": departure_date,
        "return_date": return_date,
    }

    return render(request, "results.html", context)
