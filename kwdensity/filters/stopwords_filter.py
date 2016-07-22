#-*- coding: utf-8 -*-
import os.path
from .base_filter import BaseFilter


class StopwordsFilter(BaseFilter):

    def __init__(self, country):
        super(StopwordsFilter, self).__init__()
        self.country = country
        self.fname = 'stopwords/%s.txt' % self.country
        with open(self.fname, 'rb') as f:
            self.stopwords = {l.strip().decode('utf8') for l in f if l}

    def predicate(self, tok):
        """Returns True if tok not in stopwords else False"""
        return tok not in self.stopwords


