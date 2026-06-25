from summarizer import generate_summary

text = """
Bachelor of Engineering in Computer Engineering.
CGPA 8.9.
Completed internship at ABC Company.
Skills include Python, Java and SQL.
Participated in hackathons and technical events.
"""

summary = generate_summary(text)

print(summary)