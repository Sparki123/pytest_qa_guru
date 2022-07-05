from selene.support.shared import browser
from selene import be, have


def search(query: str):
    input_element = browser.element('[name="q"]')
    input_element.should(be.blank).type(query).press_enter()


class TestSearchGoogle:
    def test_positive_search(self, google):
        search("selene")

        browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

    def test_negative_search(self, google):
        search("something")

        browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))
