import json  # 정부기관 공공데이터를 JSON형태로 수신 받기 위함
import datetime  # 시간 정보를 구하기 위해서 사용
import requests  # HTTP로 서버의 데이터를 수신하기 위해서 사용
# 공공 데이터를 수신하기 위해서 발급받은 Decoding 키를 입력
API_KEY = 'LPh8U0fWWitEfCUYAQMCreTSbSbI4XqYB%2Bspk2jhS90QAcvAT1FforFEAfawd9rL4yV8Ecqs%2B0pv6G9eMYM5yA%3D%3D'

# 날짜 및 시간 설정
now = datetime.datetime.now()  # 운영체제로 현재 시간과 날짜 정보를 가져 옴

# 년월일 정보를 추출하기 위해서 포맷 형식을 지정, base_date : 20240121
date = now.strftime('%Y%m%d')

# 시간 정보를 추출하기 위해서 포맷 형식을 지정, base_time : 0622
if now.minute < 30:   # 현재 분이 30분 이전이면 전 시간으로 설정
    now = now - datetime.timedelta(minutes=30)
    time = now.strftime('%H%M')
else:
    time = now.strftime('%H%M')

# 요청 주소의 URL 지정
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

# 예보 지점 좌표 (서울시 강남구 역삼동)
nx_val = 62
ny_val = 126

# 한 페이지에 포함된 결과 수
num_of_rows = 6
# 페이지 번호
page_no = 1
# 응답 데이터 형식 지정
data_type = 'JSON'

req_parameter = {'serviceKey': API_KEY,
                 'pageNo': page_no,
                 'numOfRows': num_of_rows,
                 'dataType': data_type,
                 'base_date': date,
                 'base_time': time,
                 'nx': nx_val, 'ny': ny_val
                 }
# 요청 및 응답 : 서버로 부터 데이터를 수신 받기 때문에 예외 처리가 필요
response = ""
try:
    response = requests.get(url, params=req_parameter)
except requests.exceptions.RequestException as e:
    print(f"날씨 정보 가져 오기 오류 : {e}")

# JSON 형태로 응답받은 데어터를 딕셔너리로 변환 (역직렬화)
dict_data = response.json()
# print(json.dumps(dict_data, indent=2))

# 딕셔너리 데이터를 분석하여 원하는 데이터를 추출
weather_items = dict_data['response']['body']['items']['item']

for weather_item in weather_items:
    obsrValue = weather_item['obsrValue']
    category = weather_item['category']
    if category == 'T1H':
        print(f"[현재 기온 : {obsrValue}℃]")
    elif category == 'REH':
        print(f"[현재 습도 : {obsrValue}%]")
    elif category == 'RN1':
        print(f"[1시간 강수량 : {obsrValue}mm]")




# import requests  # HTTP로 서버의 데이터를 수신하기 위해서
# import json  # 정부기관 공공데이터를 JSON형태로 수신 받기 위함
# import datetime  # 시간 정보를 구하기 위해서
#
# API_KEY = 'H/OTURbdTORwDoJcWGCcftHkq0Q/pZLNnHKl3LAbcW425OjuS+lQI/TZT8WVRPw4u+xvNWtCXGpMuU80YmUbiw=='
#
# # 요청 주소의 URL 지정
# url = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
#
# # 날짜 및 시간 설정
# now = datetime.datetime.now()
#
# # 매시 45분 이전이면 전 시간 정시 데이터를 요청 (API 생성 시각 반영)
# if now.minute < 45:
#     check_time = now - datetime.timedelta(hours=1)
# else:
#     check_time = now
#
# # YYYYMMDD 포맷
# date = check_time.strftime("%Y%m%d")
#
# # HH00 포맷 (콜론 없이 4자리 숫자)
# base_time_str = check_time.strftime("%H00")
#
# # 예보 지점 기상청 격자 좌표 (천안시 동남구 대흥동 기준)
# nx_val = 63
# ny_val = 110
#
# # 한 페이지에 포함된 결과 수 (초단기실황 전체 항목 8개)
# num_of_rows = 10
# page_no = 1
# data_type = 'JSON'
#
# req_parameter = {
#     'ServiceKey': API_KEY,
#     'pageNo': page_no,
#     'numOfRows': num_of_rows,
#     'dataType': data_type,
#     'base_date': date,
#     'base_time': base_time_str,  # 수정: datetime 객체가 아닌 포맷팅된 문자열 입력
#     'nx': nx_val,  # 수정: 위경도 대신 기상청 격자 X값
#     'ny': ny_val,  # 수정: 위경도 대신 기상청 격자 Y값
# }
#
# try:
#     response = requests.get(url, params=req_parameter)
#     dict_data = response.json()
#
#     # 딕셔너리 데이터를 분석하여 원하는 데이터 추출
#     weather_items = dict_data['response']['body']['items']['item']
#
#     print(f"=== {date} {base_time_str[:2]}:00 기준 날씨 정보 ===")
#     for weather_item in weather_items:
#         obsrValue = weather_item['obsrValue']
#         category = weather_item['category']
#
#         if category == 'T1H':
#             print(f"[현재 기온 : {obsrValue}°C]")
#         elif category == 'REH':
#             print(f"[현재 습도 : {obsrValue}%]")
#         elif category == 'RN1':
#             print(f"[1시간 강수량 : {obsrValue}mm]")
#
# except Exception as e:
#     print(f"날씨 정보 가져오기 오류 : {e}")
#
