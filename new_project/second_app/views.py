from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict={'insert_content':"Hello This is the second try!!"}
    return render(request,'index.html',context=my_dict)
