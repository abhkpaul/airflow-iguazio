import sys

def testFuncC():
    print('Executing testFuncC')

if __name__ == '__main__':
    globals()[sys.argv[1]]()