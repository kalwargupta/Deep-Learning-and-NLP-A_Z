#Building a chatbot with Deep NLP


#importing the libraries
import numpy as np
import tensorflow as tf
import re
import time





#######Part 1 Data Preprocessing #######



##### Import Dataset####
lines=open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conversations=open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

#####creating a dictionary that maps each line and its id
id2line={}
for line in lines:
    _line=line.split(' +++$+++ ')
    if len(_line)==5:
        id2line[_line[0]]=_line[4]

########Creating the list of all conversation
conversation_ids=[]
for conversation in conversations[:-1]:
    _conversation=conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
    conversation_ids.append(_conversation.split(','))
    
        
