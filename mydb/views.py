

from django.shortcuts import render, redirect
from django.contrib import messages
from mydb.models import members,employee,adminlogin

def login(request):
    if request.method == 'POST':
        m_id = request.POST['m_id']
        password = request.POST['password']

        try:
            if m_id.startswith('m'):
                user = members.objects.get(m_id=m_id, password=password)
                #messages.success(request, 'Successfully logged in!')
                return redirect('success_page', user_id=user.id)  # Pass user_id to success_page
            else:
               messages.error(request, 'Invalid credentials. Please try again.')
               
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

def adminredirect(request):
    return render(request,'adminlogin.html')

def adminloginpage(request):
    if request.method == 'POST':
        a_id = request.POST['a_id']
        password = request.POST['password']

        try:
            if a_id.startswith('a'):
                user = adminlogin.objects.get(a_id=a_id, password=password)
                #messages.success(request, 'Successfully logged in!')
                return redirect('admin_success_page', user_id=user.id)  # Pass user_id to success_page
            else:
               messages.error(request, 'Invalid credentials. Please try again.')
  
        except adminlogin.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
            
        return render(request,'adminlogin.html')

def admin_success_page(request, user_id):
    try:
        user = adminlogin.objects.get(id=user_id)
        context = {'user': user}
        return render(request, 'adminsuccess.html', context)
    except adminlogin.DoesNotExist:
        # Handle the case where the user with the given user_id doesn't exist
        return render(request, 'error_page.html')
    
def member_reset_password_page(request, user_id):
    return render(request, 'member_reset_password_page.html', {'user_id': user_id})

def reset_password(request, user_id):
    if request.method == 'POST':
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        try:
            user = members.objects.get(id=user_id)

            if new_password == confirm_new_password:
                # Update the password in the database
                user.password = new_password
                user.save()
                messages.success(request, 'Password reset successfully.')
            else:
                messages.error(request, 'New password and confirm password do not match. Please try again.')

        except members.DoesNotExist:
            messages.error(request, 'User not found.')

    return render(request, 'member_reset_password_page.html', {'user_id': user_id})
