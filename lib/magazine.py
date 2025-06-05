class Magazine:
    _all_magazines = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all_magazines.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value
    
    def articles(self):
        from .author import Author
        return [article for article in Author.all_articles if article.magazine == self]
    
    def contributors(self):
        authors = []
        for article in self.articles():
            if article.author not in authors:
                authors.append(article.author)
        return authors
    
    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]
    
    def contributing_authors(self):
        articles = self.articles()
        if not articles:
            return None
        
        author_counts = {}
        for article in articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None
    
    @classmethod
    def top_publisher(cls):
        if not any(magazine.articles() for magazine in cls._all_magazines):
            return None
        
        top_magazine = None
        max_articles = 0
        
        for magazine in cls._all_magazines:
            article_count = len(magazine.articles())
            if article_count > max_articles:
                max_articles = article_count
                top_magazine = magazine
        
        return top_magazine
