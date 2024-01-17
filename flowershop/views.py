from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.timezone import now

from .forms import CommentsForm, UserProfileCreationForm, OrderForm
from .models import Item, Comments, Category, UserProfile, Post, Order

def index(request):

    latest_post = Post.objects.order_by('-post_date').first()
    context = {'latest_post': latest_post}
    return render(request, 'flowershop/index.html', context=context)


def item(request, id=None):
    item = get_object_or_404(Item, title=id)
    comment_form=CommentsForm()
    comments = Comments.objects.filter(item=item).order_by('-publish_date')
    if request.method=="POST":
        form=CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            if request.user.is_authenticated:
                comment.author = request.user
            else:
                return redirect(reverse('signup'))
            comment.published_date = now()
            comment.save()
            return render(request, 'flowershop/item.html', context={'item':item, 'comments_form':comment_form, 'comments':comments})
    context = {"item":item, 'comments_form':comment_form, 'comments':comments}
    return render(request, 'flowershop/item.html', context=context)


def shop(request):
    items = Item.objects.all().order_by("-date")
    context = {"items": items}
    context.update(get_categories())
    return render(request, 'flowershop/shop.html', context=context)

def get_categories():
    categories = Category.objects.all()
    return{'categories':categories}

def category(request, name=None):
    c = get_object_or_404(Category, name=name)
    items = Item.objects.filter(category=c)
    context = {
        'items': items
    }
    context.update(get_categories())
    return render(request, 'flowershop/shop.html', context=context)

def user_logout(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            UserProfile.objects.create(user=user, phone=form.cleaned_data['phone'], dateofbirth=form.cleaned_data['dateofbirth'])
            auth_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, auth_user)

            return redirect('index')
    else:
        form = UserProfileCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_orders = Order.objects.filter(customer=request.user)
    context = {'user_profile': user_profile, 'user_orders': user_orders}
    return render(request, 'flowershop/profile.html', context=context)


def blog(request):
    posts = Post.objects.all().order_by("-post_date")
    context = {"posts": posts}
    return render(request, 'flowershop/blog.html', context=context)

def order_product(request, id):
    item = get_object_or_404(Item, id=id)

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.item = item
            order.price = item.price * int(form.cleaned_data['quantity'])
            order.customer = request.user
            order.save()
            return redirect('profile')
    else:
        form = OrderForm(initial={'item': item})

    return render(request, 'flowershop/order_product.html', {'form': form, 'item': item})


def search(request):
    query = request.GET.get('query')
    items = Item.objects.filter(title__icontains=query)
    context = {"items": items}
    context.update(get_categories())
    return render(request, 'flowershop/shop.html', context=context)