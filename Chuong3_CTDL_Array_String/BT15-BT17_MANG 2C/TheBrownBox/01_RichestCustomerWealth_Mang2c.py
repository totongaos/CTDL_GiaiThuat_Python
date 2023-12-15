'''
You are given an m*n integer grid accounts where accounts[i][j]
    i - is the accounts of money the i_th customer has in the j_th bank.
Return the wealth that the richest customer has

A customer's wealth is the account of money they have in all their bank accounts.
The richest customer is the has the maximum wealth
Ex:
input: accounts = [[1,5],[7,3],[3,5]]
output: 10
'''

# # WAY 1: xai ham sum() & max()
# def richest(acc):
#     n = len(acc)
#     max_i = 0
#     for i in range(0,n):
#         sum_i = sum(acc[i])
#         if max_i < sum_i:
#             max_i=sum_i
#     return max_i
#
# if __name__ == '__main__':
#     acc = [[1,5],[7,3],[3,5]]
#     print(richest(acc))
#     print('DONE')

# # ----------------------------------
# # WAY 2: duyet cac ptu trong mang 2c
# def richest(acc):
#     m = len(acc)
#     n = len(acc[0])
#     max_i = 0
#     for i in range(0,m):
#         sum_i = 0
#         for j in range(0,n):
#             sum_i += acc[i][j]
#         if max_i < sum_i:
#             max_i=sum_i
#     return max_i
#
# if __name__ == '__main__':
#     acc = [[1,5],[7,3],[3,5]]
#     print(richest(acc))
#     print('DONE')

