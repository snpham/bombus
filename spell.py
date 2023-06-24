import os
import time
from PyPDF2 import PdfReader
import random

def get_words_from_pdf(file_path):
    pdf = PdfReader(file_path)
    words = []

    for page in pdf.pages:
        text = page.extract_text()
        page_words = text.split()
        page_words = [word.lower().replace(" ", "") for word in page_words]  # remove spaces within words
        words.extend(page_words)

    words_to_exclude = ['difficulty', 'level:', 'one', 'two', 'three', 'louisianaleadershipinstitute.org']

    words = [word for word in words if word not in [w.lower() for w in words_to_exclude]]
    words = list(set(words))  # remove duplicates

    random.shuffle(words)

    return words

def speak(word):
    os.system(f"say -v Tessa {word}")  # Change 'Alex' to the voice you want to use
    # os.system(f"say -v Reed {word}")  # Change 'Alex' to the voice you want to use
    # os.system(f"say -v Reed {word}")  # Change 'Alex' to the voice you want to use

file_path = 'LevelTwoBee.pdf'
words = get_words_from_pdf(file_path)

correct = 0
incorrect = 0

for word in words:
    while True:
        speak(word)
        print("Please enter the spelling of the word you heard or type 'r' to hear it again:")
        user_input = input()
        if user_input.lower() == 'r':
            continue
        elif user_input.lower() == word:
            print("Correct!")
            correct += 1
        else:
            print("Incorrect. The correct spelling is: ", word)
            incorrect += 1
        break

    # Add delay to avoid overlap of pronunciation and the next word
    time.sleep(0.1)

print("You spelled", correct, "word(s) correctly and", incorrect, "word(s) incorrectly.")

