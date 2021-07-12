
from .solution import solution 

def test_case1():
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]

    assert solution(participant, completion) == "leo"

def test_case2():
    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]	
    completion = ["josipa", "filipa", "marina", "nikola"]	

    assert solution(participant, completion) == "vinko"    

def test_case3():
    participant = ["mislav", "stanko", "mislav", "ana"]	
    completion =["stanko", "ana", "mislav"]	

    assert solution(participant, completion) == "mislav"        