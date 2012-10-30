from django.views.generic import ListView, DetailView
from gallery.items.models import Item, Photo
from gallery.items.views import IndexView

urlpatterns = patterns('',
        url(r'^$', IndexView.as_view()),
        url(r'^items/$', ListView.as_view(
            queryset=Item.objects.all(),
            template_name='item_list.html',
