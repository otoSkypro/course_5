from src.dbmanager import DBManager
from src.headhunter import HeadHunter
from config import JSON_FILE_NAME, employer_ids
from sql.db_queries import create_tables, insert_to_employers, insert_to_vacancies
from utils import user_interaction


def main():
    hh = HeadHunter()
    vacancies_list = hh.get_vacancies_by_api(employer_ids)  # получаем вакансии
    hh.save_vacancies_to_json(vacancies_list, JSON_FILE_NAME)  # записываем вакансии в файл

    while 1:
        db_name = input('Введите слово на английском для названия базы данных: ')
        if all(one_letter in 'abcdefghijklmnopqrstuvwxyz1234567890' for one_letter in db_name):
            db = DBManager()
            break
        else:
            print("Введите слово на английском")
    # создаём БД
    db.create_database(db_name)
    # создаём таблицы в БД
    db.create_table(create_tables)
    # заполняем таблицы
    db.insert_data_to_table(JSON_FILE_NAME, insert_to_employers, insert_to_vacancies)

    # работаем с выборками в БД
    user_interaction(db)


if __name__ == 'main':
    main()