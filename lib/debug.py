#!/usr/bin/env python3
import ipdb

from author import Author
from article import Article
from magazine import Magazine

if __name__ == '__main__':
    # Create some sample instances for testing
    author_1 = Author("Carry Bradshaw")
    author_2 = Author("Nathaniel Hawthorne")
    
    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")
    
    article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
    article_2 = Article(author_1, magazine_2, "Dating life in NYC")
    article_3 = Article(author_2, magazine_2, "A very long article title that is within the character limit")
    
    # Test some methods
    print("Author 1 articles:", len(author_1.articles()))
    print("Author 1 magazines:", [mag.name for mag in author_1.magazines()])
    print("Magazine 1 contributors:", [auth.name for auth in magazine_1.contributors()])
    print("Magazine 2 article titles:", magazine_2.article_titles())
    
    ipdb.set_trace()
