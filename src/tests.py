from django.test import TestCase

from . import entrance

class Succinctness(TestCase):

    def test_gives_up_session_immediately_normal(self):
        outgoing, gives_up_session = entrance.receive("9876543210", "test", "info!")
        self.assertTrue(gives_up_session)

    def test_gives_up_session_immediately_continuation_somehow(self):
        outgoing, gives_up_session = entrance.receive("9876543210", "test")
        self.assertTrue(gives_up_session)


class Aborts(TestCase):

    def test_abort(self):
        # no exception raised
        entrance.abort("9876543210")

class GoodCapture(TestCase):

    def test_fail_weird(self):
        self.assertFalse(entrance.claims_conversation("kittens"))

    def test_fail_empty(self):
        self.assertFalse(entrance.claims_conversation(""))

    def test_fail_not_overreaching(self):
        self.assertFalse(entrance.claims_conversation("extraprivacy informatics"))

    def test_very_short(self):
        self.assertTrue(entrance.claims_conversation("privacyinfo"))

    def test_short(self):
        self.assertTrue(entrance.claims_conversation("privacy info"))

    def test_long(self):
        self.assertTrue(entrance.claims_conversation("I want privacy information please"))
