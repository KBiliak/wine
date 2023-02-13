def post_wine(mysql, wine):
    with mysql.connection.cursor() as cursor:
        sql = f"insert into wine(year, sort) value('{wine['year']}'," \
              f" '{wine['sort']}')"
        cursor.execute(sql)
        mysql.connection.commit()


def get_wine(mysql):
    with mysql.connection.cursor() as cursor:
        sql = f"select * from wine"
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            wine = {
                'id': row[0],
                'year': row[1],
                'sort': row[2]
            }
            result.append(wine)
    return result
