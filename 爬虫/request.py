import requests
response=requests.get("https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-08-01&leftTicketDTO.from_station=XAY&leftTicketDTO.to_station=HHC&purpose_codes=ADULT")
print(response.text)