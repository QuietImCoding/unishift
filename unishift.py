import sys
with open(sys.argv[1], 'r') as infile:
    contents = infile.read()

shift = int(sys.argv[2])
out = ''.join([ chr(ord(k)+shift) for k in contents ])
print(out)
