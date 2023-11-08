import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost, CreateBlogForm, LoginForm, User  # Import your BlogPost model

def index(request):
    blog_posts = BlogPost.objects.all()  # Query all BlogPost objects

    context = {
        'blog_posts': blog_posts,  # Pass the queryset to the template context
        'year':datetime.date.today().year,
    }

    return render(request, 'index.htm', context)  # Render the 'index.html' template with the context


def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)

    context = {
        'blog_post': blog_post,'year':datetime.date.today().year,
    }

    return render(request, 'blog_details.htm', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:request.session['user'] = User.objects.get(username=username, password=password).id
            except User.DoesNotExist:pass
            finally:return redirect('/user/')

    else:
        form = LoginForm()

    return render(request, 'login.htm', {'form': form})

def user_page(request):
    user = request.session.get('user')
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            b = BlogPost(title=title, content=content, author=User.objects.get(id=user))
            b.save()
    else:
        form = CreateBlogForm()
    return render(request, 'user.htm', {'user':User.objects.get(id=user), 'blogs':BlogPost.objects.filter(author_id=user)})