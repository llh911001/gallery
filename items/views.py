from django.views.generic import TemplateView
from gallery.items.models import Item

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['item_list'] = Item.objects.all()
        return context
