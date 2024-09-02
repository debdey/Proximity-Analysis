import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict, Counter
import itertools

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Load the CSV file
file_path = 'your_file.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Assuming the verbatim text is in a column named 'text'
texts = df['text'].astype(str).tolist()

# Preprocess the text: tokenization, stopwords removal
stop_words = set(stopwords.words('english'))
processed_texts = []

for text in texts:
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    processed_texts.append(filtered_tokens)

# Define the target words or phrases
target_words = ['your', 'target', 'words']  # Replace with words you're interested in

# Create a co-occurrence dictionary
co_occurrence = defaultdict(Counter)
window_size = 5  # Define the proximity window size (e.g., 5 words before and after)

for tokens in processed_texts:
    for i, word in enumerate(tokens):
        if word in target_words:
            window = tokens[max(i - window_size, 0):min(i + window_size + 1, len(tokens))]
            window.remove(word)  # Remove the target word from its own window
            co_occurrence[word].update(window)

# Display the proximity results
for word, counter in co_occurrence.items():
    print(f"Proximity analysis for '{word}':")
    for co_word, count in counter.most_common(10):  # Show the top 10 co-occurring words
        print(f"  {co_word}: {count}")
