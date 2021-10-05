from bot.booking.booking import Booking
from datetime import date
from datetime import timedelta

start_date = date.today()+timedelta(days=3)
start_date_format = start_date.strftime("%Y-%m-%d")
end_date = start_date+timedelta(days=4)
end_date_format = end_date.strftime("%Y-%m-%d")


with Booking() as bot:
    bot.land_first_page()
    bot.accept_cookies()
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date=start_date_format,
                     check_out_date=end_date_format)
    bot.select_adults(10)
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh() #to let our bot to grab the data properly
    bot.report_results()



