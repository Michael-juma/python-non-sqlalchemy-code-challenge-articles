
class Magazine:
    all = []
    
    def __init__(self, name, category):
        self.name = name  # This will call the setter
        self.category = category  # This will call the setter
        Magazine.all.append(self)
    
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
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        author_list = []
        for article in self.articles():
            if article.author not in author_list:
                author_list.append(article.author)
        return author_list
    
    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]
    
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        
        contributing = [author for author, count in author_counts.items() if count > 2]
        return contributing if contributing else None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        
        max_articles = 0
        top_magazine = None
        
        for magazine in cls.all:
            article_count = len(magazine.articles())
            if article_count > max_articles:
                max_articles = article_count
                top_magazine = magazine
        
        return top_magazine if max_articles > 0 else None
