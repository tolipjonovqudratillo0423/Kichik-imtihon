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
# def update(request,id):
    context = {
        'movie': Movie.objects.get(id=id)
    }
    if request.method == "POST":
        
        print("update form ishladi !!!")

        up_form = MovieForm(request.POST,request.FILES)
        print(up_form)
        if up_form.is_valid():
            print('up_form valid')
            Movie.objects.filter(id = id).update(
                title = up_form.cleaned_data.get('title'),
                desc = up_form.cleaned_data.get('desc'),
                image = up_form.cleaned_data.get('image'),
                genre = up_form.cleaned_data.get('genre'),
                # duration = cr_form.cleaned_data.get('duration'),
                date = up_form.cleaned_data.get('date'),
                duration = up_form.cleaned_data.get('duration'),
                author = up_form.cleaned_data.get('author')
            )
            return redirect('home')
        else:
            print(" up_form is INVALID")
            print(up_form.errors)
    
    print("Post method kelmadi")
    return render(request,'update.html',context=context)

    
    return render(request,'update.html',context=context)

def update(request,id):
    movie = get_object_or_404(Movie,id=id)
    if request.method == 'POST':
        print("Method is POST update")
        up_form = MovieForm(request.POST,request.FILES)
        if up_form.is_valid():
            print("up_form is valid")
            data = up_form.cleaned_data
            movie.title = data['title']
            movie.desc = data['desc']
            movie.author = data['author']
            movie.date = data['date']
            movie.duration = data['duration']
            movie.genre = data['genre']
            
            if "image" in request.FILES:
                movie.image = data['image']
            movie.save()
            return redirect('home')
        else:
            print("INVALID up form")
            return redirect('error')
    else:
        initial_data = {
            'title':movie.title,
            'desc':movie.desc,
            'author':movie.author,
            'duration':movie.duration,
            'date':movie.date,
            'genre':movie.genre,
            
        }
        form = MovieForm(initial=initial_data)
        return render(request,'update.html',{'form':form,"movie":movie})

    
def update_new_usul(request,id):
    movie = get_object_or_404(Movie,id=id)
    if request.method == 'POST':
        up_form = MovieForm(request.POST,request.FILES,instance=movie)
        if up_form.is_valid():
            up_form.save()
        else:
            print("up_form is invalid",up_form.errors)
            return redirect('error')
    else:
        form = MovieForm(instance=movie)
        return render(request, 'update.html', {'form': form, "movie": movie})
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
    movie = get_object_or_404(Movie,id=id)
    context = {
        'movie':movie
    }
    return render(request,'detail.html',context=context)
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