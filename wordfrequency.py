from collections import Counter

def most_frequent_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            
            words = text.split()

            word_counts = Counter(words)

            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

            print("Most frequent words in the file:")
            for word, count in sorted_words:
                print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <filename>")
    else:
        filename = sys.argv[1]
        most_frequent_words(filename)
