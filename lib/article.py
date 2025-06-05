class Article:
    def __init__(self, author, magazine, title):
        from .author import Author
        from .magazine import Magazine
        
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine class")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        
        self._title = title
        self._author = author
        self._magazine = magazine
        
        # Add this article to the class-level tracking
        Author.all_articles.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise Exception("Title cannot be changed after instantiation")
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author class")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine class")
        self._magazine = value
