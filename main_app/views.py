from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Item
# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', { 'items': items })

class AddItem(CreateView):
    model = Item
    fields = '__all__'

def delete(request, item_id):
    Item.objects.filter(id=item_id).delete()
    return redirect('index')