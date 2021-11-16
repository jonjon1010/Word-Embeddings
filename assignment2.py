# CompSci 723 - Intro to NLP 
# Name: Jonathan Nguyen 
# Date: 11/07/2021 
# Title: Assignment 2: Word Embeddings 
# Version: 1.0 

#Setup:
#Please go through the slides A2.pptx that will help you with the following steps:
#1. Install Gensim
#2. Try things from A2.pptx. Download word2vec and glove pre-trained word embeddings as shown in the slides.

#Tasks:
#1. Evaluate word2vec and glove embeddings on the SimLexA2.txt dataset (file in the right format is already uploaded in Canvas).
#2. Come up with at least 10 word pairs on your own and assign them similarity scores 0-1 based  on your judgement (make sure you have a good range of scores). Create your own tab-delimited file. Evaluate word2vec and glove embeddings on your dataset. Also record the similarity scores obtained using word2vec and glove for each word pair. (In case a word you used is not in the embedding then replace the word pair with a new word pair).
#3. Come up with at least 10  word analogy questions on your own and write them in the format needed by Gensim. Evaluate both word2vec and glove on your dataset.
#4. Choose any 10 words and find their most similar five words using word2vec and glove embeddings.

#Submit: 
#1. Report: Write a report in which you include:
#- Task 1 (2 points): Pearson correlation coefficients obtained using each of the two embeddings.
#- Task 2 (3 points): Pearson correlation coefficients obtained using each of the two embeddings. A table showing the word pairs and the similarity scores from the two embeddings. Write some comments on the results.
#- Task 3 (3 points): Accuracies obtained by the two embeddings. Write some comments on correct and incorrect ones.
#- Task 4 (2 points): Show the similar words in a table. Give some some comments, especially comparing the two embeddings.

#Code: 
#(3 points) Submit all the code you wrote for doing this assignment as an executable .py file. The grader should be able to replicate your results.

#Dataset: 
#(2 points): Submit the small datasets you created for Tasks 2 and 3 as plain text .txt files.

#**Imports Gensim library into the program. Gensim is a topic modeling tool used by humans in NLP**

import gensim.downloader as api

#**Contains pre-trained word embeddings**
 
wv = api.load('word2vec-google-news-300') #word2vec pre-trained word embedding model 
glove = api.load("glove-wiki-gigaword-300") #glove pre-trained word embedding model  

#**Task 1: Similarirty Evaluation between word2vec and glove word embeddings for SimLexA2.txt file**

#Line 48 and 51 are used for testing purposes to see if results were similair to what Dr. Kate got in class.
#In conculsion, my results were slightly off by a little bit compare to Dr. Kate. This might be because I am using Python Veriosn 3.10 instead of 3.8.9 that was used in class.   

#**Lines 49 and 52 imports the following text files into the program that's being used by the program from the computer being used** 
#**Lines 50 and 53 evalutates the dataset given from the SimeLexA2.txt and finds the similarity**

#sim =  open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/sim.txt", "r")
SimLexA2 = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/SimLexA2.txt", "r")
print("\n", "Similarity Evaluation using word2vec over the dataset in the file SimLexA2.txt:\n\n", wv.evaluate_word_pairs(SimLexA2), "\n") 
#sim =  open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/sim.txt", "r")
SimLexA2 = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/SimLexA2.txt", "r")
print("Similarity Evaluation using glove over the dataset in the file SimLexA2.txt:\n\n", glove.evaluate_word_pairs(SimLexA2), "\n")

#**Task 2: Similarirty Evaluation between word2vec and glove word embeddings for at least 10 word pairs**

#1st Word Pair Similarity Score 
print("1st Word Pair:")
print("word2vec similiarty score for bake and cook is", wv.similarity("bake", "cook"))
print("glove similiarty score for bake and cook is", glove.similarity("bake", "cook"), "\n")

#2nd Word Pair Similarity Score 
print("2nd Word Pair:")
print("word2vec similiarty score for hurt and pain is", wv.similarity("hurt", "pain"))
print("glove similiarty score for hurt and pain is", glove.similarity("hurt", "pain"), "\n")

#3rd Word Pair Similarity Score 
print("3rd Word Pair:")
print("word2vec similiarty score for baseball and bat is", wv.similarity("baseball", "bat"))
print("glove similiarty score for baseball and bat is", glove.similarity("baseball", "bat"), "\n")

