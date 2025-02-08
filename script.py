''' ага'''
import json
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="database_name"
    )

mycursor = mydb.cursor()

def execute_and_save(query):
    ''' khuhjhjh'''
    mycursor.execute(query)
    mydb.commit()
    return str(mycursor.rowcount) + " recordsinserted"

def execute_and_save_array(query):
    ''' kkjkjk'''
    r = 0
    for q in query:
        mycursor.execute(q)
        mydb.commit()
        r += mycursor.rowcount
    return str(r) + "records inserted"

def get_insert_manufactures_query(data_po):
    ''' kjkjkj'''
    for d in data_po:
        return "INSERT INTO manufacturers(name) \
           VALUES " + ",".join(f"('{vendor}')" for vendor in set(d["vendor"]))+";"


def get_insert_characteristics_query(data_pipi):
    ''' kjkjkjkj'''
    characteristics = []
    for x in data_pipi:
        for chara in x["characteristics"]:
            characteristics.append(chara.split(":")[0])

    characteristics = set(characteristics)
    for characteristic in characteristics:
        return "insert into characteristics(name) \
            values" + ",".join(f"('{characteristic}')")+";"


def get_insert_products_query(data_p):
    ''' jkjkj'''
    for d in data_p:
        products = [d["vendor_code"],d["name"],d["cost"],d["vendor"]]
        for a in products:
            return f"INSERT INTO products(name, price, manufacturer_id, manufacturer_code) \
                select '{a[1]}', {a[2]}, id, '{a[0]}' \
                from manufacturers \
                where name = '{a[3]}';"


def get_insert_product_characteristics_query(data_h):
    '''jkkj'''
    queries = []
    for product in data_h:
        vendor = product["vendor"]
        vendor_code = product["vendor_code"]
        for characteristic in product["characteristics"]:
            char_name, char_value = characteristic.split(":", 1)
            char_value = char_value.lstrip()
            query = f"""
                INSERT INTO product_characteristics (characteristic_id, product_id, value)
                SELECT characteristics.id, products.id, '{char_value}'
                FROM products
                JOIN manufacturers ON manufacturers.id = products.manufacturer_id
                JOIN characteristics ON characteristics.name = '{char_name}'
                WHERE manufacturers.name = '{vendor}'
                AND products.manufacturer_code = '{vendor_code}';
            """
            queries.append(query.strip())

    return queries



def fill_data(data_m):
    ''' kkjkjk'''
    r_m = execute_and_save(get_insert_manufactures_query(data_m))
    r_c = execute_and_save(get_insert_characteristics_query(data_m))
    r_p = execute_and_save_array(get_insert_products_query(data_m))
    r_pr = execute_and_save_array(get_insert_product_characteristics_query(data_m))
    print(r_m)
    print(r_c)
    print(r_p)
    print(r_pr)

data: dict = {}


def rr(file_path, encoding='utf-8'):
    '''kjkjk'''
    with open(file_path, 'r', encoding=encoding) as file:
        data_s = json.load(file)
        return data_s

rr('records.json')
fill_data(data)
