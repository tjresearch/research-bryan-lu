# Drawing Geometry Diagrams from Problem Statements

## Overview
The purpose of my project is to write a program that takes an olympiad geometry problem as input and is able to output an Asymptote diagram based on the problem statement. 

## Requirements
The project is written in Python 3.6, and requires the nltk, codecs, requests, selenium, and bs4 libraries, involved with text processing and webscraping. The project will also require the Stanford Dependency Parser, available [here](https://stanfordnlp.github.io/stanfordnlp). Some of the code requires the pycorenlp package, but likely the stanfordnlp package will work fine.

## Methods
This project borrows heavily from the github code associated with the paper Solving Geometry Problems: Combining Text and Diagram Intepretation (Seo et al., 2015) ([paper](https://pdfs.semanticscholar.org/c04f/e8aa97bee94b285585f4096706894137f0ce.pdf), [resources]
(http://geometry.allenai.org/)) Most of this code is converted to Python 3.7 from the original Python 2 code. The salient parts of the code that have been heavily modified are Webscraper for helping to scrape HTML webpages, and under the geosolver directory, the text and ontology subdirectory. 

## Installation Instructions
For Webscrape, only download HTML files for use with the scraping programs. Make sure all text files are in the same directory as the code opening them. The geosolver directory should be downloaded all in one piece. 

## Run Instructions
In order to run anything requiring  syntax parsing, run the following command in the directory where you have the Stanford NLP Parser installed: 
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000 

Otherwise, run Python from command line, or through IDE (Pycharm preferred). All files should run without user input. 
