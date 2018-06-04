from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here are the contents of the file: {filename}")
print(txt.read())

print("Type your filename again pls:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
