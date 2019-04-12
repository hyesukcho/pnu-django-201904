from django.contrib import admin
from django.urls import include, path

# FIXME: 이 코드는 RedirectView에 의해서 제거될 것입니다.
from django.shortcuts import redirect
def root(request):
    return redirect("/shop/")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('', root),
]
