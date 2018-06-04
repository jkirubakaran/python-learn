from sys import argv

script, filename = argv

print(f"Erasing file {filename}")
print("If you want to proceed hit RETURN")

input("?")

print("Truccating the file...")
target = open(filename, 'w')
target.truncate()

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print("Closing...")
target.close()
