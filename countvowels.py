text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count = count + 1

print("The number of vowels is:", count)
