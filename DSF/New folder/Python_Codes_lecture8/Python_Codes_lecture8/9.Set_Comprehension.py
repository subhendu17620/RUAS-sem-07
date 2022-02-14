#The demonstration is to create a Set Comprehension
sentence = "The cat in the hat had two sidekicks, thing one and thing two."

#make sentence entirely lowercase and then remove the comma and the period. This can be done with the
#  lower() and replace() functions. Then, use the split() function to separate it into a list of
#  words, and from there generate a set of all the unique words
words = sentence.lower().replace('.', '').replace(',', '').split()

unique_words = {word for word in words}
print ("The Set Comprehension created : ",end="")
print(unique_words)

unique_word2 = {word for word in words if len(word) <= 3}
print ("The Set Comprehension created after condition : ",end="")
print(unique_word2)

unique_word3 = {word.capitalize() if word[0] == 'h' else word for word in words}
print ("The Set Comprehension created after capital a character : ",end="")
print(unique_word3)