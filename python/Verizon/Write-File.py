import os
os.linesep

with open('Test_File', 'w') as f:
    f.write('Hello D'+ os.linesep)
    f.write('Hello 2D' + os.linesep)
    f.write('Hello 3D' + os.linesep)