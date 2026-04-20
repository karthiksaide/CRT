def Reverse_str(s):
    return s[::-1] 

print(Reverse_str("abc"))

def is_palindrome(s):
print(is_palindrome("madam"))
def Frequency_count(s):
    d={}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d
print(Frequency_count("abcabc"))