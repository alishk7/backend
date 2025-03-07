from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# Create your views here.
