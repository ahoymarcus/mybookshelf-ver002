from django.contrib import admin

from catalog.models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


# Creating a Inline Editing class to be included
class BooksInLine(admin.TabularInline):
	model = Book
	
	# This attribute prevents the layout to show spare bookinstances to be added (since there is already a link for that)
	extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
	# leaving the object empty and the web behaviour unthouched
	#pass
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	
	# Including Inline Editing Process
	inlines = [BooksInLine]
	
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Creating a Inline Editing class to be included
class BooksInstanceInline(admin.TabularInline):
	model = BookInstance
	
	# This attribute prevents the layout to show spare bookinstances to be added (since there is already a link for that)
	extra = 0

# Register the Admin classes for Book using the decorator process
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	# leaving the object empty and the web behaviour unthouched
	#pass
	list_display = ('title', 'author', 'display_genre')
	
	# Including Inline Editing Process
	inlines = [BooksInstanceInline]
	
	
# Register the Admin classes for BookInstance using the decorator process
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	# leaving the object empty and the web behaviour unthouched
	#pass
	
	list_display = ('book', 'status', 'borrower', 'due_back', 'id')
	list_filter = ('status', 'due_back')
	
	# Inserting fields set to group related model: the 1st grouping has 'no title' (none)
	fieldsets = (
		(None, {
			'fields': ('book', 'imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back', 'borrower')
		}),
	)
	