# first-flask
Проект для знакомства с фреймворком Flask

Проект обрабатывает json файл и выводит некоторую информацию в браузер.

Пример json файла:      
[
  {
    "id": 1,
    "name": "Butkov Vladimir",
    "picture": "https://picsum.photos/200/300",
    "gender": "male",
    "age": 33
  },
  {
    "id": 2,
    "name": "Tsymbalyuk Maria",
    "picture": "https://picsum.photos/200/300",
    "gender": "female",
    "age": 22
  },
  {
    "id": 3,
    "name": "Puzakov Nikita",
    "picture": "https://picsum.photos/200/300",
    "gender": "male",
    "age": 22
  }
]

Проект обрабатывает GET запросы на следующие страницы: 
/  - отображает список всех пользователей.
Формат: name, gender, age.

/users/id - отображет информация по конкретному id пользователя
