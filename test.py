#check if int is even or odd
def even_or_odd(number):
    if (number%2 == 0):
        return "Even"
    else:
        return "Odd"

#cast int to string   
def number_to_string(num):
    return str(num)

#count vowels in string
def get_count(sentence):
    return len([vowel for vowel in sentence if vowel in "AaEeIiOoUu"])