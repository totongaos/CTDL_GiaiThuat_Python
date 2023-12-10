if __name__ == '__main__':
    str = "hello word" #NOTE: String ko the thay doi dc cac p.tu ben trong no
    res = ''

    for i in range(len(str)):
        if i%2 == 0:
            res += '_'
        else:
            res += str[i]

    print('result: '+res)