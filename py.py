from hazm import Normalizer, word_tokenize, stopwords_list
from collections import Counter

# Normalizer for normalizing the text
normalizer = Normalizer()

# Function to extract keywords
def extract_keywords(text, num_keywords=40):
    # Normalize the text
    normalized_text = normalizer.normalize(text)
   
    # Tokenize the text
    words = word_tokenize(normalized_text)
   
    # Remove stopwords (common words like 'و', 'در', etc.)
    stopwords_list()
    filtered_words = [word for word in words if word not in stopwords_list() and len(word) < 200]
   
    # Count word frequencies
    word_frequencies = Counter(filtered_words)
   
    # Get the most common words
    common_words = word_frequencies.most_common(num_keywords)
   
    # Return the top N keywords
    return [word[0] for word in common_words]

# Sample input text
input_text = "hello my name is ali and i work as ai developer and i live in tehran i went to mashhad last year and iam 23 years old"



# Extract keywords from the text
keywords = extract_keywords(input_text)

# Print the result
print("Extracted Keywords:")
print(keywords)
print(input_text)