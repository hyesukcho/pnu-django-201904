# from django.views.generic import ListView
from django.shortcuts import redirect,render
from .models import Shop, Item
from .forms import ShopForm


def shop_list(request):
    qs = Shop.objects.all()
    return render(request, 'shop/shop_list.html', {
        'shop_list': qs,
    })


def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)
    return render(request, 'shop/shop_detail.html', {
        'shop': shop,
    })


def shop_new(request):
    if request.method == 'GET':  # 'GET', 'POST'
        form = ShopForm()
    else:
        # request.GET, request.POST, request.FILES
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shop/')
    return render(request, 'shop/shop_form.html', {
        'form': form,
    })




def item_list(request):
    # DB로부터 모든 Item List를 가져올 예정
    qs = Item.objects.all()  # QuerySet 타입
    # 템플릿 파일 위치 : shop/templates/shop/item_list.html
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
    })


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)  # 즉시 DB로부터 Fetch
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })
