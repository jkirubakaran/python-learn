from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"Input file is {len(indata)} bytes")

print(f"Does output file exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

in_file.close()
out_file.close()

print("Done")
