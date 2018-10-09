from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Genre(models.Model):
    """
    Model representing a book genre(e.g. Science Fiction, Non Fiction)
    """

    name = models.CharField(max_length=200, help_text= "Enter a book genre(e.g.Science Fiction, French Poetry, etc)")

    history = models.TextField(help_text="Enter a genre story")

    def __str__(self):
        """
        String to representing the Model object (in Admin site etc.)
        """

        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('genre-detail', args=[str(self.id)])


class Language(models.Model):
    language = models.CharField(max_length=20, help_text="Enter a language")

    def __str__(self):
        """
        String to representing the Model object (in Admin site etc.)
        """

        return self.language


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    history = models.TextField(help_text="Enter a genre story")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    biography = models.TextField(help_text="Enter an author biography")
    gallery = models.ImageField


    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0} {1}'.format(self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name']

# Create your models here.
