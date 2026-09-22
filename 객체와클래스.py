# class Television: # 클래스는 이름은 대문자로
#     def __init__(self, name, ison, channel, volume): # 생성자
#         self.name = name
#         self.isOn = ison
#         self.channel = channel
#         self.volume = volume
#
#     def set_on(self,ison):
#         self.isOn = ison
#     def set_channel(self,cnl):
#         self.channel = cnl
#     def set_volume(self,vol):
#         if 0 <= vol <= 100:
#             self.volume = vol
#         else:
#             print("볼륨값 입력 범위를 초과 했습니다.")
# # --------------------------------------------------------------
#     def get_on(self):
#         return self.isOn
#     def get_channel(self):
#         return self.channel
#     def get_volume(self):
#         return self.volume
#     def view_tv(self):
#         power = ("OFF","ON")
#         print(f"이름: {self.name}")
#         print(f"전원: {self.isOn}")
#         print(f"채널: {self.channel}")
#         print(f"볼륨: {self.volume}")
# -----------------------------------------------------------

# lg_tv = Television("LG", False, 10, 10)
# samsung_tv = Television("SAMSUNG", False, 20, 20)
#
# samsung_tv.view_tv()
# lg_tv.view_tv()

class Conditioning:
    # 전원, 설정 온도, 바람 세기를 매개변수로 받은 생성자 만들기
    def __init__(self, ison, set_temp, wind_strength, brand ): # 생성자
        self.ison = ison
        self.set_temp = set_temp
        self.wind_strength = wind_strength
        # self.information = information
        self.brand = brand

    def set_ison(self,ison): #전원
        self.ison = ison

    def set_set_temp(self,temp): # 설정 온도
        temp = 20
        if 18 <= temp <= 30:
            self.set_temp = temp
        else:
            print("설정 온도의 범주를 넘어섰습니다.")

    def set_wind_strength(self, strength): # 바람 세기
        self.wind_strength = strength

    # def set_information(self, information): # 에어컨 정보 표시
    #     self.information = information
    def set_brand(self, brand):
        self.brand = brand


    def get_ison(self):
        return self.ison
    def get_set_temp(self):
        return self.set_temp
    def get_wind_strength(self):
        return self.wind_strength
    # def get_information(self):
    #     return self.information

    def get_brand(self):
        return self.brand


    def view_info(self): # 에어컨 정보 표시
        wind_str = "", "1단계","2단계","3단계"
        print(f"브랜드: {self.brand}")
        print(f"전원: {self.ison and "ON" or "OFF"}")
        print(f"설정 온도: {self.set_temp}")
        print(f"바람 세기: {wind_str[self.wind_strength]}")
        # print(f"에어컨 정보: {self.information}")


my_air_con = Conditioning(True,20,1,"휘젠")
samsung_air_con = Conditioning(True,22,2,"삼성")

my_air_con.view_info()
print()
samsung_air_con.view_info()

while True:
    samsung_air_con.view_info()