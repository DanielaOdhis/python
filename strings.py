a='hello world'
print(a[1]) #prints e

#You can assign a multiline string to a variable by using three quotes (single or double):
a = '''My name is
xo. I am a
girl.'''
print(a)

for x in "banana":
  print(x) #prints b a n a n a

print(len(a)) #prints 11

txt = "The best things in life are free!"
print("free" in txt) #prints True

#To check if a certain phrase or character is present in a string, we can use the keyword in.
if "free" in txt:
  print("Yes, 'free' is present.")
else:
    print("No, 'free' is not present.")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
else:
    print("Yes, 'expensive' is present.")

#Slicing
b = "Hello, World!"
print(b[2:5]) #prints llo (from position 2 to position 5 (not included))
print(b[:5]) #prints Hello (from the start to position 5 (not included))
print(b[2:]) #prints llo, World! (from position 2 to the end)
#Use negative indexes to start the slice from the end of the string:
print(b[-5:-2]) #prints orl (from position -5 to position -2 (not included))

#Modify Strings
a = "Hello, World!"
print(a.upper()) #prints HELLO, WORLD!
print(a.lower()) #prints hello, world!
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
print(a.strip()) #removes any whitespace from the beginning or the end
#The replace() method replaces a string with another string:
print(a.replace("H", "J")) #prints Jello, World!
print(a.split(",")) #returns ['Hello', ' World!']