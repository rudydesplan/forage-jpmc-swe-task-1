import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_negativePrices(self):
        quotes = [
            {'top_ask': {'price': -121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_zeroPrices(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], 0))

    def test_getDataPoint_largePrices(self):
        quotes = [
            {'top_ask': {'price': 1e10, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1e10, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], 1e10))

    def test_getRatio_normal(self):
        self.assertEqual(getRatio(120.48, 121.68), 120.48 / 121.68)
        self.assertEqual(getRatio(117.87, 121.68), 117.87 / 121.68)

    def test_getRatio_divideByZero(self):
        self.assertIsNone(getRatio(120.48, 0))
        self.assertIsNone(getRatio(117.87, 0))

    def test_getRatio_negativePrices(self):
        self.assertEqual(getRatio(-120.48, 121.68), -120.48 / 121.68)
        self.assertEqual(getRatio(117.87, -121.68), 117.87 / -121.68)

    def test_getRatio_zeroPrices(self):
        self.assertIsNone(getRatio(0, 0))

    def test_getRatio_largePrices(self):
        self.assertEqual(getRatio(1e10, 1e10), 1)

if __name__ == '__main__':
    unittest.main()
