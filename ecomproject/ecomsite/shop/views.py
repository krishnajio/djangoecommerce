from django.shortcuts import render
from .models import Products,Order,OrderUpdate
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from users.gmod import Userdata
# Create your views here.
username= "" 
def index(request):
    product_objects = Products.objects.all()
     #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
 
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request,'shop/default.html',{'product_objects':product_objects})
 
 
def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})
    
def checkout(request):
    if request.method == "POST":
        print(Userdata.cuserid)
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state =request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        user = User.objects.get(id=Userdata.cuserid)
                
        order = Order(items=items,name=name,email=email,address=address,
                city=city,state=state,zipcode=zipcode,total=total)
        order.user_name = user
        order.save()
              
        update = OrderUpdate(order_id=order.id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request,'shop/checkout.html')
