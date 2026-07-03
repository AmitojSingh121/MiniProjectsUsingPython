import wikipedia

while True:
    query = input("Q: ")
    wikipedia.set_lang("en")
    print(wikipedia.summary(query,sentences=2))