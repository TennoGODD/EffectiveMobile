import allure
import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    PAGE_URL = Links.HOST

    class Nav:
        ABOUT_BUTTON = ("xpath", "//a[@href='#about' and text()='О нас']")
        JOB_BUTTON = ("xpath", "//a[@href='#specializations' and text()='Вакансии']")
        REVIEWS_BUTTON = ("xpath", "//a[@href='#testimonials' and text()='Отзывы']")
        CONTACT_BUTTON = ("xpath", "//a[@href='#contact' and text()='Контакты']")
        OUTSTAFF_BUTTON = ("xpath", "//a[@href='#services' and text()='Аутстафф']")
        EMPLOYMENT_BUTTON = ("xpath", "//a[@href='#services' and text()='Трудоустройство']")
        CONSULTATION_BUTTON = ("xpath", "//a[@href='#contact' and text()='Консультация']")

    class Sections:
        BLOCK_ABOUT = ("xpath", "//h2[text()='О компании']/ancestor::section")
        BLOCK_JOB = ("xpath", "//h2[text()='Кого мы ищем']/ancestor::section")
        BLOCK_REVIEWS = ("xpath", "//h2[text()='Отзывы специалистов']/ancestor::section")
        BLOCK_CONTACT = ("id", "contact")
        BLOCK_SERVICES = ("id", "services")

    def scroll_to_bottom_smoothly(self):
        scroll_height = self.driver.execute_script("return document.body.scrollHeight")
        current_position = 0
        scroll_step = 1000

        while current_position < scroll_height:
            current_position += scroll_step
            self.driver.execute_script(f"window.scrollTo(0, {current_position});")
            time.sleep(0.1)

        time.sleep(1)

    def check_navigation(self, button_locator, expected_section_locator, expected_url_hash):
        self.scroll_to_bottom_smoothly()

        button = self.wait.until(EC.presence_of_element_located(button_locator))
        button_text = button.text

        with allure.step(f"Проверить навигацию к разделу '{button_text}'"):
            # Запоминаем позицию скролла перед кликом
            scroll_before = self.driver.execute_script("return window.pageYOffset")

            button.click()
            time.sleep(1)

            # Получаем данные после клика
            current_url = self.driver.current_url
            scroll_after = self.driver.execute_script("return window.pageYOffset")

            # Проверяем произошел ли скролл (допускаем небольшую погрешность в 5px)
            scrolled = scroll_after > scroll_before + 5

            # Выводим три пункта в Allure
            allure.attach(
                f"Ожидаемый URL: {Links.HOST}{expected_url_hash}\n"
                f"Фактический URL: {current_url}\n"
                f"Скролл произошел: {'Да' if scrolled else 'Нет'}",
                name="Информация о навигации",
                attachment_type=allure.attachment_type.TEXT
            )

            if expected_url_hash and expected_url_hash not in current_url:
                print(f"Note: URL не содержит {expected_url_hash}, текущий URL: {current_url}")

            target_section = self.wait.until(
                EC.presence_of_element_located(expected_section_locator)
            )

            self.wait.until(EC.visibility_of(target_section))

            is_element_in_viewport = self.driver.execute_script("""
                var elem = arguments[0];
                var rect = elem.getBoundingClientRect();
                var windowHeight = window.innerHeight || document.documentElement.clientHeight;
                var windowWidth = window.innerWidth || document.documentElement.clientWidth;

                // Проверяем, что элемент пересекается с областью просмотра
                // (хотя бы частично виден)
                var isVisible = (
                    rect.top <= windowHeight && 
                    rect.bottom >= 0 &&
                    rect.left <= windowWidth && 
                    rect.right >= 0
                );

                return isVisible;
            """, target_section)

            assert is_element_in_viewport, "Элемент не находится в видимой области экрана"

            section_text = target_section.text
            expected_keywords = {
                "#about": "О компании",
                "#services": ["Форматы сотрудничества", "Помощь в трудоустройстве"],
                "#specializations": "Кого мы ищем",
                "#testimonials": "Отзывы специалистов",
                "#contact": "Свяжитесь с нами"
            }

            if expected_url_hash in expected_keywords:
                keywords = expected_keywords[expected_url_hash]
                if isinstance(keywords, list):
                    found = any(keyword in section_text for keyword in keywords)
                    assert found, f"В блоке не найден ожидаемый текст. Ожидалось: {keywords}"
                else:
                    assert keywords in section_text, f"В блоке не найден текст '{keywords}'"

            return target_section