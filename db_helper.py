import psycopg2


def get_users():
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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


def get_task_id(user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT task_id FROM users WHERE user_id = {user_id}")
        res = cursor.fetchall()
    except Exception as e:
        print(e)
    conn.close()
    return res[0][0]


def add_user(first_name, id, username):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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


def task_create(name, user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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
            "INSERT INTO Tasks (task_name ,user_id) VALUES (%s , %s)",
            (name, user_id))
        conn.commit()
    except Exception as e:
        print(e)
        print("There is something wrong with your code create task")

    try:
        cursor.execute(
            f"SELECT * FROM Tasks WHERE task_name='{name}'")
        res = cursor.fetchall()
        return int(res[0][0])
    except:
        print("There is something wrong with your code in create")

    conn.close()


def task_update_descrip(description, user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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
            f"UPDATE  Tasks SET description = '{description}' WHERE id = {get_task_id(user_id)}",
            {'description': description})
        conn.commit()
    except Exception as e:
        print(e)
        print("There is something wrong with your code in update description")
    conn.close()


def task_update_phone(phone_number, user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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
            f"UPDATE  Tasks SET phone_number = '{phone_number}' WHERE id = {get_task_id(user_id)}")
        conn.commit()
    except:
        print("There is something wrong with your code updating phone")
    conn.close()


def task_update_photo(photo_path, user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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
            f"UPDATE  Tasks SET photo = '{photo_path}' WHERE id = {get_task_id(user_id)}")
        conn.commit()
    except:
        print("There is something wrong with your code updating photo")
    conn.close()


def task_update_price(price, user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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
            f"UPDATE  Tasks SET price = '{price}' WHERE id = {get_task_id(user_id)}")
        conn.commit()
    except:
        print("There is something wrong with your code updating price")
    conn.close()


def task_update_region(name, user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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
            f"UPDATE  Tasks SET region = '{name}' WHERE id = {get_task_id(user_id)}")
        conn.commit()
    except:
        print("There is something wrong with your code")
    conn.close()


def update_task_id(id, user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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
            f"UPDATE  users SET task_id = {id} WHERE user_id={user_id}",
            {'id': id})
        conn.commit()
    except Exception as e:
        print(e)
        print("There is something wrong with your code in update")
    conn.close()


def get_regions():
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT name FROM regions")
        res = cursor.fetchall()
    except Exception as e:
        print(e)
    conn.close()
    return res


def get_task(user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=5432
    )
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM Tasks where id = {get_task_id(user_id)}")
        res = cursor.fetchall()
    except Exception as e:
        print(e)
    conn.close()
    return res[0]


def get_user(user_id):
    host = "ec2-35-174-56-18.compute-1.amazonaws.com"
    database = 'deng6efpk22ass'
    user = 'vunsszpfqfoilr'
    password = '9da912988502a0e913534cea85939d231bd7e762c2110407cdf8bbc578255954'
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
