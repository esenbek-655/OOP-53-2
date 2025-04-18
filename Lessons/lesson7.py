# import sqlite3
#
#
# connect = sqlite3.connect('users.db')
# # ручка с рукой
# cursor = connect.cursor()
#
#
#
# cursor.execute('''
#     CREATE TABLE users(
#         name VARCHAR (50) NOT NULL,
#         age INTEGER NOT NULL,
#         hobby TEXT
#     )
# ''')
# connect.commit()
#
import sqlite3


# A4
connect = sqlite3.connect('Users.db')
# Рука с Ручкой
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()








def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"пользватель добавлен: {name}")


# name = input("Введите ваше имя")
#
#
# add_user('Ardager', 25, 'спать')
#

def get_all_users():
    cursor.execute('SELECT * FROM users')

    users = cursor.fetchall()
    print(users)

    if users:
        print("Список всех пользвателей")

        for i in users:
            print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
    else:
        print("Список пуст!!")
get_all_users()


def update_user_by_rowid(name, id):
    cursor.execute(
        'UPDATE users SET name = ? WHERE worwid = ?',
        (name, id)
    )
    connect.commit()

    # update_user_by_id(name: "Esenbek", id:2)


def delete_user_by_id(id):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        parameters: (id,)
    )