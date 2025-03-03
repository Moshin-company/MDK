import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        
        answer = input("Ваш ответ (введите номер варианта): ")
        
        if question["options"][int(answer) - 1] == question["answer"]:
            print("Правильно!")
            self.score += 1
        else:
            print(f"Неправильно! Правильный ответ: {question['answer']}")
        print()

    def start_quiz(self):
        random.shuffle(self.questions)  # Перемешиваем вопросы
        for question in self.questions:
            self.ask_question(question)
        
        print(f"Ваш итоговый счет: {self.score} из {len(self.questions)}")

if __name__ == "__main__":
    questions = [
        {
            "question": "Что такое массив в Python?",
            "options": ["Структура данных", "Переменная", "Функция", "Класс"],
            "answer": "Структура данных"
        },
        {
            "question": "Как создать класс в Python?",
            "options": ["class MyClass:", "MyClass()", "create MyClass:", "new MyClass:"],
            "answer": "class MyClass:"
        },
        {
            "question": "Как создать список в Python?",
            "options": ["[]", "{}", "()", "<>"],
            "answer": "[]"
        },
        {
            "question": "Как вызвать функцию в Python?",
            "options": ["call myFunction()", "myFunction()", "invoke myFunction()", "execute myFunction()"],
            "answer": "myFunction()"
        },
        {
            "question": "Какой метод добавляет элемент в список?",
            "options": ["add()", "append()", "insert()", "push()"],
            "answer": "append()"
        },
        {
            "question": "Как получить длину списка?",
            "options": ["len()", "length()", "size()", "count()"],
            "answer": "len()"
        },
        {
            "question": "Как создать экземпляр класса?",
            "options": ["MyClass()", "new MyClass()", "create MyClass()", "instance MyClass()"],
            "answer": "MyClass()"
        },
        {
            "question": "Какой метод удаляет элемент из списка?",
            "options": ["remove()", "delete()", "pop()", "discard()"],
            "answer": "remove()"
        },
        {
            "question": "Как определить функцию в Python?",
            "options": ["def myFunction():", "function myFunction():", "create myFunction():", "define myFunction():"],
            "answer": "def myFunction():"
        },
        {
            "question": "Как получить доступ к элементу массива?",
            "options": ["array[index]", "array[index+1]", "array.get(index)", "array[index-1]"],
            "answer": "array[index]"
        },
        {
            "question": "Какой метод возвращает последний элемент списка?",
            "options": ["last()", "getLast()", "pop()", "tail()"],
            "answer": "pop()"
        },
        {
            "question": "Как создать пустой список?",
            "options": ["list = []", "list = {}", "list = ()", "list = null"],
            "answer": "list = []"
        },
        {
            "question": "Какой оператор используется для создания массива?",
            "options": ["[]", "{}", "()", "<>"],
            "answer": "[]"
        },
        {
            "question": "Какой метод используется для сортировки списка?",
            "options": ["sort()", "order()", "arrange()", "organize()"],
            "answer": "sort()"
        },
        {
            "question": "Какой метод возвращает индекс элемента в списке?",
            "options": ["index()", "find()", "search()", "locate()"],
            "answer": "index()"
        },
        {
            "question": "Как создать метод в классе?",
            "options": ["def methodName(self):", "method methodName(self):", "create methodName(self):", "function methodName(self):"],
            "answer": "def methodName(self):"
        },
        {
            "question": "Как вызвать метод объекта?",
            "options": ["object.methodName()", "object->methodName()", "call object.methodName()", "invoke object.methodName()"],
            "answer": "object.methodName()"
        },
        {
            "question": "Как добавить элемент в начало списка?",
            "options": ["insert(0, element)", "add(0, element)", "prepend(element)", "push_front(element)"],
            "answer": "insert(0, element)"
        },
        {
            "question": "Как удалить все элементы из списка?",
            "options": ["clear()", "removeAll()", "delete()", "empty()"],
            "answer": "clear()"
        },
        {
            "question": "Как проверить, есть ли элемент в списке?",
            "options": ["in", "exists()", "contains()", "has()"],
            "answer": "in"
        },
        {
            "question": "Как объединить два списка?",
            "options": ["list1 + list2", "list1.append(list2)", "merge(list1, list2)", "combine(list1, list2)"],
            "answer": "list1 + list2"
        }
    ]

    game = QuizGame(questions)
    game.start_quiz()
