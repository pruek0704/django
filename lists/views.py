from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.

def home_page(request):
    # หน้า Home มีหน้าที่แค่แสดงผลครับ ไม่ต้องรับ POST ที่นี่แล้ว
    # เพราะ Form เราส่งไปที่ /lists/new
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": our_list})

def new_list(request):
    # 1. สร้าง List ใหม่
    nulist = List.objects.create()

    # 2. รับค่า Priority (และจัดการค่าว่างให้เป็น 'Medium')
    priority_input = request.POST.get('priority', '')
    if priority_input == '':
        priority_input = 'Medium' # บังคับตัว M ใหญ่

    # 3. บันทึก Item ลง DB
    Item.objects.create(
        text=request.POST["item_text"], 
        list=nulist,
        priority=priority_input # ส่งค่าที่จัดการแล้วเข้าไป
    )
    return redirect(f"/lists/{nulist.id}/")

def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)

    # 1. รับค่า Priority (และจัดการค่าว่างให้เป็น 'Medium')
    priority_input = request.POST.get('priority', '')
    if priority_input == '':
        priority_input = 'Medium' # บังคับตัว M ใหญ่

    # 2. บันทึก Item ลง DB
    Item.objects.create(
        text=request.POST["item_text"], 
        list=our_list,
        priority=priority_input  
    )
    return redirect(f"/lists/{our_list.id}/")