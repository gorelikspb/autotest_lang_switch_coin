**Задание**
Разработать автоматизированные тесты для переключения языков coinmarketcap.com.
Критерии успешности проверки, сценарии проверки, инструменты для разработки и запуска тестов на ваш выбор.
Результат должен быть снабжен инструкцией по запуску теста.

**Сценарий проверки переключения языков.**
1. Открыть сайт.
2. Открыть выпадающий список переключения языков.
3. Переключить по порядку все языки из списка (каждый раз открывая список)
Критерий успешности: 
1. Все действия были произведены без прерываний.
2. Аббревиатура языка, отображаюемого после переключения должна соответствовать элементу ссылки, ведущей на страницу с этим языком. Например, для немецкого - аббревиатура языка DE и ссылка https://coinmarketcap.com/de/ (клик по ней и приводит на эту страницу). Так для каждого языка из списка (на данный момент их 12). Исключение - страница для английского языка (EN) - на неё ведет базовая ссылка https://coinmarketcap.com/, без (/en/).

**Инструкция по запуску:**
Для запуска теста, помимо установленного Python и соответствующих библиотек, понадобится Selenium
(особенности установки: https://habr.com/ru/post/248559/, пункт 1.4 не требуется. 

Под Windows для запуска тестового Firefox понадобится в т.ч. geckodriver (https://github.com/mozilla/geckodriver/releases), путь к файлу необходимо прописать в PATH



