
from django.shortcuts import render,redirect
from Shoppify.db_utils import *
from Admin.models import *

def district(request):
    district = fetch_all_records("Admin_tbl_district")
    if request.method == 'POST':
        district_name = request.POST.get('txt_district')
        insert_record('Admin_tbl_district', ['district_name'], [district_name])
        return redirect('Admin:district')
    else:
        return render(request, 'Admin/District.html',{'district': district})


def deldistrict(request,did):
    delete_record("Admin_tbl_district",did)
    return redirect('Admin:district')


def editdistrict(request,eid):
    district = fetch_record_by_id("Admin_tbl_district",eid)
    if request.method == 'POST':
        district_name = request.POST.get('txt_district')

        update_record("Admin_tbl_district",['district_name'],[district_name],eid)
        return redirect('Admin:district')
    else:
        return render(request, 'Admin/District.html', {'districtdata': district})


def place(request):
    place =  fetch_joined_records(
        "p.id as id, p.place_name, d.id as district_id, d.district_name",
        "Admin_tbl_place p",
        "Admin_tbl_district d",
        "p.district_id = d.id"
    )
    district = fetch_all_records("Admin_tbl_district")
    if request.method == 'POST':
        place_name = request.POST.get('txt_place')
        district_id = request.POST.get('sel_district')
        insert_record('Admin_tbl_place', ['place_name','district_id'], [place_name,district_id])    
        return redirect('Admin:place')
    else:
        # print(place)
        return render(request, 'Admin/Place.html',{'place': place,'districts':district})


def delplace(request,pid):
    delete_record("Admin_tbl_place",pid)
    return redirect('Admin:place')

def editplace(request,eid):
    place = fetch_record_by_id("Admin_tbl_place",eid)
    district = fetch_all_records("Admin_tbl_district")
    if request.method == 'POST':
        place_name = request.POST.get('txt_place')
        district_id = request.POST.get('sel_district')
        update_record("Admin_tbl_place",['place_name','district_id'],[place_name,district_id],eid)
        return redirect('Admin:place')
    else:
        # print(place)
        return render(request, 'Admin/Place.html', {'placedata': place,'districts':district})


def category(request):
    category = fetch_all_records("Admin_tbl_category")
    if request.method == 'POST':
        category_name = request.POST.get('txt_category')
        insert_record('Admin_tbl_category', ['category_name'], [category_name])
        return redirect('Admin:category')
    else:
        return render(request, 'Admin/Category.html',{'category': category})


def delcategory(request,cid):
    delete_record("Admin_tbl_category",cid)
    return redirect('Admin:category')

def editcategory(request,eid):
    category = fetch_record_by_id("Admin_tbl_category",eid)
    if request.method == 'POST':
        category_name = request.POST.get('txt_category')
        update_record("Admin_tbl_category",['category_name'],[category_name],eid)
        return redirect('Admin:category')
    else:
        return render(request, 'Admin/Category.html', {'categorydata': category})


def subcategory(request):
    subcategory = fetch_joined_records(
        "s.id as id, s.subcategory_name, c.id as category_id, c.category_name",
        "Admin_tbl_subcategory s",
        "Admin_tbl_category c",
        "s.category_id = c.id"
    )
    category = fetch_all_records("Admin_tbl_category")
    if request.method == 'POST':
        subcategory_name = request.POST.get('txt_subcategory')
        category_id = request.POST.get('sel_category')
        insert_record('Admin_tbl_subcategory', ['subcategory_name','category_id'], [subcategory_name,category_id])    
        return redirect('Admin:subcategory')
    else:
        return render(request, 'Admin/Subcategory.html',{'subcategory': subcategory,'categorys':category})


def delsubcategory(request,sid):
    delete_record("Admin_tbl_subcategory",sid)
    return redirect('Admin:subcategory')

def editsubcategory(request,eid):
    subcategory = fetch_record_by_id("Admin_tbl_subcategory",eid)
    category = fetch_all_records("Admin_tbl_category")
    if request.method == 'POST':
        subcategory_name = request.POST.get('txt_subcategory')
        category_id = request.POST.get('sel_category')
        update_record("Admin_tbl_subcategory",['subcategory_name','category_id'],[subcategory_name,category_id],eid)
        return redirect('Admin:subcategory')
    else:
        return render(request, 'Admin/Subcategory.html', {'subcategorydata': subcategory,'categorys':category})


def admin(request):
    if request.method == 'POST':
        admin_name = request.POST.get('txt_name')
        admin_email = request.POST.get('txt_email')
        admin_password = request.POST.get('txt_password')
        insert_record('Admin_tbl_admin', ['admin_name','admin_email','admin_password'], [admin_name,admin_email,admin_password])
        return redirect('Admin:admin')
    else:
        return render(request, 'Admin/AdminRegistration.html',{'admin': admin})

def home(request):
    return render(request, 'Admin/HomePage.html')