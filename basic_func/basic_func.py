def add(a, b):
	return a + b


def sub(a, b):
	return a  - b


def mul(a, b):
	return a * b


def div(a, b):
	if b == 0:
		print("no divided by zero")
	return a / b


def power(base, pow):
	return base ** pow


def square(base):
	return base ** 2


#def test_greet():
#    assert "안녕하신가 낯선자!" == greet()
#    assert "안녕하십니까 마법사!" == greet(이름="마법사", 나이=50)
#    assert "안녕 낯선자!" == greet(나이=4)

def greet(이름="낯선자", 나이=20):
	if 이름 == "낯선자" and 나이!= 4:
		return f"안녕하신가 {이름}!"
	elif 이름 == "마법사" and 나이== 50:
		return f"안녕하십니까 {이름}!"
	elif 나이== 4:
		return f"안녕 {이름}!"


print(greet())
print(greet(나이=4))
print(greet(이름="마법사", 나이=50))
