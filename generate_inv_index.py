import string
import csv
import pickle
stopword_file = open('stopwords.txt')
sword = stopword_file.readlines()
stop_words = []
for word in sword:
    stop_words.append(word.strip())
stopword_file.close()

Lines = [] 
column_names = []
with open('data.csv', encoding="latin-1") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            column_names = row
            line_count += 1
        else:            
            Lines.append(row)


def remove_punc(new_doc , word):
    clean_word = word
    for char in clean_word:
        if char in string.punctuation:
            clean_word = clean_word.replace(char, " ", 1)
    clean_word = clean_word.casefold()
    clean_arr = clean_word.strip()
    clean_arr = clean_word.split()
    for w in clean_arr:
        if w not in stop_words and w != "":
            new_doc.append(w)
token_dict = ({})
for line in Lines:
    doc_id = line[0]
    title = line[1]
    abstract = line[2]
    v_title = title.split()
    v_abstract = title.split()
    doc_tokens = []
    for word in v_title: 
        remove_punc(doc_tokens, word)
    for word in v_abstract:
        remove_punc(doc_tokens, word)
    if doc_id in token_dict.keys():
        token_dict[doc_id] = doc_tokens

inverted_index = ({})
for doc_id in token_dict.keys():
    doc = token_dict[doc_id]
    for word in doc: 
        if word in inverted_index.keys():
            for posting in inverted_index[word]:
                if posting[0] == doc_id:
                    posting[1] += 1
        else:
            inverted_index[word] = [[doc_id, 1]]


with open('inverted_index.pickle', 'wb') as f:
    pickle.dump(inverted_index, f)