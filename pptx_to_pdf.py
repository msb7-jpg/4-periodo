from collections import Counter

def first_unique_char(text: str):
    char_set = set()
    for index, char in enumerate(text):
        if char not in text[index+1:] and char not in char_set:
            return char
        char_set.add(char)
    return None

# text = "abeabef"
# char = first_unique_char(text)
# print(char)

#include <stdio.h>


for i in range(1000000):
    print(i)

# int main(){
#     for (size_t i = 0; i < 1000000; i++)
#     {
#         printf("%lu\n", i);
#     }
    
# }