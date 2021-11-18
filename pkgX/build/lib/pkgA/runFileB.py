import sys
from pkgX.pkgB import runFileC

def testFuncB():
    print('Executing testFuncB')
    runFileC.testFuncC()

if __name__ == '__main__':
    globals()[sys.argv[1]]()