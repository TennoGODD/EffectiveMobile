import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    request.cls.driver = driver
    driver.execute_script("""
            // Отключаем CSS transitions и animations
            const style = document.createElement('style');
            style.textContent = `
                *, *::before, *::after {
                    transition: none !important;
                    animation: none !important;
                    scroll-behavior: auto !important;
                }
            `;
            document.head.appendChild(style);

            // Отключаем smooth scroll
            document.documentElement.style.scrollBehavior = 'auto';
        """)
    yield driver
    driver.quit()