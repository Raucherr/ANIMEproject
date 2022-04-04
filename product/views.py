from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from .forms import CreateProductForm, UpdateProductForm
from .models import Category, Product

from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


# def post_detail(request, slug):
#     template_name = 'cart_detail.html'
#     product = get_object_or_404(Product, slug=slug)
#     comments = product.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.product = product
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'product': product,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})
#

# def add_comment_to_post(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.product = product
#             comment.save()
#             return redirect('detail', pk=product.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'products/add_comment_to_post.html', {'form': form})
#
#
#
