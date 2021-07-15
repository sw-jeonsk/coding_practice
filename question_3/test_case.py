
from .solution import solution 

def test_case1():
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]


    assert solution(orders, course) == ["AC", "ACDE", "BCFG", "CDE"]


def test_case2():
    orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	
    course = [2,3,5]	


    assert solution(orders, course) == ["ACD", "AD", "ADE", "CD", "XYZ"]
