sentence = "List Comprehensions are the Greatest!"
vowels = ['a', 'e', 'i', 'o', 'u']
text = list(sentence)

new_sentence = [letter for letter in text if letter.lower() not in vowels]
print(new_sentence)





#convert text to a list of characters















