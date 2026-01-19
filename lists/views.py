from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item, List
# Create your views here.

def home_page(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        # [NEW] รับค่า priority
        priority_level = request.POST.get('priority', 'medium') 
        
        Item.objects.create(
            text=request.POST['item_text'], 
            list=list_,
            priority=priority_level # [NEW] บันทึกลง DB
        )
        return redirect(f'/lists/{list_.id}/')
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": our_list})

def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=nulist)
    return redirect(f"/lists/{nulist.id}/")

def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(
        text=request.POST["item_text"], 
        list=our_list,
        priority=request.POST['priority']  
    )
    return redirect(f"/lists/{our_list.id}/")