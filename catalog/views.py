from django.shortcuts import render

from catalog.models import Book, Author, BookInstance, Genre, Language

# Create your views here.
def index(request):
	"""View function to the home page of the site."""
	
	# Generates counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	
	# Available books(status = 'a')
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	
	# The 'all()' is implied by default
	# num_authors = Author.objects.all().count()
	num_authors = Author.objects.count()
	
	# Filtering some text subjects and counts
	num_python_words = Book.objects.filter(title__icontains='python').count()
	name_python_books = Book.objects.filter(title__icontains='python')[:15] # Get 15 books containing the title python
	
	# Using Session to count the number of visits to this view with this var
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1
	
	#a context variable, which is a Python dictionary, containing the data to insert into the placeholders.
	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_python_words': num_python_words,
		'name_python_books': name_python_books,
		'num_visits': num_visits,
	}
	
	# Using the context data create to send data to the view to be renred
	return render(request, 'index.html', context=context)
	
from django.views import generic

class BookListView(generic.ListView):
	"""Generic class-based view for a list of books."""
	model = Book
	paginate_by = 10
	
	# your own name for the list as a template variable
	# See that the view passes the context (list of books) by default as object_list and book_list aliases; either will work.
	context_object_name = 'book_list'
	queryset = Book.objects.all()
	template_name = 'books/books_name_list.html'
	
class BookDetailView(generic.DetailView):
	"""Generic class-based detail view for a book."""
	model = Book

class AuthorListView(generic.ListView):
	"""Generic class-based list view for a list of authors."""
	model = Author
	paginate_by = 10
	
	
	
class AuthorDetailView(generic.DetailView):
	"""Generic class-based detail view for an author."""
	model = Author
	
	
from django.contrib.auth.mixins import LoginRequiredMixin
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
	"""Generic class-based view listing books on loan to current user."""
	model = BookInstance
	template_name = 'catalog/bookinstance_list_borrowed_user.html'
	paginate_by = 10
	
	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
		
		
