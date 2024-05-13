import os
import time
from PyPDF2 import PdfReader
import random
import re
import numpy as np


def get_words_from_pdf(file_path):
    pdf = PdfReader(file_path)
    words = []

    for page in pdf.pages:
        text = page.extract_text()
        page_words = text.split()
        page_words = [word.lower().replace(" ", "") for word in page_words]
        words.extend(page_words)

    words_to_exclude = [
        "difficulty",
        "level:",
        "one",
        "two",
        "three",
        "louisianaleadershipinstitute.org",
    ]

    words = [
        word for word in words if word not in [w.lower() for w in words_to_exclude]
    ]
    words = list(set(words))

    random.shuffle(words)

    return words


def get_words_from_pdf_round3(file_path):
    pdf = PdfReader(file_path)
    words = np.array([])
    parts_of_speech = []
    definitions = []

    pattern = (
        r"(.+)(?:noun|adjective|adverb|verb|plural noun|geographical entry|trademark)"
    )
    skip_header = True

    for page in pdf.pages:
        text = page.extract_text()

        if skip_header:
            header_end_index = text.find("round three study list (spelling)")
            if header_end_index != -1:
                text = text[
                    header_end_index + len("round three study list (spelling)") :
                ]
                skip_header = False

        matches = re.findall(pattern, text)
        matches = [x.strip().lower() for x in matches]
        words = np.hstack((words, np.array(matches)))
    # print(words)
    # print(len(words))

    return words


def speak(word):
    # os.system(f"say -v Tessa {word}")
    os.system(f"say -v Reed {word}")


def scripps_round1():
    file_path = "LevelTwoBee.pdf"
    words = get_words_from_pdf(file_path)

    correct = 0
    incorrect = 0

    for word in words:
        while True:
            speak(word)
            print(
                "Please enter the spelling of the word you heard or type 'r' to hear it again:"
            )
            user_input = input()
            if user_input.lower() == "r":
                continue
            elif user_input.lower() == word:
                print("Correct!")
                correct += 1
            else:
                print("Incorrect. The correct spelling is: ", word)
                incorrect += 1
            break
        time.sleep(0.1)
    print(
        "You spelled",
        correct,
        "word(s) correctly and",
        incorrect,
        "word(s) incorrectly.",
    )


def scripts_round3():
    file_path = "round3_words.pdf"
    words = get_words_from_pdf_round3(file_path)
    random.shuffle(words)
    correct = 0
    incorrect = 0

    for word in words:
        while True:
            speak(word)
            print(
                "Please enter the spelling of the word you heard or type 'r' to hear it again:"
            )
            user_input = input()
            if user_input.lower() == "r":
                continue
            elif user_input.lower() == word:
                print("Correct!")
                correct += 1
            else:
                print("Incorrect. The correct spelling is: ", word)
                incorrect += 1
            break
        time.sleep(0.1)
    print(
        "You spelled",
        correct,
        "word(s) correctly and",
        incorrect,
        "word(s) incorrectly.",
    )


if __name__ == "__main__":
    pass
    # scripps_round1()

    scripts_round3()
