words = [word for word in input().split() if word == word[::-1]]
palindrome = input()

palindrome_count = words.count(palindrome)
print(f"{words}\nFound palindrome {palindrome_count} times")