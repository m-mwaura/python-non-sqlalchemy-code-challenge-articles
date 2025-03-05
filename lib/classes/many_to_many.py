class Article:

    all = []

    def __init__(self, author, magazine, title):
        
        if not isinstance(author, Author):
            raise Exception(f"Author must be instance of Author")
        
        if not isinstance (magazine, Magazine):
            raise Exception(f"Magazine must be an instance of a Magazine")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        author.articles().append(self)
        magazine.articles().append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(value, str):
            raise Exception(f"Titles must be of type str")
        if len(value) < 5 or len(value) > 50:
            raise Exception(f"Title must be a string between 5 and 50 characters")
        self._title = value

    
    
    @property
    def author(self):
        return self._author
    
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception(f"Author must be an intance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception(f"Magazine must be an instance of Magazine")
        self._magazine = value


        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception(f"Author name must be a non-empty string.")
        self._name = name
        self._articles = []  

    @property
    def name(self):
        return self._name 
    
     
    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title) 
        return new_article

    def topic_areas(self):
        topics = {magazine.category for magazine in self.magazines()}
        return list(topics) if topics else None

class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            pass  

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            pass  

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
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None
    
    ##