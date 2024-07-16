import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(string):
    unique_characters = set(string)
    return len(unique_characters)

def main():
    input = sys.stdin.read
    data = input().splitlines()

    num_strings = int(data[0])
    results = []
    for i in range(1, num_strings + 1):
        current_string = data[i]
        result = stringConstruction(current_string)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()