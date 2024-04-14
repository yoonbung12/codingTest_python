# 튜플(잠겨 있는 리스트-변경 만 불가능) - immutable(sort, remove, insert, pop 이 불가능**)
t1 = (1,) # 하나의 요소를 넣을때는 반드시 ,를 넣어야함
t2 = (1, 2,3)
t3 = (1, 2, 3, ("a", "b"))
print(t3[1:])
print(t3)

t4 = t3 + t2  # 새로운 튜플을 만들어냄
print(t4)

# 딕셔너리 { 'key' : 'value'} - immutable
dic = {'name' : "bonggu", 'phone' : '010-000-000', 'birth' : '199999999' }
print(dic)
print(dic['birth']) # 번호면 번호로 아니면 문자열이면 문자열로.!!
del dic['birth'] # key 이름을 넣어줄것.
print(dic.keys())
print(dic.values()) #값들만 가져올때, items도 있다 기억할것.
dic.clear() # 값을 싹다 날림
print(dic.get('h1', '값이 없습니다.')) # hi가 있으면 출력하고 없으면 값이 없습니다를 출력

# 집합(set)
s1 = set([1,2,3,4,5,6])
print(s1)
s2 = set([4,5,6,7,8,9]) 
print(s2)
print(s1 & s2) # 교집합
print(s1.intersection(s2)) # 교집합
print(s1 | s2) # 합집합(union도 있다.)
s3 = str([4,5,6,7,8,9]) # 문자열로 바꿈




