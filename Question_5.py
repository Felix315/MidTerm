# Write a function that finds all the occurrences of a certain pattern, that starts with “un” has unlimited number of letters and ends with “an”
# The function takes 1 parameter: the text to look into and returns the number of matches.
# Use only the things we have learned in class. Give some explanations besides the code.

def count_pattern_words(text):
    """
    Counts words that start with 'un' and end with 'an' in the given text.

    :param text: The input string to search.
    :return: The count of words that match the pattern.
    """
    punctuation = ",.!?;:\"'()[]{}-*<>"
    for p in punctuation:
        text = text.replace(p, " ")  # Remove punctuation

    words = text.split()  # Split into words
    count = 0

    for word in words:
        if word.startswith("un") and word.endswith("an"):
            count += 1  # Increase count if the word matches

    return count


# Example usage:
sample_text = "unbeaten unseen unknown unhuman unusual unclean unbeatable"
print(count_pattern_words(sample_text))  # Output: 2 (unclean, unbeaten)