#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Answer 01


# In[2]:


import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


# In[ ]:


# Answer 02


# In[3]:


import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))


# In[ ]:


# Answer 03


# In[4]:


import re
def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))


# In[ ]:


# Answer 04


# In[5]:


import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


# In[ ]:


# Answer 05


# In[6]:



# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']


# In[ ]:


# Answer 06


# In[7]:


import re
def text_match(text):
        patterns = 'ab{3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("abbb"))
print(text_match("aabbbbbc"))


# In[ ]:


# Answer 06


# In[8]:


import re
text = "UpperCaseSplitString"
res = re.findall('[A-Z][^A-Z]*', text)
print(res)
#OUTPUT: ['Upper', 'Case', 'Split', 'String']


# In[ ]:


# Answer 07


# In[9]:


import re
def text_match(text):
        patterns = 'ab?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("aabbc"))


# In[ ]:


# Answer 08


# In[10]:


import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))


# In[ ]:


# Answer 09


# In[11]:


import re
def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))


# In[ ]:


# Answer 10


# In[12]:


import re
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))


# In[ ]:


# Answer 11


# In[13]:


import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))


# In[ ]:


# Answer 12


# In[14]:


import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))


# In[ ]:


# Answer 13


# In[15]:


import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[ ]:


# Answer 14


# In[16]:


#importing re functions
import re
#storing the value of datestring in a variable
datestring = '31-08-2022'
#use re.match() functions to match the datestring
str =re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
#printing the str.group()
print ("The first input date string is", str.group())
#again declaring the datestring variable with different date format
datestring = '2022-08-31'
#matching the datestring with re.match() functions.
str=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
#printing the str
print ("Matching both the date input if it's in the same format or not:", str)


# In[17]:


# Answer 15


# In[18]:


import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Matched!')
    else:
        print('Not Matched!')
		


# In[19]:


# Answer 16


# In[20]:


import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' %     (match.re.pattern, match.string, s, e))


# In[21]:


# Answer 17


# In[22]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)
	


# In[23]:


# Answer 18


# In[24]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
	


# In[26]:


# Answer 19


# In[27]:


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[28]:


# Answer 20


# In[29]:


import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#find all the words starting with 'a' or 'e'
list = re.findall("[ae]\w+", text)
# Print result.
print(list)


# In[30]:


# Answer 21


# In[31]:


import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())
	


# In[1]:


# Answer 22


# In[2]:


# import module for regular expression and collections
import re
#input
string='ab12cd123ef23'
#seperate number from string
number = re.findall('\d+', string)
#convert it into integer
number = map(int, number)
print("Max_value:",max(number))


# In[3]:


# Answer 23


# In[4]:


import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))


# In[5]:


# Answer 24


# In[7]:


# Python3 code to find sequences of one upper
# case letter followed by lower case letters
import re

# Function to match the string
def match(text):
        
       # regex
       pattern = '[A-Z]+[a-z]+$'
        
       # searching pattern
       if re.search(pattern, text):
               return('Yes')
       else:
               return('No')

# Driver Function
print(match("Geeks"))
print(match("geeksforGeeks"))
print(match("geeks"))


# In[8]:


# Answer 25


# In[9]:


# Python program to remove duplicate words
# using Regular Expression or ReGex.
import re
 
 
# Function to validate the sentence
# and remove the duplicate words
def removeDuplicateWords(input):
 
    # Regex to matching repeated words
    regex = r'\b(\w+)(?:\W+\1\b)+'
 
    return re.sub(regex, r'\1', input, flags=re.IGNORECASE)
 
 
# Driver Code
 
# Test Case: 1
str1 = "Good bye bye world world"
print(removeDuplicateWords(str1))
 
# Test Case: 2
str2 = "Ram went went to to his home"
print(removeDuplicateWords(str2))
 
# Test Case: 3
str3 = "Hello hello world world"
print(removeDuplicateWords(str3))
 
# This code is contributed by yuvraj_chandra


# In[10]:


# Answer 26


# In[11]:


import re

regex_expression = '[a-zA-z0-9]$'

def check_string(my_string):

   if(re.search(regex_expression, my_string)):
      print("The string ends with alphanumeric character")

   else:
      print("The string doesnot end with alphanumeric character")


my_string_1 = "Python@"
print("The string is :")
print(my_string_1)
check_string(my_string_1)

my_string_2 = "Python1245"
print("\nThe string is :")
print(my_string_2)
check_string(my_string_2)


# In[12]:


# Answer 27


# In[13]:


# function to print all the hashtags in a text
def extract_hashtags(text):

	# initializing hashtag_list variable
	hashtag_list = []

	# splitting the text into words
	for word in text.split():

		# checking the first character of every word
		if word[0] == '#':

			# adding the word to the hashtag_list
			hashtag_list.append(word[1:])

	# printing the hashtag_list
	print("The hashtags in \"" + text + "\" are :")
	for hashtag in hashtag_list:
		print(hashtag)


if __name__ == "__main__":
	text1 = "GeeksforGeeks is a wonderful #website for #ComputerScience"
	text2 = "This day is beautiful ! #instagood #photooftheday #cute"
	extract_hashtags(text1)
	extract_hashtags(text2)


# In[14]:


# Answer 28


# In[15]:



#input string
str = "This is Python \u500cPool"
 
#encode() method
strencode = str.encode("ascii", "ignore")
 
#decode() method
strdecode = strencode.decode()
 
#output
print("Output after removing Unicode characters : ",strdecode)


# In[16]:


# Answer 29


# In[21]:


test_str = "gfg at 2021-01-04"

# Split the input string into words and iterate through them
words = test_str.split()
for word in words:
	if len(word) == 10 and word[4] == "-" and word[7] == "-":
		print(word)
		break


# In[22]:


# Answer 30


# In[23]:


import re
text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text))


# In[ ]:




