# imports whole file
import Python.ModuleandPackages.modelss.maths as maths
print(maths.addition(12,12))

# import the perticular method of function from that file
from Python.ModuleandPackages.modelss.maths import addition

print(addition(12,12))

from modelss import hello,maths


# if there is folder inside another folder then what will have to write?
# suppose there is model folder inside modelss then

# form modelss.model import hello, maths