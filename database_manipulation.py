import sqlite3


conn = sqlite3.connect('my_database.db')

c = conn.cursor()

c.execute('''
    SELECT Users.id, Users.name
    FROM Users
    JOIN Orders ON Users.id = Orders.user_id
    GROUP BY Users.id
    HAVING COUNT(Orders.id) > 5
''')
users_with_more_than_5_orders = c.fetchall()

print(users_with_more_than_5_orders)

c.execute('''
    SELECT Users.id, Users.name, SUM(Orders.amount)
    FROM Users
    JOIN Orders ON Users.id = Orders.user_id
    GROUP BY Users.id
''')
total_order_amount_per_user = c.fetchall()

print(total_order_amount_per_user)

c.execute('''
    UPDATE Users
    SET email = 'new_email@example.com'
    WHERE id = 1
''')
conn.commit()


