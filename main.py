import holidays
import pytz
import datetime

if __name__ == '__main__':
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    brt_now = utc_now.astimezone(pytz.timezone("America/Sao_Paulo"))
    print(brt_now)

    # testing
    datetime_str = '04/22/22 13:55:26'
    brt_now = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

    week_day = brt_now.weekday()
    day_of_month = brt_now.day
    month = brt_now.month    
    year = brt_now.year
    print(f'week_day = {week_day} | day_of_month = {day_of_month} | month = {month} | year = {year}')

    # TODO check if it has all regional holidays
    hs = holidays.Brazil(years=year, subdiv='SP')
    for h in hs.items():
        print('#######################')
        print(brt_now.date())
        print(h[0])
        print(h[1])
        
        if brt_now.date() == h[0]:
            print('it is holiday')

        day_before_holiday = h[0] - datetime.timedelta(days=1)
        if brt_now.date() == day_before_holiday:
            print('Day before')

        day_after_holiday = h[0] + datetime.timedelta(days=1)
        if brt_now.date() == day_after_holiday:
            print('Day after')


        # print(brt_now.date())
        # print(h[0])
        # print(h[1])