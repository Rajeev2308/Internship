#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Ans_1

a= 'Python Exercises  PHP exercises '
d= a.replace(" ",":")
print(d)


# In[ ]:


#Ans_2

text = input("Enter a String: ")
print("word starting with 'a' or 'e'are...")

word = text.split("")


# In[ ]:


#Ans_6

import re
items = ["example (.com)","hr@fliprobo (.com)", "w3resource", "github (.com)", "Hello (Data Science World"),"Data (Scientist)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))


# In[ ]:


#Ans_7

import re
text = "ImportanceOfRegularExpressionsInPython"
print(re.findall('[A-Z][^A-Z]*', text))


# In[ ]:


#Ans_8


import re
def capital_words_spaces(int1):
  return re.sub(r"(\w)([0-9])", r"\1 \2", int1)

print(capital_words_spaces("RegularExpression1IsAn2ImportantTopic3InPython"))


# In[ ]:


#Ans_9


import re
def capital_words_spaces(str):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str)

print(capital_words_spaces("RegularExpression1IsAn2ImportantTopic3InPython"))


# In[ ]:


#Ans_10

import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The lion is sleeping with its cubs."))
print(text_match("Python_Exercises_1"))


# In[ ]:


#Ans_12


import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('2-3244564'))
print(match_num('2-3244564'))


# In[ ]:


#Ans_13

import re
ip = "314.01.034.198"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[ ]:


#Ans_15

import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')


# In[ ]:


#Ans_16

import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' %     (match.re.pattern, match.string, s, e))


# In[ ]:


#Ans_17

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# In[ ]:


#Ans_18

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[ ]:


#Ans_19

import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2023-05-05"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[ ]:


#Ans_21

import re

text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


# In[ ]:


#Ans_22

import re

string='My marks in each semester are: 947, 896, 926, 524, 734, 950, 642' 

number = re.findall('\d+', string)

number = map(int, number)
print("Max_value:",max(number))


# In[ ]:


#Ans_23

import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("RegularExpressionIsAnImportantTopicInPython"))


# In[ ]:


#Ans_24

import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("Welcome"))
print(text_match("WelcomeHomewelcome Hello Welcome"))
print(text_match("Welcomes you"))


# In[ ]:


#Ans_25

import re

def removeDuplicatesFromText(text):
    regex = r'\b(\w+)(?:\W+\1\b)+' 
    return re.sub(regex, r'\1', text, flags=re.IGNORECASE)

str1 = "Hello hello world world"
print(removeDuplicatesFromText(str1))


# In[ ]:


#Ans_26

import re
regex = '[a-zA-z0-9]$'

def check_alpha_numeric(string):
 if(re.search(regex, string)):
     print("The string is ending with an alphanumeric character. \n")

 else:
    print("The string is not ending with an alphanumeric character. \n")


check_alpha_numeric("pitchumca@") 
check_alpha_numeric("pitchumca123") 

