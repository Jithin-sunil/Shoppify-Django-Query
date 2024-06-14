from django.shortcuts import render,redirect
from Shoppify.db_utils import *
from Guest.models import *
# Create your views here.
def user(request):
    if request.method == 'POST':
        name = request.POST.get('txt_name')
        email = request.POST.get('txt_email')
        contact = request.POST.get('txt_contact')
        password = request.POST.get('txt_password')
        address = request.POST.get('txt_address')
        photo=request.FILES.get('file_photo')
        insert_record(
                'Guest_tbl_user',
                ['username', 'useremail', 'usercontact', 'userpassword', 'useraddress', 'userphoto'],
                [name, email, contact, password, address, photo]
            )
        return redirect('Guest:user')
    else:
        return render(request,'Guest/UserRegistration.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('txt_email')
        password = request.POST.get('txt_password')
        user = fetch_records_by_fields('Guest_tbl_user', ['useremail', 'userpassword'], [email, password])
        admin= fetch_records_by_fields('Admin_tbl_admin',['admin_email', 'admin_password'], [email, password])
        if user and user['userpassword'] == password:
            request.session['user_id'] = user['id']
            request.session['user_name'] = user['username']
            return redirect('User:home')
        elif admin and admin['admin_password'] == password:
            request.session['admin_id'] = admin['id']
            request.session['admin_name'] = admin['admin_name']
            return redirect('Admin:home') 
        else:
            return render(request, 'Guest/Login.html',{'msg':'Invalid password'})
    return render(request, 'Guest/Login.html',{'msg1':'invalid username or password'})