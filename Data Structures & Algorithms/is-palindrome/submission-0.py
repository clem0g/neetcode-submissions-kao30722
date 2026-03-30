import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = []
        right = []
        rule_book = str.maketrans('','',string.punctuation + string.whitespace)
        text = s.translate(rule_book)
        final_text = text.lower()

        for i in range(len(final_text)):

            left.append(final_text[i])
            right.append(final_text[len(final_text)-1-i])

        if left == right:
            return True
        else:
            return False