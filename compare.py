# Compare two files and add the diffs to each other
# Nothing will be removed, then program will only add tags
# Run using python compare.py file1 file2

# Imports
import sys

def checker(index, lis, string):
    for i in range(index, len(lis)):
        if lis[i] == string:
            return i
    return False

print ""
print "###############"
print "# {}".format(sys.argv[0])
print "# Files: {}, {}".format(str(sys.argv[1]), str(sys.argv[2]))
print "###############"
print ""

linesX = []
linesY = []
with open(str(sys.argv[1])) as f:
    linesX = f.readlines()
    if not linesX:
        linesX.append('')

with open(str(sys.argv[2])) as f:
    linesY = f.readlines()
    if not linesY:
        linesY.append('')

x = 0
y = 0


if linesX == linesY:
    print "The files are identical. Exiting program."
    sys.exit(0)

while True:
    if linesX[x] != linesY[y]:
        print "Diff line {} in file {} and line {} in file {}".format(x, str(sys.argv[1]), y, str(sys.argv[2]))
        ret = checker(x, linesY, linesX[x])
        if ret:
            for i in range(x, ret):
                linesX.insert(i, linesY[i])
        else:
            linesY.insert(x, linesX[x])

    x += 1
    y += 1
    if x >= len(linesX) and y >= len(linesY):
            break
    elif x >= len(linesX):
        x -= 1
        for i in range(y, len(linesY)):
            linesX.insert(i, linesY[i])
        break
    elif y >= len(linesY):
        y -= 1
        for i in range(x, len(linesX)):
            linesY.insert(i, linesX[i])
        break

if linesX == linesY:
    with open(str(sys.argv[1]), 'w') as f:
        f.writelines(linesX)
    with open(str(sys.argv[2]), 'w') as f:
        f.writelines(linesY)
    print "The files are now identical. Exiting program."
    sys.exit(0)
