from django.shortcuts import redirect, render
from .models import Customer,Product,Order
def index(request):
    user=Customer.objects.all()
    return render(request,'index.html',{'user':user})


def products(request):
    products=Product.objects.all()
    return render(request,'products.html',{'products':products})

def add(request):
    return render(request,'add.html')


def add_product(request):
    return render(request,'addProduct.html')

def order(request):
    products=Product.objects.all()
    customers=Customer.objects.all()
    return render(request,'order.html',{'customers':customers,'products':products})

   
def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        user = Customer(name=name, phone_number=phone,email=email, address=address)
        user.save()
        return redirect('index') 
    return render(request, 'add.html')



 
def add_product_service(request):
    if request.method == 'POST':
        product_name = request.POST.get('p_name')
        product_price = request.POST.get('p_price')
        product_stock = request.POST.get('p_stock')
        product_desc = request.POST.get('p_desc')
        user = Product(name=product_name, price=product_price,stock_quantity=product_stock, description=product_desc)
        user.save()
        return redirect('index') 
    return render(request, 'addProduct.html')


def delete(request,id):
    user =Customer.objects.get(id=id)
    user.delete()
    return redirect('index') 


def update(request,id):
    user =Customer.objects.get(id=id)
    return render(request,'update.html',{'user':user}) 

def uprec(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        user= Customer.objects.get(id=id)
        user.name=name
        user.phone_number=phone
        user.email=email
        user.address=address
        # user = Customer(name=name, phone_number=phone,email=email, address=address)
        user.save()
        return redirect('index') 
    return render(request, 'update.html')

def place_order(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        
        customer = Customer.objects.get(id=customer_id)
        product = Product.objects.get(id=product_id)
        
        order = Order(customer=customer, product=product, quantity=quantity, status='Pending')
        order.save()
        print(Order.objects.all())
        
        return redirect('index')  # Redirect to the index page or any other page
     