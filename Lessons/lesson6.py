# nums = [2, 7, 11, 15]
# target = 9
#
# def two_sum(nums, target):
#     num_map = {}
#
#     for index, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return [num_map[complement], index]
#         num_map[num] = index
#
# print(two_sum(nums, target))


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

add_user('Ardager', 25, 'спать')