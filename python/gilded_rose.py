# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedItem(Item):
    # default change in quality per day
    delta_quality = -1
    max_quality = 50

    def change_qual(self):
        # lower quality
        if (self.quality > (0 - self.delta_quality)):
            self.quality += self.delta_quality
        else:
            self.quality = 0

    def update_sell_in(self):
        self.sell_in -= 1

    def update_qual(self):
        self.update_sell_in()
        self.change_qual()
        if self.sell_in < 0:
            self.change_qual()


class BetterWithAge(GildedItem):
    delta_quality = 1

    def change_qual(self):
        # increase quality
        if (self.quality < self.max_quality - self.delta_quality):
            self.quality += self.delta_quality
        else:
            self.quality = self.max_quality


class AgedBrie(BetterWithAge):
    pass


class Sulfuras(GildedItem):

    def update_qual(self):
        pass


class BackstagePasses(BetterWithAge):

    def update_qual(self):
        if self.sell_in <= 5:
            self.delta_quality = 3
        elif self.sell_in <= 10:
            self.delta_quality = 2
        self.change_qual()
        self.update_sell_in()
        if self.sell_in < 0:
            self.quality = 0


class ConjuredItem(GildedItem):
    delta_quality = -2


class GildedRose(object):

    def __init__(self, items):
        item_filter = {
            "Aged Brie": AgedBrie,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePasses,
            "Sulfuras, Hand of Ragnaros": Sulfuras,
            "Conjured Mana Cake": ConjuredItem,
        }
        self.items = []
        for item in items:
            itemdata = [item.name, item.sell_in, item.quality]
            # create the appropriate object for this type of item
            constructor = item_filter.get(item.name, GildedItem)
            self.items.append(constructor(*itemdata))

    def update_quality(self):
        for item in self.items:
            item.update_qual()
