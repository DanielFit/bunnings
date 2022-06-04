import collections
import beat_it_by_10
import current_stock
import competitors
from collections import defaultdict
import sales_report

"""Here we can find out if a lower price on a stocked item is beaten by 10%, how much
profit will be lost. We can then use these to figures to determine how many sales need
to be made to make up for the loss. This tool is intended to be use to make decisions 
about the future"""



def loss_on_discount_per_item(cs:dict, comp:dict):
    discount = cs.copy()
    for key in discount:
        if key in comp:
            if discount[key] > comp[key]:
                discount[key] = round(comp[key] * .9, 2)

    copy_discount = collections.Counter(discount)
    copy_cs = collections.Counter(cs)
    profit_loss = dict(copy_cs - copy_discount)

    loss_per_product = dict()
    for key in profit_loss:
        loss_per_product[key] = round(profit_loss[key], 2)

    total_loss = sum(loss_per_product.values())

    return loss_per_product ,'$', total_loss


#print(loss_on_discount(current_stock.power_tools,competitors.comp_power_tools))