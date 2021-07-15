test_data = [9, 8, 1, 3, 2]


def main(_data: list):

    for _i in range(len(_data)):
        for _i2, _i3 in zip(range(0, len(_data)), range(1, len(_data))):
            if _data[_i2] > _data[_i3]:
                _data[_i2], _data[_i3] = _data[_i3], _data[_i2]
            print(_data)


main(test_data)
