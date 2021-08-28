import psycopg2

# host = "ec2-52-45-183-77.compute-1.amazonaws.com"
# database = 'daapamgkh1vf58'
# user = 'mlrhattekvwvkq'
# password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
# conn = psycopg2.connect(
#     host=host,
#     database=database,
#     user=user,
#     password=password,
#     port=5432
# )
# cursor = conn.cursor()
# cursor.execute("ALTER TABLE orders ADD COLUMN tulov_type VARCHAR ")
# conn.commit()
# print('succes')

def get_users():
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT user_id FROM users")
        res = cursor.fetchall()
    except Exception as e:
        print(e)
    conn.close()
    return res


def get_order_id(user_id):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT currunt_order FROM users WHERE user_id = {user_id}")
        res = cursor.fetchall()
    except Exception as e:
        print(e)
    conn.close()
    return res[0][0]


def add_user(first_name, id, username):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (first_name ,user_id, username ) VALUES (%s ,%s , %s)",
            (first_name, id, username))
        conn.commit()
    except:
        print("There is something wrong with your code adding")
    conn.close()


def order_create(order, user_id):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )

    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO orders (orders ,user_id) VALUES (%s , %s)",
            (order, user_id))
        conn.commit()
    except Exception as e:
        print(e)
        print("There is something wrong with your code create task")

    try:
        cursor.execute(
            f"SELECT * FROM orders WHERE orders='{order}'")
        res = cursor.fetchall()
        return int(res[0][0])
    except:
        print("There is something wrong with your code in create")

    conn.close()




def order_update_phone(phone_number, user_id):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"UPDATE  users SET phone_number1 = '{phone_number}' WHERE user_id = {user_id}")
        conn.commit()
    except:
        print("There is something wrong with your code updating phone")
    conn.close()




def order_update_location(latitude,longitude ,  user_id):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"UPDATE  orders SET latitude = '{latitude}', atitude = '{longitude}' WHERE id = {get_order_id(user_id)}")
        conn.commit()
    except Exception as e:
        print(e)
        print("There is something wrong with your code")
    conn.close()


def update_order_id(id, user_id):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"UPDATE  users SET currunt_order = {id} WHERE user_id={user_id}",
            {'id': id})
        conn.commit()
    except Exception as e:
        print(e)
        print("There is something wrong with your code in update")
    conn.close()


def get_order(user_id):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM orders where id = {get_order_id(user_id)}")
        res = cursor.fetchall()
    except Exception as e:
        print(e)
    conn.close()
    return res[0]


def get_user(user_id):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )

    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM users where user_id = {user_id}")
        res = cursor.fetchall()
    except Exception as e:
        print(e)
    conn.close()
    return res[0]

def update_tulov_type(type, user_id):
    host = "ec2-52-45-183-77.compute-1.amazonaws.com"
    database = 'daapamgkh1vf58'
    user = 'mlrhattekvwvkq'
    password = 'b4fdbc46c929a6f5ea6458e18dc19ef8a349372990bfc29a314595c507699377'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(
            f"UPDATE  orders SET tulov_type = '{type}' WHERE id={get_order_id(user_id)}")
        conn.commit()
    except Exception as e:
        print(e)
        print("There is something wrong with your code in update")
    conn.close()
