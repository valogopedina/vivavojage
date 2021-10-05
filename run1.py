from bot.vivavoyage.vivavoyage import VivaVoyage

with VivaVoyage() as bot:
    bot.land_first_page()
    bot.destination('Caribbean')
    bot.advance_search()