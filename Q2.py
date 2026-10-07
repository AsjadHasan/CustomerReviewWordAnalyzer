import string
from collections import Counter

num_reviews = int(input("Number of reviews: "))

stop_words = {"the", "is", "and", "was", "but", "a", "an", "of", "to"}

all_words = []

for i in range(num_reviews):
    review = input("Review: ")

    review = review.lower()

    review = review.translate(str.maketrans("", "", string.punctuation))

    words = review.split()

    for word in words:
        if word not in stop_words:
            all_words.append(word)

word_counts = Counter(all_words)

top_words = word_counts.most_common(3)

print("Top words:", top_words)