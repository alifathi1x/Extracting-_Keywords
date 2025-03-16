# Extracting-_Keywords

# Introduction:
In the field of Natural Language Processing (NLP), text preprocessing is a critical step that significantly impacts the performance of downstream tasks such as text classification, sentiment analysis, and machine translation. One common preprocessing task is the removal of stop words—words that are frequently used in a language but carry little meaningful information. Examples of such words in English include "am," "is," "are," "the," "and," and "in." These words often add noise to the data and can be removed to improve the efficiency and accuracy of NLP models.
This project focuses on the extraction and removal of specific stop words—namely "am," "is," and "are"—from English text. These words, while grammatically important, often do not contribute to the semantic understanding of the text. By identifying and removing them, we aim to streamline the text data, making it more suitable for further analysis or machine learning applications.
# Objectives:
1. Text Analysis: Develop a method to identify and extract the words "am," "is," and "are" from a given English text.
2. Stop Word Removal: Implement an algorithm to remove these words from the text while preserving the overall structure and meaning of the sentences.
3. Evaluation: Assess the impact of removing these stop words on the readability and utility of the text for NLP tasks.

# For Example:
#text:
In the heart of the Whispering Woods, where sunlight filtered through the dense canopy like golden threads, there lived a peculiar creature named Luma. Luma was no ordinary forest dweller; she was a luminescent fox with fur that shimmered like starlight and eyes that glowed like twin moons. The animals of the forest revered her, for she was said to be the guardian of the woods, a spirit born from the first beam of moonlight that ever touched the earth.
# OUT PUT:
['the', 'of', 'like', 'a', '.', 'was', 'that', 'Luma', 'forest', 'she', 'In', 'heart', 'Whispering', 'Woods,', 'where', 'sunlight', 'filtered', 'through', 'dense', 'canopy', 'golden', 'threads,', 'there', 'lived', 'peculiar', 'creature', 'named', 'no', 'ordinary', 'dweller;', 'luminescent', 'fox', 'with', 'fur', 'shimmered', 'starlight', 'and', 'eyes', 'glowed', 'twin']




![Screenshot (10)](https://github.com/user-attachments/assets/b3cf96c1-ca2f-4083-869f-fd3db973ea21)

