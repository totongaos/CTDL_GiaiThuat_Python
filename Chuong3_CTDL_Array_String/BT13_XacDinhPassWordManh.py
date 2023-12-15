'''Một mật khẩu mạnh là một chuỗi kí tự đảm bảo có đầy đủ 5 yếu tố sau:

Độ dài của mật khẩu phải nhiều hơn 6 ký tự
Trong mật khẩu phải có ít nhất 1 ký tự số (1234567890)
Trong mật khẩu phải có ít nhất 1 ký tự thường (abc...z)
Trong mật khẩu phải có ít nhất 1 ký tự in hoa (ABC...Z)
Trong mật khẩu phải có ít nhất 1 ký tự đặc biệt (!@#$%^&*()-+)'''

#--------------------------------------------------------------
#WAY 1:
#1. input passWord
# passWord = str(input())
passWord = 'Ab3#44'

count_titlte = count_lower = count_num = count_Special_characters = False
#2. check password
if len(passWord) >=6:
    for i in passWord:
        if i.isupper():
            count_titlte = True
        elif i.isnumeric():
            count_num = True
        elif i.islower():
            count_lower = True
        elif i in '!@#$%^&*()-+':
            count_Special_characters = True

    if count_Special_characters and count_num and count_lower and count_titlte :
        print('TRUE')
    else:
        print('FALSE')
else:
    print('FALSE')