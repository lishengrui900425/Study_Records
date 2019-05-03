# import a module named argv
#from sys import argv
# use argv to get a filename
#script, filename = argv
# open the file user inputted and return a corresponding file object. 
#txt = open(filename)
# print a few message and use the method read() to read the txt's content.
#print(f"Here's your file {filename}:")
#print(txt.read())

print("Type the filename again:")
file_again = input(">")

text_again = open(file_again)

print(text_again.read())
