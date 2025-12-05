import allure
import pytest
from base.base_test import BaseTest


@allure.epic("Главная страница")
@allure.feature("Навигация по разделам")
class TestMainPageNavigation(BaseTest):

    @allure.title("Проверка навигации: 'О нас' к блоку 'О компании'")
    @pytest.mark.order(1)
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_about_navigation(self):
        self.main_page.open()
        self.main_page.is_open()

        self.main_page.check_navigation(
            button_locator=self.main_page.Nav.ABOUT_BUTTON,
            expected_section_locator=self.main_page.Sections.BLOCK_ABOUT,
            expected_url_hash="#about"
        )
        self.main_page.make_screenshot("")

    @allure.title("Проверка навигации: 'Вакансии' к блоку 'Кого мы ищем'")
    @pytest.mark.order(2)
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_job_navigation(self):
        self.main_page.open()
        self.main_page.is_open()

        self.main_page.check_navigation(
            button_locator=self.main_page.Nav.JOB_BUTTON,
            expected_section_locator=self.main_page.Sections.BLOCK_JOB,
            expected_url_hash="#specializations"
        )
        self.main_page.make_screenshot("")

    @allure.title("Проверка навигации: 'Отзывы' к блоку 'Отзывы специалистов'")
    @pytest.mark.order(3)
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_reviews_navigation(self):
        self.main_page.open()
        self.main_page.is_open()

        self.main_page.check_navigation(
            button_locator=self.main_page.Nav.REVIEWS_BUTTON,
            expected_section_locator=self.main_page.Sections.BLOCK_REVIEWS,
            expected_url_hash="#testimonials"
        )
        self.main_page.make_screenshot("")

    @allure.title("Проверка навигации: 'Контакты' к блоку 'Свяжитесь с нами'")
    @pytest.mark.order(4)
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_contact_navigation(self):
        self.main_page.open()
        self.main_page.is_open()

        self.main_page.check_navigation(
            button_locator=self.main_page.Nav.CONTACT_BUTTON,
            expected_section_locator=self.main_page.Sections.BLOCK_CONTACT,
            expected_url_hash="#contact"
        )
        self.main_page.make_screenshot("")

    @allure.title("Проверка навигации: 'Аутстафф' к блоку 'Форматы сотрудничества'")
    @pytest.mark.order(5)
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_outstaff_navigation(self):
        self.main_page.open()
        self.main_page.is_open()

        self.main_page.check_navigation(
            button_locator=self.main_page.Nav.OUTSTAFF_BUTTON,
            expected_section_locator=self.main_page.Sections.BLOCK_SERVICES,
            expected_url_hash="#services"
        )
        self.main_page.make_screenshot("")

    @allure.title("Проверка навигации: 'Трудоустройство' к блоку 'Форматы сотрудничества'")
    @pytest.mark.order(6)
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_employment_navigation(self):
        self.main_page.open()
        self.main_page.is_open()

        self.main_page.check_navigation(
            button_locator=self.main_page.Nav.EMPLOYMENT_BUTTON,
            expected_section_locator=self.main_page.Sections.BLOCK_SERVICES,
            expected_url_hash="#services"
        )
        self.main_page.make_screenshot("")

    @allure.title("Проверка навигации: 'Консультация' к блоку 'Свяжитесь с нами'")
    @pytest.mark.order(7)
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_consultation_navigation(self):
        self.main_page.open()
        self.main_page.is_open()

        self.main_page.check_navigation(
            button_locator=self.main_page.Nav.CONSULTATION_BUTTON,
            expected_section_locator=self.main_page.Sections.BLOCK_CONTACT,
            expected_url_hash="#contact"
        )
        self.main_page.make_screenshot("")