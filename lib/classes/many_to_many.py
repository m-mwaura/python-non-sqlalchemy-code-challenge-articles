class Article:

    all = [] #track all articles

    def __init__(self, author, magazine, title):
        #validate input types
        if not isinstance(author, Author):
            raise Exception("Author must be instance of Author")
        
        if not isinstance (magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")        

        #initialize instance variables
        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    
    @property
    def author(self):
        return self._author
    
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an intance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self._magazine = value


class Author:
    
    def __init__(self, name):

        #validate name input
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string.")
        
        if hasattr(self, '_name'):
            raise Exception("Name cannot be changed after initialization")
        
        #initialize instance variables
        self._name = name
        self._articles = [] #list to store articles written by the author 

    @property
    def name(self):
        return self._name 
    
    #returns a list of all articles written by the author
    def articles(self):
        return self._articles

    #returns a unique list of magazines the author has contributed to
    def magazines(self):
        return list({article.magazine for article in self._articles})

    #Create and return a new article for this author
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Return unique categories the author has written for
    def topic_areas(self):
        topics = {magazine.category for magazine in self.magazines()}
        return list(topics) if topics else None
    

class Magazine:

    all = [] #track all magazine instances

    def __init__(self, name, category):

        # Validate name and category inputs
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 characters")
        
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        
        # initialize instance variables
        self._name = name
        self._category = category
        self._articles = [] #List to store articles published in this magazine

        Magazine.all.append(self) #track all magazine

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        #validate and update magazine name
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):

        #update and validate category
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non empty string")
        self._category = value
      

    def articles(self):
        #Return all articles published in the magazine
        return self._articles

    def contributors(self):
        #Return unique list of authors who have contributed to the magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        #Return a list of article titles or None if no articles exist
        return [article.title for article in self._articles] if self._articles else None
    
    #Return a list of authors who have written more than two articles
    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2] or None
    
    #returns the magazine with most article or none if therent any
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)
    