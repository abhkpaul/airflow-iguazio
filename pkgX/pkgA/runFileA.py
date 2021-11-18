import sys

def testFuncA():
    print('Executing testFuncA')

if __name__ == '__main__':
    globals()[sys.argv[1]]()