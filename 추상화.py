# 추상화(Abstraction)란 복잡한 내부 구현이나 세부 동작 원리는 숨기고,
# 사용자가 꼭 알아야 할 핵심 기능(인터페이스)만 단순화하여 외부로 드러내는 객체지향 설계 원칙입니다.
# 자동차의 엔진 작동 방식(복잡한 내부 구현)을 몰라도
# 운전자는 '핸들, 엑셀, 브레이크'(추상화된 인터페이스)만 가지고 차를 조작할 수 있는 것과 같습니다.

from abc import *

class NetworkAdapter(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass

class LAN(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} LAN에 연결 했습니다,")

class WiFi(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} Wi-Fi에 연결 했습니다.")

class LTE(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} LTE에 연결 했습니다.")

net = input("연결할 네트워크를 선택 [1]LAN, [2]Wi-Fi, [3]LTE : ")
if net == "1":
    adapter = LAN("KT Megapass")
    adapter.connect()
elif net == "2":
    adapter = WiFi("SK Telecom")
    adapter.connect()
elif net == "3":
    adapter = LTE("LG U+")
    adapter.connect()
else: print("연결할 네트워크가 없습니다.")

print()
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # Unit을 상속 받아 공격유닛을 만듬
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스에 생성자 호출
        self.damage = damage

    def attack(self, location):
        print(f"{self.name}: {location}방향으로 적군을 공격합니다.")
    def damaged(self, damage):
        print(f"{self.name}: {damage}입었습니다.")
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp} 입니다,")
        if self.hp <= 0:
            print(f"{self.name} : 파괴 되엇습니다.")

firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(50)






