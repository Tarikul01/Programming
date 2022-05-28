import nltk
import pip
import xlrd
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tag import pos_tag
# nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus.reader import wordlist
import nltk
# nltk.download('averaged_perceptron_tagger')
# --------------------------------------------------------------------get excel data ---------------------------------------
# Give the location of the file
from numpy.core.defchararray import isdigit

loc = ("C:\python code\Cricket Score.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
# n=sheet.nrows;
# m=sheet.ncols;
arr=[]
# for row in  range(1,4):
#     for col in range(3):
#         print(sheet.cell_value(row,3),end=' ')
        # arr.append(sheet.cell_value(row,3))
        # print(arr)
    # print()
total_run=0
total_actual_run=0
rc=0;
wc=0;

for  value in range(1,67):
    # arr.append((sheet.cell_value(value,3)))
    # print(sheet.cell_value(value,0));
    # print(sheet._cell_values(value,1))
    # print(sheet.cell_value(value,2))
    # print(sheet.cell_value(value,3))
    # print(sheet.cell_value(value,4))

    text=sheet.cell_value(value,3)
    # print(text)
    # print(sheet.cell_value(value,2))
    # print(int(sheet.cell_value(value,5)))
    actula_run=int(sheet.cell_value(value,5))
    total_actual_run+=actula_run


    tokenized_text_sent = sent_tokenize(text)
    tokenized_text_word = word_tokenize(text)
    fdist = FreqDist(tokenized_text_word)
    # print(fdist)
    # print(fdist.most_common(5))

    # Show  grapical representation representation
    # fdist.plot(30, cumulative=False)

    stop_words = set(stopwords.words("english"))
    filtered_sent = []
    for w in tokenized_text_word:

        if w not in stop_words:
            filtered_sent.append(w)
    # print("Filterd Sentence:", filtered_sent,end='\n')
    ps = PorterStemmer()
    root_word=[];
    for w in filtered_sent:
        rootWord = ps.stem(w)
        root_word.append((rootWord))
    remove_duplicate=[]
    for word in root_word:
        if(word not in remove_duplicate):
            remove_duplicate.append(word)
    # print(remove_duplicate)

    def filter(value):
        value=value.lower()
        if(isdigit(value) or value in ['run','four','six','no-ball']):
            return True
    e_run=[]
    # print(remove_duplicate)
    for  char in remove_duplicate:
        if(filter(char)):
            e_run.append(char)
    t_run = ['four', 'six']
    sum=0
    # print(e_run)
    for i in range(len(e_run)):
       if(isdigit(e_run[i])):
           sum+=int(e_run[i])
       elif e_run[i]=='four':
           sum+=4
       elif e_run[i]=='six':
           sum+=6
    #     if isdigit(e_run[i]):
    #      if e_run[i+1]=='run':
    #           sum+=int(e_run[i])
    #     if e_run[i] in t_run:
    #         if e_run[i]=='four':
    #             sum+=4
    #         else:
    #             sum+=6
    #         sum+=4 if t_run.index(i)==0 else 6
    # print(sum)
    total_run+=sum
    if sum==actula_run:
        rc+=1
    else:
        wc+=1

    # # print(sheet.cell_value(value,0),end='   ')
    # # print(sheet.cell_value(value, 1), end='   ')
    # # print(sheet.cell_value(value, 2), end='   ')
    # # print(sum);
    # print(remove_duplicate)
print(total_actual_run)
print(total_run)
print(rc,wc,rc+wc)
result=(rc*100)/(wc+rc)
print(result)







