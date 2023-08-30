# first-flask
**Проект для знакомства с фреймворком Flask**

Проект обрабатывает json файл и выводит некоторую информацию в браузер.

Пример json файла: 
```
[
  {
    "id": 1,
    "name": "Vagner Vladimir",
    "picture": "https://picsum.photos/200/300",
    "gender": "male",
    "age": 33
  },
  {
    "id": 2,
    "name": "Kalashnikova Maria",
    "picture": "https://picsum.photos/200/300",
    "gender": "female",
    "age": 22
  },
  {
    "id": 3,
    "name": "Grad Nikita",
    "picture": "https://picsum.photos/200/300",
    "gender": "male",
    "age": 22
  }
]
```

Проект обрабатывает GET запросы на следующие страницы: 

/  - отображает список всех пользователей.

Формат выходных данных: name, gender, age.


/users/id - отображет информация по конкретному id пользователя

Формат выходных данных: picture, name, gender, age.


/genders/gender - отображает информацию по пользователям на основании переданного параметра gender.

Формат выходных данных: name, gender, age.
