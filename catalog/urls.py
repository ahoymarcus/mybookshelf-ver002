from django.urls import path
from . import views


# From here we are going to pass all the path specific from the Catalog application
# The path() directs to a view, and it also creates a name to 'reverse' the mapper, and use the name to point to this url
# Note: We can hard code the link as in <a href="/catalog/">Home</a>), but if we change the pattern for our home page, for example, to /catalog/index) the templates will no longer link correctly. Using a reversed url mapping is much more flexible and robust.
# Remembet that as /myLocalLibrary/urls.py has already been configured to redirec, we will have: /catalog/books and /catalog/authors. See also that this present path is using a view implemen ted as a class! 
# See at path for BookDetailView how it's used a angle brackets to capture the part of the url for the mapping. Also, it was def a name and a type for the var to hold the info (pk as primary_key.
urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name='books'), 
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

# Testing borrowed URL path
urlpatterns += [
	path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
