from django.shortcuts import render, redirect

from shop_main.forms import CommentForm
from shop_main.models import Product
from django.shortcuts import get_object_or_404


def home_page(request):
    filter_type = request.GET.get('filter', '')
    if filter_type == 'Popular items':
        products = Product.objects.all().order_by('-rating')[:4]
    elif filter_type == 'New Arrivals':
        products = Product.objects.all().order_by('-id')
    elif filter_type == 'Cheap':
        products = Product.objects.all().order_by('old_price')
    elif filter_type == 'Expensive':
        products = Product.objects.all().order_by('-old_price')
    elif filter_type == 'Likes':
        products = Product.objects.all().order_by('-rating')
    else:
        products = Product.objects.all()

    rating_range = list(range(1, 6))
    context = {
        'products': products,
        'rating_range': rating_range,
    }
    return render(request, template_name='home.html', context=context)


def detail_view(request, _id):
    product = Product.objects.get(pk=_id)
    related_products = Product.objects.all().exclude(id=product.id)
    comments = product.comments.all().order_by('-created_at')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.product_id = _id
            comment.save()
            return redirect('detail', _id)



    context = {
        'form':form ,
        'related_products': related_products,
        'product': product,
        'comments': comments,
    }
    return render(request, 'detail.html', context)


