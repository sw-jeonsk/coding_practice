import pdb
def my_solution1(phone_book):
    phone_book.sort()
    for index, phone in enumerate(phone_book):
        for index2, phone2 in enumerate(phone_book):
            if index == index2:
                continue
            if phone == phone2[:len(phone)]:
                return False
    return True


def my_solution2(phone_book):

    for index, phone in enumerate(phone_book):
        temp = [phone2[:len(phone)] for index1, phone2 in enumerate(phone_book) if index != index1]
        if phone in temp:
            return False
    return True


def my_solution3(phone_book):
    phone_book = sorted(phone_book)
    for phone, phone2 in zip(phone_book, phone_book[1:]):
        if phone == phone2[:len(phone)]:
            return False
    return True


def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    print(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True