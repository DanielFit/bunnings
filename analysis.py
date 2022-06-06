import collections
import beat_it_by_10
import current_stock
import competitors
from collections import defaultdict


"""Here we can find out if Bunning's compares two financial years, in financial year 1 they do not
 offer any discount and in financial year 2 they apply the discount of 'beating competitors prices by 10%'
 """


"""this looks at each item in a category individually to see how much each item loses 
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

"""This function measures the profits and loses per item in a category over two financial years """
def profit_loss_by_year_by_category_items(fy1:dict, fy2:dict):
    fy1_copy = collections.Counter(fy1)
    fy2_copy = collections.Counter(fy2)

    profits = dict(fy2_copy- fy1_copy)
    losses = dict(fy1_copy- fy2_copy)
    total = round(sum(profits.values()) - sum(losses.values()),2)
    return "profits $", str(profits),"losses $",str(losses), "$", total

"""This function measures the profits and loses per item in a category over two financial years """
def profit_loss_by_year_category_total(fy1:dict, fy2:dict):
    fy1_copy = collections.Counter(fy1)
    fy2_copy = collections.Counter(fy2)

    profits = dict(fy2_copy- fy1_copy)
    losses = dict(fy1_copy- fy2_copy)
    total = round(sum(profits.values()) - sum(losses.values()),2)
    return total





