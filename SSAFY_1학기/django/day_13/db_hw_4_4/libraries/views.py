from django.shortcuts import render,redirect
from .models import Book
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    review_form = ReviewForm()
    context = {
        'book': book,
        'review_form':review_form,
    }
    return render(request, 'libraries/detail.html', context)

def creates_review(request,book_pk):
    # 1. 리뷰를 작성할 책의 인스턴스 생성
    book = Book.objects.get(pk=book_pk)
    # 2. 작성한 리뷰를 받아옴
    review_form = ReviewForm(request.POST)
    # 3. 적절히 작성된 리뷰야??
    if review_form.is_valid():
        # 4. 일단 임시 저장하고 그 객체 뽑아와바
        review = review_form.save(commit=False)
        # 5. foreignKey 넣어주자
        # 6. user도 넣어줘야 한다!!
        review.user = request.user
        review.book = book
        review.save()
    return redirect('libraries:detail', book.pk)

def deletes_review(request,book_pk,review_pk):
    # 1. 어떤 책이야?
    book = Book.objects.get(pk=book_pk)
    # 2. 어떤 댓글이야?
    review = book.review_set.get(pk=review_pk)
    # 3. 삭제하자
    review.delete()
    return redirect('libraries:detail', book.pk)