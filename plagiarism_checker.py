import difflib

def check_plagiarism(text1, text2):
    # Split the texts into lines
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()

    # Calculate the similarity ratio between the texts
    similarity = difflib.SequenceMatcher(None, lines1, lines2).ratio()

    return similarity

# Example usage
#The ratio method returns a value between 0 and 1, where 0 means no similarity and 1 means complete similarity.
text1 = """Lorem Ipsum is simply dummy text of the printing and typesetting industry."""
text2 = """Lorem Ipsum is simply dummy text of the printing . """

similarity_ratio = check_plagiarism(text1, text2)
print(f"Similarity ratio: {similarity_ratio}")
