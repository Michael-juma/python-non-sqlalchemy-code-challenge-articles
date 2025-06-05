class Author:
    all_articles = []  # Class variable to track all articles
    
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception("Name cannot be changed after instantiation")
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = value
    
    def articles(self):
        return [article for article in Author.all_articles if article.author == self]
    
    def magazines(self):
        magazines = []
        for article in self.articles():
            if article.magazine not in magazines:
                magazines.append(article.magazine)
        return magazines
    
    def add_article(self, magazine, title):
        from .article import Article
        article = Article(self, magazine, title)
        return article
    
    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return []
        categories = []
        for article in articles:
            if article.magazine.category not in categories:
                categories.append(article.magazine.category)
        return categories
