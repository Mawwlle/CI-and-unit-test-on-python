import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = Chrome('chromedriver',chrome_options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize(
    "url, phrase, search_id_first, search_id_second, search_res_count",
    [
# Please comment on one of the tests, as CI does not yet support all tests
        # DuckDuckGo
        ('https://duckduckgo.com/', 'hello', 'search_form_input_homepage', 'search_form_input',
         'results'),
        # Yandex
        # ('https://yandex.ru/', 'abobuis', 'text', 'uniq16295382021401', 'content__left'),
        # # Test my own webpage
        # ('http://127.0.0.1:5000/search', 'test_browser', 'text', 'uniq16295382021401', 'content__left')
    ]
)
def test_basic_search(url, phrase, search_id_first, search_id_second, search_res_count, browser):
    # This func realizing Arrange-Act-Assert pattern
    # Arrange
    browser.get(url)

    # Act
    search_input = browser.find_element_by_id(search_id_first)
    search_input.send_keys(phrase + Keys.RETURN)

    # Assert
    link_divs = browser.find_element_by_class_name(search_res_count)
    assert link_divs

    search_input = browser.find_element_by_id(search_id_second)
    assert search_input.get_attribute('value') == phrase
