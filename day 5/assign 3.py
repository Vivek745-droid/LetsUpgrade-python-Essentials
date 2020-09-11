def sentenceCapitalizer (string1: str):
          sentences = string1.split(", ")
          sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
          string2 = ', '.join(sentences2)
          return string2
print (sentenceCapitalizer("hey this is sai”,I am in mumbai”,...."))