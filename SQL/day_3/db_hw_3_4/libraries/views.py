from django.shortcuts import render,redirect
from .models import Author
from .forms import BookCreateForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    book_create_form = BookCreateForm()
    context = {
        'author': author,
        'book_create_form': book_create_form,
    }
    return render(request, 'libraries/detail.html', context)

def books_create(request,author_pk):
    # 1. 어떤 author의 book을 추가할거야? author를 특정해야 해
    author = Author.objects.get(pk=author_pk)
    # 2. book에 대한 정보가 담긴 form을 바로 저장해도 되겠어?
    form = BookCreateForm(request.POST)
    if form.is_valid():
        # 3. 1:N 관계에서 foreignkey를 특정해야지!
        book = form.save(commit=False)
        book.author = author
        # 4. 이제 저장하면 문제 없어~
        book.save()
    return redirect('libraries:detail', author.pk)