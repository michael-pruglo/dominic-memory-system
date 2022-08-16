import random, math, sys


def generate(n, columns=None, seed=None):
    if columns is None or columns<1:
        columns = math.ceil(n/4)
    if seed is None:
        seed = random.randrange(sys.maxsize)
        print(f"Remember args for recall: ({n} {columns} {seed})\n")
    random.seed(seed)

    s = ""
    for i in range(n):
        s += str(random.randint(0,9))
        if (i+1)%(columns*4)==0:
            s += '\n'
        elif (i+1)%4==0:
            s += ' '
    return s+'\n'

def test_recall(n, columns, seed):
    data = generate(n, columns, seed)
    
    print("input what you remember (when you're done press Ctrl+D):")
    inp = sys.stdin.read().strip()
    print(f"\n\n\ncompare:\n{data}")
    correct = total = 0
    for exp,given in zip(data,inp):
        COLOR_RED = "\033[31m"
        COLOR_RESET = "\033[0m"
        color = COLOR_RED if exp!=given else ''

        if exp.isdigit():
            correct += exp==given
            total += 1
        print(color+given+COLOR_RESET, end='')
    print(f"\naccuracy = {correct/total:.3}")

def main():
    print("input what you want to do:")
    print("  g N [COLUMNS]    - generate N-digit number, organize into COLUMNS 4-digit groups")
    print("  r N COLUMNS SEED - test recall")
    
    command, *args = input().strip().split()
    args = list(map(int, args))
    if command=="g":
        assert len(args)<=2
        print(generate(*args))
    elif command=="r":
        assert len(args)==3
        test_recall(*args)
    else:
        print(f'ERROR: unknown command "{command}"')


if __name__ == "__main__":
    main()