#4th Word Pair Similarity Score 
print("4th Word Pair:")
print("word2vec similiarty score for dessert and desert is", wv.similarity("dessert", "desert"))
print("glove similiarty score for dessert and desert is", glove.similarity("dessert", "desert"), "\n")

#5th Word Pair Similarity Score 
print("5th Word Pair:")
print("word2vec similiarty score for hot and desert is", wv.similarity("hot", "dessert"))
print("glove similiarty score for hot and desert is", glove.similarity("hot", "dessert"), "\n")

#6th Word Pair Similarity Score 
print("6th Word Pair:")
print("word2vec similiarty score for dessert and ocean is", wv.similarity("dessert", "ocean"))
print("glove similiarty score for dessert and ocean is", glove.similarity("dessert", "ocean"), "\n")

#7th Word Pair Similarity Score 
print("7th Word Pair")
print("word2vec similiarty score for bat and club is", wv.similarity("bat", "club"))
print("glove similiarty score for bat and club is", glove.similarity("bat", "club"), "\n")

#8th Word Pair Similarity Score 
print("8th Word Pair:")
print("word2vec similiarty score for glass and plastic is", wv.similarity("glass", "plastic"))
print("glove similiarty score for glass and plastic is", glove.similarity("glass", "plastic"), "\n")

#9th Word Pair Similarity Score 
print("9th Word Pair:")
print("word2vec similiarty score for hot and cold is", wv.similarity("hot", "cold"))
print("glove similiarty score for hot and cold is", glove.similarity("hot", "cold"), "\n")

#10th Word Pair Similarity Score 
print("10th Word Pair:")
print("word2vec similiarty score for ice and cold is", wv.similarity("ice", "cold"))
print("glove similiarty score for ice and cold is", glove.similarity("ice", "cold"), "\n")

#11th Word Pair Similarity Score 
print("11th Word Pair:")
print("word2vec similiarty score for flame and heat is", wv.similarity("flame", "heat"))
print("glove similiarty score for flame and heat is", glove.similarity("flame", "heat"), "\n")

#12th Word Pair Similarity Score 
print("12th Word Pair:")
print("word2vec similiarty score for flame and fire is", wv.similarity("flame", "fire"), "\n")
print("glove similiarty score for flame and fire is", glove.similarity("flame", "fire"), "\n")

#13th Word Pair Similarity Score 
print("13th Word Pair:")
print("word2vec similiarty score for wet and dry is", wv.similarity("wet", "dry"))
print("glove similiarty score for wet and dry is", glove.similarity("wet", "dry"), "\n")

#14th Word Pair Similarity Score 
print("14th Word Pair:")
print("word2vec similiarty score for far and further is", wv.similarity("far", "further"))
print("glove similiarty score for far and further is", glove.similarity("far", "further"), "\n")

#15th Word Pair Similarity Score 
print("15th Word Pair:")
print("word2vec similiarty score for road and sidewalk is", wv.similarity("road", "sidewalk"))
print("glove similiarty score for road and sidewalk is", glove.similarity("road", "sidewalk"), "\n")

#16th Word Pair Similarity Score 
print("16th Word Pair:")
print("word2vec similiarty score for lamp and pole is", wv.similarity("lamp", "pole"))
print("glove similiarty score for lamp and pole is", glove.similarity("lamp", "pole"), "\n")

#17th Word Pair Similarity Score 
print("17th Word Pair:")
print("word2vec similiarty score: for fire and torch is", wv.similarity("fire", "torch"))
print("glove similiarty score for fire and torch is", glove.similarity("fire", "torch"), "\n")

#18th Word Pair Similarity Score 
print("18th Word Pair:")
print("word2vec similiarty score for lamp and light is", wv.similarity("lamp", "light"))
print("glove similiarty score for lamp and light is", glove.similarity("lamp", "light"), "\n")

#19th Word Pair Similarity Score 
print("19th Word Pair:")
print("word2vec similiarty score for wood and far is", wv.similarity("wood", "far"))
print("glove similiarty score for wood and far is", glove.similarity("wood", "far"), "\n")

#20th Word Pair Similarity Score 
print("20th Word Pair:")
print("word2vec similiarty score for fan and wind is", wv.similarity("fan", "wind"))
print("glove similiarty score for fan and wind is", glove.similarity("fan", "wind"), "\n")

