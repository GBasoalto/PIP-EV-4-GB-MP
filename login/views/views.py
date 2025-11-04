
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user = request.user
    groups = user.groups.all()
    return render(request, 'home/index.html', {
        'title': 'Bienvenido',
        'user': user,
        'groups': groups,
    })
