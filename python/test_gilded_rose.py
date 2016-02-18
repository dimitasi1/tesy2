# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 2, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_Brie(self):
    	items = [Item("Aged Brie", 3, 5)]
    	gilded_rose = GildedRose(items)
    	gilded_rose.update_quality()
    	self.assertEqual("Aged Brie", gilded_rose.items[0].name)
    	self.assertEqual(6, gilded_rose.items[0].quality)

if __name__ == '__main__':
    unittest.main()
