# Palindrome Checker

print("===== PALINDROME CHECKER =====")

word = input("Enter a word: ")

reverse_word = word[::-1]

print("Original Word:", word)
print("Reversed Word:", reverse_word)

if word.lower() == reverse_word.lower():
    print("It is a Palindrome")

else:
    print("It is not a Palindrome")