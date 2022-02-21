"""file defines various types of orders"""

from abc import ABC, abstractmethod


class Order(ABC):
    """Defines an abstract type for an order

    An order is any transaction that is carried out by the matching engine.
    There are different types of orders and each has a different behavior of getting executed.
    However, all the orders are expected to get executed depending on the attributes defined below.

    Attributes:
        uid: A unique identifier string for the order
        type: A string indicating type of the order, possible values:
            -LO: Limit Order
        side: A string indicating the side of the order, possible values:
            -B: Buy Order
            -S: Sell Order
        quantity: An int indicating no of units requested for trade
        price: A float indicating the price of each unit
    """

    # pylint: disable=C0103
    def __init__(self, action, uid, type, side, quantity, price):
        """Inits Order class and its attributes"""
        self.action = action
        self.uid = uid
        self.type = type
        self.side = side
        self.quantity = quantity
        self.price = price

        super().__init__()

    def __lt__(self, other):
        """defines less than operator for order comparision"""
        return self.price < other.price

    @abstractmethod
    def __str__(self):
        """Abstract method enables string rep of the order"""

    @abstractmethod
    def _execute_sell_order(self, order_book):
        """Private abstract method enables sell order execution"""
        return

    @abstractmethod
    def _execute_buy_order(self, order_book):
        """Private abstract method enables buy order execution"""
        return

    @abstractmethod
    def execute(self, order_book):
        """Abstract method enables order execution"""
        return
