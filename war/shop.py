class Item:
    def __init__(self,name, sell_in, quality):
        self.name=name
        self.sell_in=sell_in
        self.quality=quality

items=[]

items+=[Item('+5 Dexterity Vest', 10, 20)]
items+=[Item('Aged Brie', 2, 0)]
items+=[Item('Elixir of the Mongoose', 5, 7)]
items+=[Item('Sulfuras, Hand of Ragnaros', 0, 80)]
items+=[Item('Backstage passes to a TAFKAL80ETC concert', 15, 20)]
items+=[Item('Conjured Mana Cake', 3, 6)]

def update_quality():
    for i in range(len(items)):
        if items[i].name == "Sulfuras":
            pass
        else:
            items[i].sell_in -= 1


"""
def update_quality():
    for i in range(len(items)):
        if items[i].name!='Aged Brie' and items[i].name!='Backstage passes to a TAFKAL80ETC concert':
            if items[i].quality>0:
                if items[i].name!='Sulfuras, Hand of Ragnaros':
                    items[i].quality=items[i].quality - 1
        else:
            if items[i].quality<50:
                items[i].quality=items[i].quality + 1
                if items[i].name=='Backstage passes to a TAFKAL80ETC concert':
                    if items[i].sell_in<11:
                        if items[i].quality<50:
                            items[i].quality=items[i].quality + 1
                    if items[i].sell_in<6:
                        if items[i].quality<50:
                            items[i].quality = items[i].quality + 1
        if items[i].name != 'Sulfuras, Hand of Ragnaros':
            items[i].sell_in = items[i].sell_in - 1
        if items[i].sell_in<0:
            if items[i].name!='Aged Brie':
                if items[i].name!='Backstage passes to a TAFKAL80ETC concert':
                    if items[i].quality>0:
                        if items[i].name !='Sulfuras, Hand of Ragnaros':
                            items[i].quality=items[i].quality - 1
                else:
                    items[i].quality = items[i].quality - items[i].quality
            else:
                if items[i].quality < 50:
                    items[i].quality=items[i].quality + 1
"""
