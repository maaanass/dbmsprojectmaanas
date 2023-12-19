

from django.shortcuts import render, redirect
from django.contrib import messages
from mydb.models import members,employee,adminlogin
from .forms import employeeForm
from .forms import memberForm

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

def member_reset_password(request, user_id):
    if request.method == 'POST':
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        try:
            user = members.objects.get(id=user_id)

            if new_password == confirm_new_password :
                # Update the password in the database
                user.password = new_password
                user.save()
                messages.success(request, 'Password reset successfully.')
            else:
                messages.error(request, 'New password and confirm password do not match. Please try again.')

        except members.DoesNotExist:
            messages.error(request, 'User not found.')

    return render(request, 'member_reset_password_page.html', {'user_id': user_id})

def trainer_login(request):
    if request.method =='POST':
        e_id=request.POST['e_id']
        password=request.POST['password']

        try:
            if e_id.startswith('e'):
                user=employee.objects.get(e_id=e_id,password=password)
                return redirect('trainer_success',user_id=user.id)
            else:
                messages.error(request,'Invalid Credentials. Please Try Again.')
        except employee.DoesNotExist:
            messages.error(request,'Invalid Credentials. Please Try Again.')

    return render(request,'elogin.html')


def trainer_success(request,user_id):
    try:
        user=employee.objects.get(id=user_id)
        context={'user':user}
        members = user.members.all()
        context = {'user': user, 'members': members}
        return render(request,'esuccess.html',context)
    except employee.DoesNotExist:
       return render(request,'error_page.html')


def trainer_reset_password_page(request,user_id):
    return render(request,'trainer_reset_password_page.html',{'user_id':user_id})

def reset_password(request,user_id):
    if request.method=='POST':
        new_password=request.POST['new_password']
        confirm_new_password=request.POST['confirm_new_password']

        try:
            user=employee.objects.get(id=user_id)

            if new_password==confirm_new_password:
                user.password=new_password
                user.save()
                messages.success(request,'Password Reset Sucessfully.')
            else:
                messages.error(request,'New Password And Confirm Password Do Not Match. Please Try Again.')
        except employee.DoesNotExist:
            messages.error(request,'User Not Found')
        
    return render(request,'trainer_reset_password_page.html',{'user_id':user_id})

def employee_list(request):
    employees = employee.objects.all()
    form = employeeForm()

    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')

    return render(request, 'employee_list.html', {'employees': employees, 'form': form})

def delete_employee(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        employee.objects.filter(id__in=selected_ids).delete()
        return redirect('employee_list')

def update_employee(request, employee_id):
    employee_instance = employee.objects.get(id=employee_id)
    form = employeeForm(instance=employee_instance)

    if request.method == 'POST':
        form = employeeForm(request.POST, instance=employee_instance)
        if form.is_valid():
            form.save()
            return redirect('update_employee_confirm', employee_id=employee_id)

    return render(request, 'update_employee.html', {'form': form, 'employee_id': employee_id})

def update_employee_confirm(request, employee_id):
    employee_instance = employee.objects.get(id=employee_id)

    if request.method == 'POST':
        form = employeeForm(request.POST, instance=employee_instance)
        if form.is_valid():
            form.save()
            return redirect('employee_list')

    return render(request, 'update_employee_confirm.html', {'form': employeeForm(instance=employee_instance)})

#member views
def members_list(request):
    member = members.objects.all()
    form = memberForm()

    if request.method == 'POST':
        form = memberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_list')

    return render(request, 'members_list.html', {'member': member, 'form': form})

def delete_members(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        members.objects.filter(id__in=selected_ids).delete()
        return redirect('members_list')

def update_members(request, members_id):
    memberr_instance = members.objects.get(id=members_id)
    form = memberForm(instance=memberr_instance)

    if request.method == 'POST':
        form = memberForm(request.POST, instance=memberr_instance)
        if form.is_valid():
            form.save()
            return redirect('update_members_confirm', members_id=members_id)


    return render(request, 'update_members.html', {'form': form, 'members_id': members_id})


def update_members_confirm(request, members_id):
    memberr_instance = members.objects.get(id=members_id)

    if request.method == 'POST':
        form = memberForm(request.POST, instance=memberr_instance)
        if form.is_valid():
            form.save()
            return redirect('members_list')


    return render(request, 'update_members_confirm.html', {'form': memberForm(instance=memberr_instance)})

def adminsucess(request):
    return render(request, 'adminsuccess.html')
