def solution(n, arr1, arr2):
    arr1_bi = []
    arr2_bi = []
    result_arr = []

    for i in range(n):

        for x in range(n) :
            arr1_bi.append(arr1[i] % 2)
            arr1[i] = int(arr1[i] / 2)

            arr2_bi.append(arr2[i] % 2)
            arr2[i] = int(arr2[i] / 2)

        arr1_bi.reverse()
        arr2_bi.reverse()

        result = ""
        for y in range(n) :
            if arr1_bi[y] == 0 and arr2_bi[y] == 0 :
                result += " "
            else:
                result += "#"

        result_arr.append(result)

        arr1_bi = []
        arr2_bi = []

    return result_arr

