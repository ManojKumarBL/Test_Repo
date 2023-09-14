def word_count(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Initialize a dictionary to store word counts
            word_counts = {}

            # Read each line from the file
            for line in file:
                # Split the line into words
                words = line.split()

                # Iterate through each word and update the word counts
                for word in words:
                    # Remove punctuation and convert to lowercase
                    word = word.strip('.,!?').lower()

                    # Update the word count in the dictionary
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

            # Print each word and its count
            for word, count in word_counts.items():
                print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python wordcount.py <filename>")
    else:
        filename = sys.argv[1]
        word_count(filename)
