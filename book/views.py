from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Category, Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BookForm
from slugify import slugify
from django.contrib import messages


# Create your views here.



def index(request):
    categories = Category.objects.all()
    books = Book.objects.filter(published=True)

    categ_id = request.GET.get('categoryid')
    if categ_id:
        # ถ้ามีค่า 
        books = books.filter(category_id=categ_id)

   
    paginator = Paginator(books, 10)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    

    return render(request, 'book/index.html',{
        'categories':categories,
        'books':books,
        'categ_id':categ_id,
    })



def detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book/detail.html', {
        'book':book,
    })

def book_add(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.slug = slugify(book.name)
            book.published = True
            book.save()
            form.save_m2m()
            messages.success(request, 'Save success')
            return HttpResponseRedirect(reverse('book:index', kwargs={}))
        messages.error(request, 'Save failed')
    return render(request, 'book/add.html',{
        'form': form,
    })

def cart_add(request, slug):
    book = get_object_or_404(Book, slug=slug)
    cart_items = request.session.get('cart_items') or []

    # update existing item
    

    duplicated = False
    for c in cart_items:
        if c.get('slug') == book.slug:
            c['qty'] = int(c.get('qty') or '0') + 1
            duplicated = True
        
    # insert new item
    if not duplicated:
        cart_items.append({
            'id': book.id,
            'slug': book.slug,
            'name': book.name,
            'price':0,
            'qty': 1,
        })
    
    #Me
    for d in cart_items:
        if d.get('slug') == book.slug:
            d['price'] = int(d.get('price') ) + book.price
            
        

    request.session['cart_items'] = cart_items
    return HttpResponseRedirect(reverse('book:cart_list', kwargs={}))

def cart_reduce(request, slug):
    book = get_object_or_404(Book, slug=slug)
    cart_items = request.session.get('cart_items') or []

    # update existing item
    

    duplicated = False
    for c in cart_items:
        if c.get('slug') == book.slug:
            c['qty'] = int(c.get('qty') or '0') - 1
            duplicated = True
        
    # insert new item
    if not duplicated:
        cart_items.append({
            'id': book.id,
            'slug': book.slug,
            'name': book.name,
            'price':0,
            'qty': 0,
        })
    
    #Me
    for d in cart_items:
        if d.get('slug') == book.slug:
            # if d['qty'] != 0:
            d['price'] = int(d.get('price') ) - book.price
            
        

    request.session['cart_items'] = cart_items
    return HttpResponseRedirect(reverse('book:cart_list', kwargs={}))

def cart_list(request):

    cart_items = request.session.get('cart_items') or []


    total_qty = 0
    for c in cart_items:
        total_qty = total_qty + c.get('qty')

   
    request.session['cart_qty'] = total_qty
    return render(request, 'book/cart.html', {
        'cart_items': cart_items,

 
    })

def cart_delete(request, slug):
    cart_items = request.session.get('cart_items') or []
    for i in range(len(cart_items)):
        if cart_items[i]['slug'] == slug:
            del cart_items[i]
            break
    request.session['cart_items'] = cart_items
    return HttpResponseRedirect(reverse('book:cart_list', kwargs={}))

