# Легковесный Dockerfile только для запуска тестов
FROM python:3.10-alpine3.18

# Устанавливаем только Chrome и зависимости
RUN apk update && \
    apk add --no-cache \
    chromium \
    chromium-chromedriver \
    bash \
    && rm -rf /var/cache/apk/*

# Переменные окружения
ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY . .

# Только запуск тестов
CMD ["pytest", "-v", "--alluredir=allure-results"]