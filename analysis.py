import collections
import beat_it_by_10
import current_stock
import competitors
from collections import defaultdict


"""Here we can find out if a lower price on a stocked item is beaten by 10%, how much
profit will be lost. We can then use these to figures to determine how many sales need
to be made to make up for the loss. This tool is intended to be use to make decisions 
about the future"""


"""this looks only at each item individually to see how much each item loses 
value if the discount is applied due to a competitor having a lower priced
item"""
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

"""This functionmeasures over a two years the profits and loses per item in a category
and then reutrns for the category the overall profit or loss for the year"""
def profit_loss_by_year_by_category_items(fy1:dict, fy2:dict):
    fy1_copy = collections.Counter(fy1)
    fy2_copy = collections.Counter(fy2)

    profits = dict(fy2_copy- fy1_copy)
    losses = dict(fy1_copy- fy2_copy)
    total = round(sum(profits.values()) - sum(losses.values()),2)
    return "profits $", str(profits),"losses $",str(losses)

def profit_loss_by_year_category_total(fy1:dict, fy2:dict):
    fy1_copy = collections.Counter(fy1)
    fy2_copy = collections.Counter(fy2)

    profits = dict(fy2_copy- fy1_copy)
    losses = dict(fy1_copy- fy2_copy)
    total = round(sum(profits.values()) - sum(losses.values()),2)
    return total





