#Extract all words starting with a vowel from a sentence using comprehension

s1="Python is a easy lanuguage"
vowels="aeiouAEIOU"
V=[ w for w in s1.split() if w[0] in vowels]
print(V)