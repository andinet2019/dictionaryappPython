import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def dictionary(word):
    word=word.lower()
    if word in data:
       return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0 :
          answer=  input("did you mean %s instead? " % get_close_matches(word,data.keys())[0] )
          answer=answer.lower()
          if answer== "yes":
              return data[get_close_matches(word,data.keys())[0]]
          elif answer=="no":
              return "Sorry the word doesnot exist in our dictionary!"
          else: return "I didnot understand your entry."

    else:
         return "Sorry the word doesnot exist in our dictionary!"
while  True:

 x = input("Enter a word to get the meaning\n").lower()

 output= dictionary(x)
 if type(output)==list:
     for item in output:
         print(item)
 else:print(output)









