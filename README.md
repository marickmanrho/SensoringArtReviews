# Sensoring Art Reviews
We try to find groups of sensory words which predict the sentiment of an art review.

## In short
When we try to describe something we often use sensory words. Does the use of these sensory words tell us something about the sentiment of a text? In particular how we try to describe something abstract as art?

To answer this question we plan to analyze art reviews from Brittish or U.S.A. newspapers from the last decade.

## Project layout
The project will be split into six sections, corresponding to the six folders in `./src`. Here we will explain each section into a little more detail.

### mine
In this section we assemble our database of art reviews. The datamining is done using webscraping techniques. We collect .html pages from online archives and extract the main body text and relevant meta-data.

### sentiment
The sentiment is determined per review and per sentence. The sentiment per review is found by training a neural network on the rating connected to the review. The sentiment per sentence is found using existing algorithms.

### nlp
Natural Language Processing is used to reduce the size of each review. We remove stop words, stem all verbs, and if the count of a word is very low we substitute it for a more common synonym.

### vectorize
We train a recurrent neural network (RNN) to find a vector embedding of all the words in our database. The vector space is reduced by keeping only sensory words.

### categorize
The word embeddings are categorized using a group finding algorithm.

### projection
Project the art reviews onto the categories. Compute the correlation function between sentence sentiment and category projection.
