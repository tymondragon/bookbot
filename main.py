from stats import *
import sys

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

path = sys.argv[1]

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def main():
  text = get_book_text(path)
  num_words = get_num_words(text)
  counts = word_count(text)
  sorted_list = sort_dictionary(counts)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for dict in sorted_list:
    char = dict["char"]
    if char.isalpha():
     print(f"{char}: {dict["num"]}")
  print("============= END ===============")
  

main()