import unittest
from hamcrest import equal_to, assert_that
from checkout import Checkout


inventory = {
    "apple": {
        "price": 0.5,
        "special_price": {
            "quantity": 3,
            "price": 1.30
        }
    },
    "banana": {
        "price": 0.3,
        "special_price": {
            "quantity": 2,
            "price": 0.45
        }
    },
    "cucumber": {
        "price": 0.2,
    },
    "doughnut": {
        "price": 0.15,
    }
}

class TestCheckout(unittest.TestCase):

    def test_item_on_order(self):

        # add item to order
        # go through order and get price for each item
        # add price to total
        # return total

        #  add an apple to the list
        # confirm there is an apple on the list

        checkout = Checkout(inventory)

        checkout.scan("apple")

        #assert
        assert_that(checkout._Checkout__order[0], equal_to("apple"))

    def test_get_total_for_one_apple(self):

        checkout = Checkout(inventory)

        checkout.scan("apple")

        assert_that(checkout.get_total(), equal_to(0.5))

    def test_get_total_for_one_banana(self):

        checkout = Checkout(inventory)

        checkout.scan("banana")

        assert_that(checkout.get_total(), equal_to(0.3))

    def test_total_for_two_apples(self):
        checkout = Checkout(inventory)

        checkout.scan("apple")
        checkout.scan("apple")

        assert_that(checkout.get_total(), equal_to(1))

    def test_get_special_price_for_three_apples(self):
        checkout = Checkout(inventory)

        checkout.scan("apple")
        checkout.scan("apple")
        checkout.scan("apple")

        assert_that(checkout.get_total(), equal_to(1.30))

    def test_get_price_for_four_apples(self):
        checkout = Checkout(inventory)

        checkout.scan("apple")
        checkout.scan("apple")
        checkout.scan("apple")
        checkout.scan("apple")

        assert_that(checkout.get_total(), equal_to(1.80))

    def test_problem_four(self):
        checkout = Checkout(inventory)

        checkout.scan("apple")
        checkout.scan("banana")
        checkout.scan("apple")
        checkout.scan("banana")
        checkout.scan("cucumber")
        checkout.scan("doughnut")

        assert_that(checkout.get_total(), equal_to(1.80))

    def test_problem_five(self):
        checkout = Checkout(inventory)

        checkout.scan("apple")
        checkout.scan("doughnut")
        checkout.scan("cucumber")
        checkout.scan("banana")
        checkout.scan("apple")
        checkout.scan("banana")
        checkout.scan("apple")

        assert_that(checkout.get_total(), equal_to(2.10))
