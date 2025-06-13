# Create a string and print it
text = "Hello, Python!"
print("Original String:", text)
# Find the length of the string
print("Length of String:", len(text))
# Access the first and last character of the string
print("First Character:", text[0])
print("Last Character:", text[-1])
# Convert the string to uppercase and lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
# Check if a word is present in the string
if "Python" in text:
    print("Yes, 'Python' is in the string.")
else:
    print("No, 'Python' is not in the string.")
# Concatenate two strings
greeting = "Hi "
name = "Narayan"
full_greeting = greeting + name
print("Concatenated String:", full_greeting)
