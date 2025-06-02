#!/usr/bin/env python3
import ipdb

from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine

if __name__ == '__main__':
    # Create some test instances
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Science Weekly", "Science")
    
    article1 = Article(author1, magazine1, "The Future of AI")
    article2 = Article(author1, magazine2, "Climate Change Solutions")
    article3 = Article(author2, magazine1, "Programming Best Practices")
    
    print("Debug session started. Test your code here!")
    print("Available objects: author1, author2, magazine1, magazine2, article1, article2, article3")
    
    # Test some methods
    print(f"Author1 articles: {len(author1.articles())}")
    print(f"Magazine1 contributors: {len(magazine1.contributors())}")
    print(f"Author1 topic areas: {author1.topic_areas()}")
    
    ipdb.set_trace()
