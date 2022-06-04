import beat_it_by_10
import competitors
import current_stock
import  analysis

""""ou can use the functions to check prices of current stocked item.
try by_competition or by_product"""


print(beat_it_by_10.by_competition(current_stock.outdoor_furniture,competitors.comp_outdoor_furniture))
#print(beat_it_by_10.by_product("oak",70,current_stock.timber))
print(analysis.loss_on_discount(current_stock.outdoor_furniture,competitors.comp_outdoor_furniture))

