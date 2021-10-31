import sys

def sayHello(name):
    print(f"Hello ${name}")

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    print("".join(lines))
