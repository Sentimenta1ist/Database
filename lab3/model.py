import psycopg2 as ps
from configparser import ConfigParser


class Database:
    def request(self, req, fetch_results=False):
        pass

    def config(self, filename='config.ini', section='postgresql'):
        parser = ConfigParser()
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db

    def get_request(self, req, get_results=False):
        try:
            cursor = self.conn.cursor()
            cursor.execute(req)
            self.conn.commit()
            if cursor.description is not None:
                self.colnames = [desc[0] for desc in cursor.description]
            if get_results:
                return cursor.fetchall(), self.colnames
            else:
                self.conn.commit()
                return True
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            self.conn.rollback()
            self.gen_error = error
            self.erFlag = True
            print(error)
            return False

    def __init__(self):
        self.conn = None
        self.error = ''
        self.gen_error = ''
        self.erFlag = False
        self.Gen = True
        self.colnames = list()
        try:
            params = self.config('config.ini')
            self.conn = ps.connect(**params)
            print(self.conn)

        except(Exception, ps.DatabaseError) as error:
            print(error)

    def test(self):
        req = "SELECT * FROM book;"
        return self.get_request(req, True)

    def read(self, table, columns):
        req = "SELECT %s FROM %s" % (",".join(columns) if (columns is not None and len(columns) != 0) else "*", table)
        return self.get_request(req, True)

    def delete(self, table, cond):
        req = "DELETE FROM %s WHERE %s" % (table, cond)
        return self.get_request(req)

    def search(self, mode, attributes):
        req = ""

        if mode == 1:
            select = "SELECT p.title,p.description,u.name FROM posts p "
            join = "JOIN walls w ON w.id=p.id_walls JOIN Users u ON w.id_user=u.phone "
            cond = "WHERE w.id_user LIKE '{}' AND p.date {} AND p.description LIKE '{}'".format(attributes[0],
                                                                                                attributes[1],
                                                                                                attributes[2])
            req = select + join + cond
        elif mode == 2:
            select = "SELECT u.name,g.name FROM users u JOIN users_groups_rel rel ON u.phone=rel.user_fk "
            join = "JOIN groups g ON g.id=rel.groups_fk where g.name='anime group' and g.date = '2020-01-02' and u.phone like '+380%' GROUP BY g.name, u.name "
            # cond = "WHERE g.name='{0}' and date {1} and u.phone {2}".format(attributes[0],
            #                                                                attributes[1],
            #                                                                attributes[2])
            #cond = "where g.name='about japan' and date > '2000-01-01' and '2020-12-12' and u.phone like '+380%'"
            req = select + join
        elif mode == 3:
            req = "select p.likes from Posts p join Walls w on w.id=p.id_walls where title='birthday!' and id_user='+380679201293' and likes>0"
        return self.get_request(req, True)

    def insert(self, table, columns_data, values_data, count=1):
        columns = ",".join(columns_data)
        raw_values = ",".join([x.lstrip("!") if x.startswith("!") else "'{}'".format(x) for x in values_data])
        values = ",".join(["({0})".format(raw_values) for x in range(0, count)])
        req = "INSERT INTO %s (%s) VALUES %s" % (table, columns, values)
        print(req)
        return self.get_request(req)

    def update(self, table, column_data, value_data, cond):
        update_query = ",".join(
            ["{} = {}".format(element[0],
                              element[1].lstrip("!") if element[1].startswith("!")
                              else "'{}'".format(element[1]))
             for element in zip(column_data, value_data)])
        req = "UPDATE {0} SET {1} WHERE {2}".format(table, update_query, cond)
        return self.get_request(req)

    def by_key_value(self, key, value):
        return "{0}='{1}'".format(key, value)

    def len_eq(self, key, len):
        return "length({0}) = {1}".format(key, len)

    def gen_int_req(self, min, range):
        return "! trunc({0}+random()*{1})::int".format(min, range)

    def gen_date(self):
        return "! timestamp '2004-01-10' + random() * (timestamp '2004-01-20' - timestamp '2004-01-10')"

    def gen_date_string(self):
        return "! {0} || '-' || {1} || '-' || {2}".format(self.gen_string_req(4)[1:],
                                                          self.gen_string_req(2)[1:],
                                                          self.gen_string_req(2)[1:])

    def gen_string_req(self, len, min_char=65, char_range=25):
        req = ["chr(trunc({0}+random()*{1})::int)".format(min_char, char_range)]
        return "!" + "||".join(req * len)

    def fill_random(self):
        return self.insert(
            "users",
            ["login", "name", "password", "phone"],
            [self.gen_string_req(3),
             self.gen_string_req(14),
             self.gen_string_req(7),
             self.gen_string_req(10)],
            int(input("Input count of random users to insert: ")))
