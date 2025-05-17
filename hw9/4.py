from datetime import datetime

start_str = input("시작 날짜(연/월/일) --> ")

start_date = datetime.strptime(start_str, "%Y/%m/%d")
today = datetime.today()

delta_days = (today - start_date).days

weekday_kor = ["월", "화", "수", "목", "금", "토", "일"]
today_weekday = weekday_kor[today.weekday()]

print(f"{start_date.strftime('%Y/%m/%d')} 부터 오늘( {today.year}/{today.month}/{today.day} )까지는  {delta_days:>4} 일이 지났습니다.")
print(f"그리고 오늘은  {today_weekday} 요일 입니다.")
