
from .solution import solution 

def test_case1():
    phone_book = ["119", "97674223", "1195524421"]	

    assert solution(phone_book) == False

def test_case2():
    phone_book = ["123","456","789"]	

    assert solution(phone_book) == True  

def test_case3():
    phone_book = ["12","123","1235","567","88"]		

    assert solution(phone_book) == False        