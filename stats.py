def get_num_words(text):
  return len(text.split())

def word_count(text):
  words = list(text.lower())
  counts = {}
  for word in words:
    if word in counts:
      counts[word] = counts[word] + 1
    else:
      counts[word] = 1
  return counts

def sort_dictionary(dict):
  list = []
  for char in dict:
    list.append({"char": char, "num": dict[char]})
  list.sort(key=sort_on)
  return list

def sort_on(items):
  return items["num"]