#Evaulates the Similarity of the Dataset in SimOwnWordPairs.txt file  
SimOwnWordPairs = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/SimOwnWordPairs.txt", "r")
print("Similarity Evaluation using word2vec over the dataset in the file SimOwnWordPairs.txt:\n\n", wv.evaluate_word_pairs(SimOwnWordPairs), "\n")
SimOwnWordPairs = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/SimOwnWordPairs.txt", "r")
print("Similarity Evaluation using glove over the dataset in the file SimOwnWordPairs.txt:\n\n", glove.evaluate_word_pairs(SimOwnWordPairs), "\n")

#**Task 3: Word Analogy Evaluation between word2vec and glove word embeddings at least 10 word analogy questions**

#analogy = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/analogy.txt", "r")
#print("Word Analogy Evaluation accuracy using word2vec over the dataset in the file analogy.txt:\n")
#a = wv.evaluate_word_analogies(analogy)
#print(a[0], "\n")
#print("Word Analogy Evaluation accuracy using glove over the dataset in the file analogy.txt:\n")
#analogy = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/analogy.txt", "r")
#b = wv.evaluate_word_analogies(analogy)
#print(b[0], "\n")

#test = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/test.txt", "r")
#print("Word Analogy Evaluation accuracy using word2vec over the dataset in the file test.txt:\n")
#c = wv.evaluate_word_analogies(test)
#print(c[0], "\n")
#test = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/test.txt", "r")
#print("Word Analogy Evaluation accuracy using glove over the dataset in the file test.txt:\n")
#d = glove.evaluate_word_analogies(test)
#print(d[0], "\n")

SimOwnWordAnalogies = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/SimOwnWordAnalogies.txt", "r")
print("Word Analogy Evaluation accuracy using word2vec over the dataset in the file SimOwnWordAnalogies.txt:\n")
e = wv.evaluate_word_analogies(SimOwnWordAnalogies)
print(e[0], "\n")
print("Word Analogy Evaluation Correct and Incorrect using word2vec over the dataset in the file SimOwnWordAnalogies.txt:\n")
print(e[1], "\n")
SimOwnWordAnalogies = open("/Users/Jonathan Nguyen/Python/CompSci 723 Assignment 2/SimOwnWordAnalogies.txt", "r")
print("Word Analogy Evaluation accuracy using glove over the dataset in the file SimOwnWordAnalogies.txt:\n")
f = glove.evaluate_word_analogies(SimOwnWordAnalogies)
print(f[0], "\n")
print("Word Analogy Evaluation Correct and Incorrect using glove over the dataset in the file SimOwnWordAnalogies.txt:\n")
print(f[1], "\n")

#**Task 4: Find most similar five words of any 10 words using word2vec and glove embeddings** 

#word2vec most similar words 
print("Finding the most similar words for the 10 words using word2vec:\n")
print("Similar words to bee", wv.most_similar("bee"), "\n")
print("Similar words to chicken", wv.most_similar("chicken"), "\n")
print("Similar words to television", wv.most_similar("television"), "\n") 
print("Similar words to telephone", wv.most_similar("telephone"), "\n")
print("Similar words to flower",wv.most_similar("flower"), "\n")
print("Similar words to printer",wv.most_similar("printer"), "\n")
print("Similar words to plant",wv.most_similar("plant"), "\n")
print("Similar words to planet",wv.most_similar("planet"), "\n")
print("Similar words to board",wv.most_similar("board"), "\n")
print("Similar words to cabinet",wv.most_similar("cabinet"), "\n")

#glove most similar words 
print("Finding most similar words for the 10 words using glove:\n")
print("Similar words to bee", glove.most_similar("bee"), "\n")
print("Similar words to chicken", glove.most_similar("chicken"), "\n")
print("Similar words to television", glove.most_similar("television"), "\n") 
print("Similar words to telephone", glove.most_similar("telephone"), "\n")
print("Similar words to flower",glove.most_similar("flower"), "\n")
print("Similar words to printer",glove.most_similar("printer"), "\n")
print("Similar words to plant",glove.most_similar("plant"), "\n")
print("Similar words to planet",glove.most_similar("planet"), "\n")
print("Similar words to board",glove.most_similar("board"), "\n")
print("Similar words to cabinet",glove.most_similar("cabinet"), "\n")