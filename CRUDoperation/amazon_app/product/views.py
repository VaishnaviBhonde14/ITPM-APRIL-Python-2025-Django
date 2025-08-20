from django.shortcuts import render,redirect,get_object_or_404
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()

    return render(request, 'product/product_list.html',{'products':products})

#Add a product
def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name = request.POST['name'],
            price = request.POST['price'],
            description = request.POST['description'],
            stock = request.POST['stock'],
        )

        return redirect('product_list')
    return render(request,'product/add_product.html') #it takes html file ad_product.html from

#Edit an existing product
def edit_product(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.stock = request.POST['stock']
        product.save()
        return redirect('product_list')
    return render(request,'product/edit_product.html',{'product':product})


#Delete a product
def delete_product(request,id):
    product = get_object_or_404(Product , id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product/delete_product.html', {'product': product})

