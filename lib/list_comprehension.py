#!/usr/bin/env python3
def return_evens(num_list):
    result = []
    for i in num_list:
        if i % 2 == 0:
            result.append(i)
    return result

print(return_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        

            

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]