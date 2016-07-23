#-*- coding: utf-8 -*-
from setuptools import setup
import glob

files = glob.glob("kwdensity/filters/stopwords/*.txt")


def read(fname):
    with open(fname, 'rb') as f:
        txt = f.read()
    return txt


setup(
    name = "keyword_density",
    version = "0.1",
    author = "Giorgos Komninos",
    author_email = "g@gkomninos.com",
    description = ("Computes the keyword density of a string"),
    license = "BSD",
    keywords = "keyword density seo",
    url = "",
    packages=['kwdensity', 'kwdensity.filters',],
    long_description=read('README.md'),
    classifiers=[
    ],
    data_files = [('kwdensity/filters/stopwords', files),]
)

