import re
def count_words(text):
    words=text.lower()
    words=re.split(r'[.,!?;:\s]\s*',words) 
    words = [w for w in words if w]          
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return  word_count  
r=input("Enter a string")
print(count_words(r))