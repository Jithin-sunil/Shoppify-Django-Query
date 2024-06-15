from django.shortcuts import render,redirect
from django.contrib import messages
from Shoppify.db_utils import *
from Guest.models import *
# Create your views here.
def home(request):
    return render(request,'User/HomePage.html')


def myprofile(request):
    # user_id=request.session['user_id']
    user=fetch_record_by_id("Guest_tbl_user",request.session['user_id']) 
    return render(request,'User/MyProfile.html',{'user':user})


def editprofile(request):
    user_id=request.session['user_id']
    user=fetch_record_by_id("Guest_tbl_user",user_id)
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        update_record("Guest_tbl_user",['username','useremail','usercontact','useraddress'],[name,email,contact,address],user_id)
        return render(request, 'User/EditProfile.html',{'msg':'Profile has been updated'})
    else:
        return render(request,'User/EditProfile.html',{'user':user})



def changepassword(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = fetch_record_by_id("Guest_tbl_user", user_id)
        dbpassword = user['userpassword']
        currentpassword = request.POST.get('txt_curpass')
        newpassword = request.POST.get('txt_newpass')
        repass = request.POST.get('txt_repass')
        if dbpassword == currentpassword:
            if newpassword == repass:
                update_record("Guest_tbl_user", ['userpassword'], [newpassword], user_id)
                return render(request, 'User/ChangePassword.html',{'msg':'Password updated successfully'})
            else:
                return render(request, 'User/ChangePassword.html', {'msg1': 'Password Mismatch'})
        else:
            return render(request, 'User/ChangePassword.html', {'msg2': 'Invalid Password'})   
    else:
        return render(request, 'User/ChangePassword.html')