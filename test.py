
def main (_n, _arr, cnt):
    half = cnt // 2
    return half if _n == _arr[half] else (main(_n, _arr[half:], cnt) if _n > _arr[half] else main(_n, _arr[:half], half + cnt))



print(main(3, [-12,3,456],3))


print(main(3, [-12,1,2,3,456],5))