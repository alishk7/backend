from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            if Reservation.objects.filter(table=reservation.table, date=reservation.date).exixts():
                form.add_error(None, "Этот стол уже забронирован на указанную дату.")
            else:
                reservation.save()
                return redirect('reservation-list')
            
    else:
        form = ReservationForm()

    return render(request, 'reservations/create_reservation.html', {'form': form})
# Create your views here.
