from django.shortcuts import render,redirect,get_object_or_404
from .forms import MovieForm
from django.http import HttpResponseForbidden
from .models import Movie
# Create your views here.

def index(request):
    context = {
        'data': Movie.objects.all() 
              }
    return render(request,'index.html',context=context)
def update(request,id):
    context = {
        'movie': Movie.objects.get(id=id)
    }
    if request.method == "POST":
        
        print("update form ishladi !!!")

        up_form = MovieForm(request.POST,request.FILES)
        print(up_form)
        if up_form.is_valid():
            print('up_form valid')
            Movie.objects.filter(id == id).update(
                title = up_form.cleaned_data.get('title'),
                desc = up_form.cleaned_data.get('desc'),
                image = up_form.cleaned_data.get('image'),
                genre = up_form.cleaned_data.get('genre'),
                # duration = cr_form.cleaned_data.get('duration'),
                date = up_form.cleaned_data.get('date'),
            )
        else:
            print(" up_form is INVALID")
            print(up_form.errors)
    else:
        print("Post method kelmadi")
        return render(request,'update.html')

    
    return render(request,'update.html')
def delete(request,id):
    movie = get_object_or_404(Movie,id=id)
    # if request.user != movie.author:
    #      return HttpResponseForbidden("У вас нет прав для удаления этого фильма")
    
    if request.method == "POST":
        movie.delete()
        return redirect('home')
    context = {
        'movie': movie
    }
    return render(request,'delete.html',context=context)
def detail(request,id):
    return render(request,'detail.html')
def create(request):
    if request.method == "POST":

        
        print("create form ishladi !!!")

        cr_form = MovieForm(request.POST,request.FILES)
        print(cr_form)
        if cr_form.is_valid():
            print('cr_form valid')
            Movie.objects.create(
                title = cr_form.cleaned_data.get('title'),
                desc = cr_form.cleaned_data.get('desc'),
                image = cr_form.cleaned_data.get('image'),
                genre = cr_form.cleaned_data.get('genre'),
                # duration = cr_form.cleaned_data.get('duration'),
                date = cr_form.cleaned_data.get('date'),
                duration = cr_form.cleaned_data.get('duration'),
                author = cr_form.cleaned_data.get('author')
            )
            return redirect('home')
        else:
            print(" cr_form is INVALID")
            print(cr_form.errors)
    else:
        print("Post method kelmadi")

            

    return render(request,'create.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def error(request):
    return render(request,'error.html')