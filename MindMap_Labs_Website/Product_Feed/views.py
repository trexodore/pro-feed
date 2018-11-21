from django.shortcuts import render
from django.http import HttpResponse
from Product_Feed.models import Feed

# Create your views here.
def index(request):
    return render(request,'MindMap_Labs_Website/index.html')

#Product Feed views
def prod_index(request):
    feed_list = Feed.objects.order_by('website')
    website_dict = {'feeds':feed_list}
    return render(request,'Product_Feed/index.html',context=website_dict)
