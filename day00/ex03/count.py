def text_analyzer(text=""):
    "\nThis function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
    while (len(text) == 0):
        text = input("What is the text to analyse?\n")
    print("The text contains " + "%s" % len(text) + " characters:")
    print("- " + "%s" % sum(c.isupper() for c in text) + " upper letters")
    print("- " + "%s" % sum(c.islower() for c in text) + " lower letters")
    print("- " + "%s" % (len(text) - sum(c.isalnum() for c in text) - sum(c.isspace() for c in text)) + " punctuation marks")
    print("- " + "%s" % sum(c.isspace() for c in text) + " spaces")
