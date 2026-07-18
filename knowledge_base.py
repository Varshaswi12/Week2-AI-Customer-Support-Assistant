def load_faq():
    with open("data/faq.txt", "r", encoding="utf-8") as file:
        return file.read()