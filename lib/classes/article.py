 
def __init__(self, author, magazine, title: str):
        if not hasattr(author, 'name'):
            raise ValueError("author bmust be an instance of the Author class")
        if not hasattr(magazine, 'name'):
            raise ValueError("magazine must be an instance of the Magazine class")
        
        if not isinstance(title, str):
             raise ValueError("Title must be of type str.")
        if len(title) < 5 or len(title) > 50:
             raise ValueError("Title must be between 5 and and 50 character, inclusive.")
        
        self.title = title
        self.author = author
        self.magazine = magazine
        
        @property
        def title(self):
             return self._title
        
        @title.setter
        def title(self, value):
             raise AttributeError("Article title cannot be changed once it is set.")