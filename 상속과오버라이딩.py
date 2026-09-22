# 상속: 부모클래스에서 만든 변수와 메서드를 물려 받아 사용할 수 있음
# 오버라이딩: 부모 클래스의 메서드를 상속 받아 재정의 하는 것
class ProtoTV:
    pass
    # 전원, 채널, 볼륨을 매개변수로 하는 생성자 생성
    def __init__(self, power, channel, volume ): # 생성자
        self.power = power
        self.channel = channel
        self.volume = volume
    # 전원을 켜고 끄는 메서드
    def set_power(self,power):
        self.power = power

    # 채널 설정 메서드 (1~1000)
    def set_channel(self,channel):
        if 0 <= channel <= 1000:
            self.channel = channel
            print(f"채널을 {channel} 변경")
        else:
            print("채널 설정 범위에 벗어났습니다.")
    # 볼륨 설정 메서드 (0~100)
    def set_volume(self,volume):
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"볼륨을 {volume}로 변경 하였습니다.")
        else:
            print("소리 설정의 범주를 넘어섬")

class ProductTV(ProtoTV):
    def set_channel(self,channel):
        if 0 <= channel <= 1000:
            self.channel = channel
            print(f"채널은 {channel}로 변경 하였습니다")
        else:
            print("다시 설정해주세요")

    # 정보를 출력하는 메서드
    def information(self):
        print(f"전원: {'ON' if self.power else 'OFF'}")
        print(f"채널: {self.channel}")
        print(f"볼륨: {self.volume}")

ProductTV = ProductTV(False,10,10)
ProductTV.set_power(True)
ProductTV.set_channel(45)
ProductTV.set_volume(50)
ProductTV.information()


