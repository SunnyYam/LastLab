def max_sum(nums):
    nums.sort() #сортируем список чисел четной длины, с идеей складывать наименьшее число в списке с наибольшим, так
                #сумма этих чисел будет являться наименьшей возможной
    pair_list = []
    n = len(nums)
    for i in range(0, n//2):
        pair_list.append(nums[i]+nums[n-1-i]) #в список заносим суммы чисел
    return max(pair_list) #возвращаем значение наибольшей парной суммы из списка значений всех полученных сумм
