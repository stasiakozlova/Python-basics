def main():
    string = input()

    string_length = len(string)

    for i in range(0, string_length):
        for j in range(0, string_length):
            if string[i] < string[j]:
                temp = string[i]
                string = string[:i] + string[j] + string[i + 1:]
                string = string[:j] + temp + string[j + 1:]

    print(string)

if __name__ == '__main__':
    main()
