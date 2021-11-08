num = input('Введите число:')
def rot(num):
    new_num_list = [int(a) for a in str(num)]
    for i in new_num_list:
        if i != 6 and i != 9:
            return ('Число должно состоять из 6 и 9')
            break
    stroka_new_num_list=''.join(str(t) for t in new_num_list)
    ending_num_list = int(stroka_new_num_list.replace('6', '9', 1))
    return ending_num_list
print(rot(num))
