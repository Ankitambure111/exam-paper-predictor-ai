import re

def extract_questions(text):

    # remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    # remove university/instruction parts
    text = re.sub(r'DR\. BABASAHEB.*?Instructions to the Students:', '', text, flags=re.I)
    text = re.sub(r'\*\*\*End\*\*\*.*', '', text, flags=re.I)

    # split by question labels A), B), C)
    parts = re.split(r'[A-C]\)', text)
import re

def extract_questions(text):

    # normalize spaces
    text = re.sub(r'\s+', ' ', text)

    # remove instructions section
    text = re.sub(r'Instructions to the Students:.*?Marks', '', text, flags=re.I)

    # remove ending section
    text = re.sub(r'\*\*\*End\*\*\*.*', '', text, flags=re.I)

    # split using A) B) C)
    parts = re.split(r'[A-C]\)', text)

    questions = []

    for part in parts:

        part = part.strip()

        if len(part) < 40:
            continue

        # remove CO codes
        part = re.sub(r'CO\s*\d+\s*\d*', '', part)

        # remove Q numbers
        part = re.sub(r'Q\.\d+.*?following\.', '', part)

        questions.append(part.strip())

    return questions
    questions = []

    for part in parts:

        part = part.strip()

        if len(part) < 40:
            continue

        # remove CO numbers and marks
        part = re.sub(r'CO\d+\s*\d*', '', part)

        questions.append(part.strip())

    return questions