solve  = ["Тестовые фреймворки в Python" ,
"Поиск элементов на HTML-странице",
"Использование паттерна PageObject для упрощения поддержки автотестов",
"Методы работы с всплывающими окнами браузера в Selenium WebDriver",
"Запуск браузера с помощью Selenium WebDriver",
"Параллельный запуск тестов",
"Настройка окружения Selenium WebDriver",
"Методы для поиска элементов в Selenium WebDriver" ]


list_try = [[1,2,4,7],[4,7,3,0], [4,6,1,3], [7,4,3,6],
    [3,1,7,6], [4,3,6,1],[7,4,6,3],[6,4,3,1],[3,6,1,7]
]

for ind, task in zip(range(len(solve)),solve):
    print(ind,end=" ")
    for tr in list_try:
        if ind in tr:
            print("+",end=" ")
        else:
            print("-",end=" ")
    print(task)

