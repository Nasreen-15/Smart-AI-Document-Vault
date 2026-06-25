def classify_document(text):

    text = text.lower()

    if (
        "cgpa" in text or
        "semester" in text or
        "university" in text or
        "engineering" in text
    ):
        return "Academic"

    elif (
        "resume" in text or
        "skills" in text or
        "experience" in text or
        "project" in text
    ):
        return "Professional"

    elif (
        "internship" in text or
        "certificate" in text
    ):
        return "Achievement"

    elif (
        "aadhaar" in text or
        "uidai" in text or
        "pan card" in text
    ):
        return "Identity"

    else:
        return "Other"