from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,SignUpForm
from .forms import CustomerProfileView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect
from .models import CartItem
from .forms import CartItemForm


class ProductView(View):
 def get(self,req):
  topwear = Product.objects.filter(category='TW')
  bottomwear = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  return render(req, 'app/home.html',{'topwears':topwear,'bottomwear':bottomwear,'mobiles':mobiles,})

class ProductDetailView(View):
 def get(self,request,pk):
  product=Product.objects.get(pk=pk)
  return render(request,'app/productdetail.html',{'product':product})



#def add_to_cart(request,pk):
  #v=Product.objects.get(pk=pk)
  #return render(request, 'app/buynow.html',{'v':v})
    # Logic to add the product to the cart, such as using session or a shopping cart model.
    # Here, we assume you have a session-based cart implementation.
    #cart = request.session.get('cart', {})  # Retrieve the cart from the session
    # Add the product to the cart dictionary with quantity as value
    #cart[product.id] = cart.get(product.id, 0) + 1
    #request.session['cart'] = cart  # Update the cart in the session
    #return redirect('cart')   Redirect to the cart page after adding the product
  

def buy_now(request):
 return render(request, 'app/buynow.html')

def cart_to(request):
  cart_items = CartItem.objects.filter(user=request.user)
  return render(request, 'app/cart2.html', {'cart_items': cart_items})

  #cart_count = CartItem.objects.filter(user=user).count()
  #cart_item = CartItem.objects.filter(Product)
  #return render(request, 'app/addtocart.html', {'cart_item':cart_item,'current_user': request.user,'cart_count': cart_count})


#---------add_to_cart------------------------------------------------------------------------------
def add_to_cart(request, pk):
    product =Product.objects.get(pk=pk)
    print(product)
    user = request.user
    
    # Check if the item already exists in the cart
    cart_item = CartItem.objects.filter(user=user,product=product).first()                #.first()
    print(cart_item)
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartItem(user=user,product=product)
        cart_item.save()

    return render(request, 'app/addtocart.html',{'cart_item':cart_item})
#------------------------------------------------------------------------------------------

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')


#------Logout Section--------------------------------------------------------
def log_out(request):
    logout(request)
    return render(request, 'app/login.html')
#---------------------------------------------------------------------------------

#------Log In Page-----------------------------------------------


def log_in(request):
  if request.method=='POST':
    fm=LoginForm(request=request,data=request.POST)
    if fm.is_valid():
      username=fm.cleaned_data['username']
      passw=fm.cleaned_data['password']
      user= authenticate(username=username,password=passw)
      if user is not None:
        login(request, user)
        #return redirect('home')
        return render(request,'app/home.html',{'current_user':request.user})
  else:
    fm=LoginForm()
    return render(request, 'app/login.html',{'fm':fm})

#----------User name display trial---------------------------------------
def tv(request):
  if request.method=='GET':
    id=request.user.id
    user=User.objects.get(pk=id) 
    return render(request,'app/tv.html',{'user':user}) 
#------------------------------------------------------------------------

#----------User Profile---------------------------------------
# def profile(request):
#     if request.method=='GET':
#         id=request.user.id
#         user=User.objects.get(pk=id)
#         return render(request,'app/profile.html',{'user':user})       
#     else:
#         form=CustomerProfileView()
#         id=request.user.id
#         user=User.objects.get(pk=id)  
#     return render(request,'app/profile.html',{'form':form})

def profile(request):
    if request.method=='GET':
        user = request.user
        return render(request, 'app/profile.html', {'user': user})
#-------------------------------------------------------------------------------

#------Customer Registration-----------------------------------------------
def customer_registration(request):
 # step-1 sign up form
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'app/customerregistration.html')
    else:
        fm=SignUpForm()
    return render(request, 'app/customerregistration.html',{'fm':fm})
#-------------------------------------------------------------------------------



#----------Home all Items --------------------------------------------------------
def home(req):
    return render(req,'app1/index.html')
#---------------------------------------------------------------------------------

#----------Fashion items----------------------------------------------------------
def fashion(request,data=None):
  if data==None:
    fashion1 = Product.objects.filter(category='TW')
    fashion2 = Product.objects.filter(category='BW')
  elif data=='topwear':
    fashion1 = Product.objects.filter(category='TW')
    return render(request, 'app/fashion.html',{'fashion1':fashion1})
    #grocery = Product.objects.filter(category='G').filter(brand=data)
  return render(request, 'app/fashion.html',{'fashion1':fashion1,'fashion2':fashion2})
#----------------------------------------------------------------------------------
#------Beauty Product-------------------------------------------------------------------
def beauty(request,data=None):
  if data==None:
    beauty_product= Product.objects.filter(category='B')
  return render(request, 'app/beauti.html',{'beauty_product':beauty_product})
#----------------------------------------------------------------------------------
#------Electronic Product-------------------------------------------------------------------
def electronics(request,data=None):
  if data==None:
    electronics = Product.objects.filter(category='E')
  return render(request, 'app/electronics.html',{'electronics':electronics})
#----------------------------------------------------------------------------------
#------Best Deals-------------------------------------------------------------------
def best_deal(request,data=None):
  if data==None:
    offer = Product.objects.filter(category='D')
  return render(request, 'app/best_offer.html',{'offer':offer})
#----------------------------------------------------------------------------------
#------home decorator-------------------------------------------------------------------
def home_decorator(request,data=None):
  if data==None:
    decorate = Product.objects.filter(category='H')
  return render(request, 'app/home_decorator.html',{'decorate':decorate})
#----------------------------------------------------------------------------------
#----------Tv & applinces---------------------------------------------------------------
def tv_applinces(request,data=None):
  if data==None:
    applinces = Product.objects.filter(category='A')
  return render(request, 'app/applinces.html',{'applinces':applinces})
#----------------------------------------------------------------------------------------
#----------Furniture---------------------------------------------------------------
def furniture(request,data=None):
  if data==None:
    furniture = Product.objects.filter(category='F')
  return render(request, 'app/furniture.html',{'furniture':furniture})
#----------------------------------------------------------------------------------------

#------Grocery---------------------------------------------------------------------------
def grocery(request,data=None):
  if data==None:
    grocery = Product.objects.filter(category='G')
  elif data=='Redmi' or data=='Samsung':
    grocery = Product.objects.filter(category='G').filter(brand=data)
  return render(request, 'app/grocery.html',{'grocery':grocery})
#----------------------------------------------------------------------------------------

#--------Mobile-----------------------------------------------------------------
def mobile(request,data=None):
 if data==None:
    mobiles = Product.objects.filter(category='M')
 elif data=='Redmi' or data=='Samsung':
    mobiles = Product.objects.filter(category='M').filter(brand=data)
 return render(request, 'app/mobile.html',{'mobiles':mobiles})
#----------------------------------------------------------------------------------------

#----Checkout---------------------------------------------------------------------------
def checkout(request):
 return render(request, 'app/checkout.html')

#------------------------------------------------------------------------


