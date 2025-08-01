from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Account


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


@login_required
def accounts_view(request):
    try:
        account = Account.objects.get(user=request.user)
        return render(request, 'accounts/accounts.html', {'account': account})
    except Account.DoesNotExist:
        messages.error(request, 'No account found for this user.')
        return render(request, 'accounts/accounts.html', {'account': None})
