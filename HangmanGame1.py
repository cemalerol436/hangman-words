#this is a hangman game
import random as rd
from tolga import tolga as tl
from melike import melike as mk

hangman_words = ["miedo","respuesta","pedir","mundo","sucio","dejar","correr","lluvioso","nublado"]
hangman_words_eng = ["scared","answer","ask","world","dirty","leave","run","rainy","cloudy"]
real_word =  rd.choice(hangman_words)
letter_qty = len(real_word)
print("-"*letter_qty)

first_guess = tl("ı love you")
#print(type(first_guess))

if len(first_guess) == 1 and first_guess:
    first_guess = first_guess
else:
    first_guess= mk("melike tell us what are u doing there")
addings = []
def letter_harf(wordd):
    i=0
    while i<int(letter_qty):
        l = int(letter_qty)
        if wordd == real_word[i] :
            comlet = wordd
        else:
            comlet = "-"
        i=i+1
        addings.append(comlet)
    print("".join(addings))
letter_harf(first_guess)
second_guess = input("please guess your second letter:")
if second_guess == first_guess:
    print("hop bilader")
    second_guess_try = input("please guess your second letter again:")
    second_guess = second_guess_try
else:
    second_guess_try = ""
addingss=[]
def letter_2harf(worddd):
    i=0
    while i<int(letter_qty):
        l = int(letter_qty)
        if worddd == real_word[i] :
            comlett = worddd
        elif first_guess == real_word[i] :
            comlett = first_guess
        else:
            comlett = "-"
        i=i+1
        addingss.append(comlett)
    print("".join(addingss))
letter_2harf(second_guess)
third_guess = input("please guess your third letter:")
if third_guess == first_guess or third_guess == second_guess or third_guess == second_guess_try:
    print("hop bilader")
    third_guess_try = input("please guess your third letter again:")
    third_guess = third_guess_try
addingsss = []
def letter_2harf(wordddd):
    i=0
    while i<int(letter_qty):
        l = int(letter_qty)
        if wordddd == real_word[i] :
            comlettt = wordddd
        elif first_guess == real_word[i] :
            comlettt = first_guess
        elif second_guess == real_word[i] :
            comlettt = second_guess
        else:
            comlettt = "-"
        i=i+1
        addingsss.append(comlettt)
    print("".join(addingsss))
letter_2harf(third_guess)
print("you are out of guess")
final_guess = input("please guess the word:")
if final_guess==real_word:
    print("Great!!! You got it.")
else:
    print("Sorry! The word was "+real_word)
def finding_eng():
    p=0
    while p<len(hangman_words):
        p=p+1
        if real_word == hangman_words[p]:
            print(real_word +" means " + hangman_words_eng[p].upper() + " in English.")
            break
finding_eng()
