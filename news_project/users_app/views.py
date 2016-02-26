from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from .models import category ,post,tag
# Create your views here.




from models import post , tag
def index (request):

    #posts = post.objects.all()

    #return render (request,'index.html',{'posts':posts })

	testpost= post.objects.all()
	paginator = Paginator(testpost,5)  #Show 5 posts per page
	page_num=request.GET.get('page')
	try:
        	walk = paginator.page(page_num)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        	walk = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        	walk= paginator.page(paginator.num_pages)

	return render(request, 'index.html',{"walk":walk})

