import re

def clean_questions(questions):

    cleaned = []

    for q in questions:

        # remove numbering
        q = re.sub(r'^\d+\.?', '', q)

        # remove marks
        q = re.sub(r'\(\d+\s*marks?\)', '', q)

        # remove extra spaces
        q = q.strip()

        cleaned.append(q)

    return cleaned