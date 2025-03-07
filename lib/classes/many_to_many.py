class Article:

    all = []

    def __init__(self, author, magazine, title):
        
        if not isinstance(author, Author):
            raise Exception("Author must be instance of Author")
        
        if not isinstance (magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")        

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

        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string.")
        
        if hasattr(self, '_name'):
            raise Exception("Name cannot be changed after initialization")
        
        self._name = name
        self._articles = []  

    @property
    def name(self):
        return self._name 
    
     
    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = {magazine.category for magazine in self.magazines()}
        return list(topics) if topics else None
    

class Magazine:

    all = []

    def __init__(self, name, category):

        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 characters")
        
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        
        self._name = name
        self._category = category
        self._articles = []

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be a string between 2 and 16 characters")
        
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):

        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non empty string")
        self._category = value
      

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2] or None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)
    

