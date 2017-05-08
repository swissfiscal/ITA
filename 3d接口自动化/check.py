
def checkhost(filename):
    with open(filename) as f:
        input = f.read()
    print input
filename = r'C:\WINDOWS\system32\drivers\etc\HOSTS'
checkhost(filename)