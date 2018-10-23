def countLines(name):
    return len(lines(name))


def countChars(name):
    charcount = 0
    for line in lines(name):
        charcount += len(line)
    return charcount


def lines(name):
    return open(name).readlines()


def test(name):
    print('Lines: %s' % countLines(name))
    print('Chars: %s' % countChars(name))


# Tests
if __name__ == '__main__':
    testfile = 'datafile.txt'
    test(testfile)
