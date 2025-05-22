def pig_latin(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words_not_starting_with_vowel = []

    #break up the sentence into words
    for word in sentence.split():
        #search for words starting with a vowel
        for vowel in vowels:
            if not vowel in word[0]:
                words_not_starting_with_vowel.append(word)
            else:
                return word

    for word in words_not_starting_with_vowel:
        pig_latin_suffix = word[0] + "ay"
        pig_latin_main_part_of_word = word[1:]
        pig_latin_word = pig_latin_main_part_of_word + pig_latin_suffix
    return pig_latin_word

result = pig_latin("awesome")
print(result)

# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")