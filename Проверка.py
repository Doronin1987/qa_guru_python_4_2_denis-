from селен_учеба.support.shared import browser
from селен_учеба import be, have

browser.config.timeout = 10  # Увеличим таймаут, если нужно

browser.open("https://google.com")
browser.element('input[name="q"]').should(be.blank).type("yashaka/selene").press_enter()
browser.should(have.text("Selene - User-oriented Web UI browser tests in Python"))
