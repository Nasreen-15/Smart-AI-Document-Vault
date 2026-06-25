from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def generate_summary(text):

    if len(text.strip()) < 100:
        return text

    parser = PlaintextParser.from_string(
        text,
        Tokenizer("english")
    )

    summarizer = LsaSummarizer()

    summary = summarizer(
        parser.document,
        3
    )

    result = ""

    for sentence in summary:
        result += str(sentence) + "\n"

    return result