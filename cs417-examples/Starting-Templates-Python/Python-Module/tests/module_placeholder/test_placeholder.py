from hamcrest import *
import unittest

from datetime import datetime

import module_placeholder.placeholder as placeholder


class TestPlaceholder(unittest.TestCase):
    def setUp(self):
        self.names = ["Thomas", "Jay"]

    def test_name_in_greeting(self):
        assert_that(placeholder.demo_function("Thomas"), contains_string("Thomas"))
        assert_that(placeholder.demo_function("GenericName"), contains_string("GenericName"))

    def test_day_in_greeting(self):
        day_name = f"{datetime.now():%A}"

        for name in self.names:
            assert_that(placeholder.demo_function("name"), ends_with(day_name))

