import pytest

from pages.main_page import MainPage


class BaseTest:

    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup(self,request,driver):
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
