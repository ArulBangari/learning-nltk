from nltk.book import *
import matplotlib.pyplot as plt
import os

width = os.get_terminal_size().columns if os.isatty(1) else 80

print('-' * width)
print('To import all books, run "from nltk.book import *"')
print('To get the name of a book, run print(text[number]), for example text1, text2')
print(text1)
print('-' * width)

print('To search text, use the .concordance() function')
print('text1.concordance("monstrous")')
print(text1.concordance("monstrous"))
print('-' * width)

print('To get similar words to a word, use the .similar() function')
print('text1.similar("monstrous")')
print(text1.similar("monstrous"))
print('-' * (width//2))
print('text2.similar("monstrous")')
print(text2.similar("monstrous"))
print('As you can see, text1 and text2 give very different results. This is because the context they are used in are different')
print('-' * width)

print('To get common contexts (words that are similar to 2+ words), use the .common_contexts() method')
print('text1.common_contexts(["monstrous", "very")]')
print(text2.common_contexts(["monstrous", "very"]))
print('-' * width)

print('To get the location of words in a text, use the, .dispersion_plot() function')
print('text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])')
print(text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]))
plt.show()
print('-' * width)

print('To generate random text in the style of a text, use the .generate() method')
print("text3.generate()")
print(text3.generate())
print('-' * width)

print('To get the number of words and punctuation symbols in the text(tokens), use the len() function')
print('len(text3)')
print(f'Text3 has {len(text3)} words and punctuation marks.')
print('-' * width)

print('To get the distinct words and punctuation marks in a text, use the set() function')
print('sorted(set(text3))')
print(sorted(set(text3))[0:10])
print(f'Text3 has {len(sorted(set(text3)))} distinct words and punctuation marks.')
print('-' * width)

print('To calculate the measure of the lexical richness, divide the number of tokens by the number of distinct tokens')
print(print(f"The lexical richness is {len(set(text3)) / len(text3) * 100}%"))
print('-' * width)

print('To get a frequency distributions of a text, use the FreqDist() method')
print('fdist1 = FreqDist(text1)')
fdist1 = FreqDist(text1)
print('To get the x most common words, use .most_common(x)')
print('print(fdist1.most_common(50))')
print(fdist1.most_common(50))
print('-' * width)

print('To get the words that have more than 7 letters and occur more than 7 times, do:')
print('fdist5 = FreqDist(text5)')
print('sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)')
fdist5 = FreqDist(text5)
print(sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7))
print('Getting the long words will help to characterize a piece of text')
print('-' * width)

print("A collocation is a sequence of words that occur together unusually often. For example, red wine. These collocations can't be substituted with words that have similar meanings (maroon wine).")
print("To get collocations, extract the list of words pairs from a text (bigrams). To do it, use the bigrams() function")
print("list(bigrams(['more', 'is', 'said', 'than', 'done']))")
print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))
print("Collocations are pretty much frequent bigrams. To get all the collocations in a text, use the .collocations method")
print("text4.collocations()")
print(text4.collocations())