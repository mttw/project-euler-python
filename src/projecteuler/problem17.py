"""If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? """
from projecteuler import sum_of
import re

dict = {
        0 : 'zero',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
        20 : 'twenty',
        30 : 'thirty',
        40 : 'forty',
        50 : 'fifty',
        60 : 'sixty',
        70 : 'seventy',
        80 : 'eighty',
        90 : 'ninety',
        100 : 'hundred',
        1000 : 'thousand',
        }


def say_less_100(num):
    if num < 20:
        return dict[num]
    elif num % 10:
        return dict[num /10 *10] + " " + dict[num % 10]
    else:
        return dict[num /10 *10]
    


def say(num):
    word = ''
    str_num = str(num)
    pos = len(str_num) - 1
    for s in str_num:
        if (pos > 1):
            if(int(s)):
                word += " " + dict[int(s)]
                word += " " + dict[10**pos]
            pos -= 1
    
    if num %100 != 0:
            if(len(word) > 0):
                word += " and "            
            
            word += say_less_100(num % 100)
    
    return word
            

def number_of_letters_for_number(n):
    def strip_spaces(text):
        return re.sub("\s+", "", text)
    return len(strip_spaces(say(n)))


if __name__ == '__main__':
    N = 1000
    result = sum_of([number_of_letters_for_number(i) for i in range(1, N+1)])
    print("If all the numbers from 1 to %(N)d were written out in words, %(result)d letters would be used" % vars())
