def prefix_suffix(string):
    if not string:
        return 0
    arr = [0] * (len(string) + 1)
    for i in range(2, len(arr)):
        arr[i] = arr[i - 1]
        while string[i - 1] != string[arr[i]] and arr[i] > 0:
            arr[i] = arr[arr[i]]
        if string[i - 1] == string[arr[i]]:
            arr[i] += 1
    return arr[-1]


if __name__ == '__main__':
    string = 'a'
    print('Test #1 is', 'Ok.' if prefix_suffix(string) == 0 else 'Fail.')
    string = ''
    print('Test #2 is', 'Ok.' if prefix_suffix(string) == 0 else 'Fail.')
    string = 'asdfghasdfgh'
    print('Test #3 is', 'Ok.' if prefix_suffix(string) == 6 else 'Fail.')
    string = 'aaa'
    print('Test #4 is', 'Ok.' if prefix_suffix(string) == 2 else 'Fail.')
    string = 'aaaabaaaaaa'
    print('Test #5 is', 'Ok.' if prefix_suffix(string) == 4 else 'Fail.')
    string = 'aaaaaa'
    print('Test #6 is', 'Ok.' if prefix_suffix(string) == 5 else 'Fail.')
    string = 'abacabadabacaba'
    print('Test #7 is', 'Ok.' if prefix_suffix(string) == 7 else 'Fail.')
    string = 'aaabaaaaa$aaaabaaaa'
    print('Test #8 is', 'Ok.' if prefix_suffix(string) == 8 else 'Fail.')

