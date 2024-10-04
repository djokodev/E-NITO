from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product, Cart, Order
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    query = request.GET.get("q")  # Récupérer la recherche de l'utilisateur
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query)
        )  # Filtrer selon la recherche

    paginator = Paginator(products, 6)  # Appliquer la pagination après le filtrage
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "store/home.html",
        context={"products": page_obj, "page_obj": page_obj, "query": query},
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "store/detail.html", context={"product": product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(
        user=user, ordered=False, product=product
    )

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, "store/cart.html", context={"orders": cart.orders.all()})


def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()

    return redirect("home")
