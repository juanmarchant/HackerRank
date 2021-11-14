if __name__ == '__main__':
    s = input()
    
    def reset_(count):
        count = 0 
        return count

    def result(count_):
        result = True if count_ > 0 else False
        print(result)

    count = 0

    for letter in s:
        if letter.isalnum():
            count += 1

    result(count)

    count = reset_(count)

    for letter in s:
        if letter.isalpha():
            count += 1

    result(count)

    count = reset_(count)

    for letter in s:
        if letter.isdigit():
            count += 1

    result(count)

    count = reset_(count)

    for letter in s:
        if letter.islower():
            count += 1

    result(count)

    count = reset_(count)

    for letter in s:
        if letter.isupper():
            count += 1

    result(count)

    #  SECOND TIME I DID IT 
    # print(any(i.isalnum() for i in s))
    # print(any(i.isalpha() for i in s))
    # print(any(i.isdigit() for i in s))
    # print(any(i.islower() for i in s))
    # print(any(i.isupper() for i in s))