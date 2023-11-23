

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import members

def login(request):
    if request.method == 'POST':
        m_id = request.POST['m_id']
        password = request.POST['password']

        try:
            user = members.objects.get(m_id=m_id, password=password)
            messages.success(request, 'Successfully logged in!')
            return redirect('success_page', user_id=user.id)  # Pass user_id to success_page
        except members.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html')
def success_page(request, user_id):
    try:
        user = members.objects.get(id=user_id)
        context = {'user': user}
        return render(request, 'success_page.html', context)
    except members.DoesNotExist:
        # Handle the case where the user with the given user_id doesn't exist
        return render(request, 'error_page.html')

