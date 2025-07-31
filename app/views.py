


from django.shortcuts import render

from app.models import Plan_info


# Create your views here.
def index(request):
    if request.method == "GET":
        destination = request.GET.get('destination')
        tour_type = request.GET.get('tour_type')

        matching_trips= Plan_info.objects.all()

        if destination:
            matching_trips = matching_trips.filter(destination__icontains=destination)
        if tour_type:
            matching_trips = matching_trips.filter(tour_type__icontains=tour_type)
        context = {
            'trips':matching_trips,
        }
    return render(request, 'index.html',context)
