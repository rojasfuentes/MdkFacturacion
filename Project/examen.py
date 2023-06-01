def getSubstringCount(s):
    count = 0
    subtrings = []
    current_count = 0
    
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i+1]:
            current_count += 1
        else:
            count += current_count +1
            current_count = 0
    
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getSubstringCount(s)

    fptr.write(str(result) + '\n')

    fptr.close()