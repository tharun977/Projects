from django.shortcuts import render, get_object_or_404, redirect
from .models import BookCategory
from .forms import BookCategoryForm

def book_category_list(request):
    categories = BookCategory.objects.all()
    return render(request, 'books/book_category_list.html', {'categories': categories})

def book_category_create(request):
    if request.method == 'POST':
        form = BookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_category_list')
    else:
        form = BookCategoryForm()
    return render(request, 'books/book_category_form.html', {'form': form})

def book_category_update(request, pk):
    category = get_object_or_404(BookCategory, pk=pk)
    if request.method == 'POST':
        form = BookCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('book_category_list')
    else:
        form = BookCategoryForm(instance=category)
    return render(request, 'books/book_category_form.html', {'form': form})

def book_category_delete(request, pk):
    category = get_object_or_404(BookCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('book_category_list')
    return render(request, 'books/book_category_confirm_delete.html', {'category': category})
