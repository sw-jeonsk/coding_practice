test_data = [9, 8, 1, 3, 2]


def main(_data: list):
    print(_data)
    for _i in range(len(_data)):
        min_index = _data.index(min(_data[_i:]))
        _data[_i:].index(min(_data[_i:]))
        _data[_i], _data[min_index] = _data[min_index], _data[_i]
        print(_data)


main(test_data)
