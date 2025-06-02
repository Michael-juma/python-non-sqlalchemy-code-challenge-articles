class Author:
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
        self._name = value
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        magazine_list = []
        for article in self.articles():
            if article.magazine not in magazine_list:
                magazine_list.append(article.magazine)
        return magazine_list
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        categories = []
        for magazine in magazines:
            if magazine.category not in categories:
                categories.append(magazine.category)
        return categories