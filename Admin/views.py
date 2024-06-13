
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
    places = fetch_joined_records("Admin_tbl_place", "Admin_tbl_district", "Admin_tbl_place.district_id = Admin_tbl_district.id")
    district = fetch_all_records("Admin_tbl_district")
    if request.method == 'POST':
        place_name = request.POST.get('txt_place')
        district_id = request.POST.get('sel_district')
        insert_record('Admin_tbl_place', ['place_name','district_id'], [place_name,district_id])
        return redirect('Admin:place')
    else:
        # print(place)
        return render(request, 'Admin/Place.html',{'place': place,'districts':district})