import wordcount

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python command.py <filename>")
    else:
        filename = sys.argv[1]
        wordcount.word_count(filename)
