from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_add_new_book_add_book_twice(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # создаем экземпляр (объект) класса BooksCollector одну и ту же книгу дважды
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        # проверяем, что добавилась одна книга
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_rating_9(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Оно')
        #устанавливаем рейтинг 9
        collector.set_book_rating('Оно', 9)
        #проверяем что установлен рейтинг 9
        assert collector.get_book_rating('Оно')==9

    def test_set_book_rating_set_rating_book_not_in_list(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Оно')
        #устанавливаем рейтинг книге, которой нет в списке
        collector.set_book_rating('Роковые яйца', 10)
        #проверяем, что книге, которой нет в списке нельзя установить рейтинг
        assert collector.get_book_rating('Роковые яйца') !=10

    def test_add_book_in_favorites_add_one_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Проклятые короли')
        #устанавливаем рейтинг 10
        collector.set_book_rating('Проклятые короли', 10)
        #добавляем книгу в избранное
        collector.add_book_in_favorites('Проклятые короли')
        #проверяем, что книга добавилась в избранные
        assert collector.get_list_of_favorites_books() == ['Проклятые короли']

    def test_get_books_with_specific_rating_get_books_with_raiting_10(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем новую книгу
        collector.add_new_book('Проклятые короли')
        #устанавливаем рейтинг 10
        collector.set_book_rating('Проклятые короли', 10)
        # добавляем вторую новую книгу
        collector.add_new_book('Безнадега')
        # устанавливаем рейтинг 9
        collector.set_book_rating('Безнадега', 9)
        # добавляем еще одну книгу
        collector.add_new_book('Сборник рецептов')
        # устанавливаем рейтинг 1
        collector.set_book_rating('Сборник рецептов', 1)
        #Проверяем, что в списке только книга с рейтингом 10
        assert collector.get_books_with_specific_rating(10) ==['Проклятые короли']

    def test_set_book_rating_down_one(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # Добавляем новую книгу
        collector.add_new_book('Сборник рецептов')
        # Устанавливаем рейтинг меньше 1
        collector.set_book_rating('Сборник рецептов', -2)

        assert collector.get_book_rating('Сборник рецептов') == 1

    def test_set_book_rating_high_ten(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # Добавляем книгу
        collector.add_new_book('Хоббит')
        #Устанавливаем рейтинг больше 10
        collector.set_book_rating('Хоббит', 11)

        c = collector.get_book_rating('Хоббит')

        assert c != 11

    def test_delete_book_from_favorites_add_two_diff_books_del_one(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        #добавляем две книги
        collector.add_new_book('Хоббит')
        collector.add_new_book('Сердце тьмы')
        #добавляем обе книги в избранное
        collector.add_book_in_favorites('Хоббит')
        collector.add_book_in_favorites('Сердце тьмы')
        #Удалаем одну книгу из избранного
        collector.delete_book_from_favorites('Хоббит')

        assert len(collector.get_list_of_favorites_books()) == 1