from model import *
from view import *
import sys
import sys  # sys нужен для передачи argv в QApplication

# Import the necessary packages
all_tables_list = 1
tables_dict = {"users": ["login", "name", "password", "phone"],
               "groups": ["id", "name", "description", "owner", "date"],
               "friends": ["status", "id", "id_user"],
               "walls": ["id", "id_user", "info"],
               "posts": ["description", "date", "title", "likes", "id", "id_walls"]}
tables = ["users", "groups", "friends", "walls", "posts"]
columns = [["login", "name", "password", "phone"],
           ["id", "name", "description", "owner", "date"],
           ["status", "id", "id_user"],
           ["id", "id_user", "info"],
           ["description", "date", "title", "likes", "id", "id_walls"]]
read_number = 2
insert_number = 3
delete_number = 4
update_number = 5
search_number = 6
random_fill = 7


class Controller():
    def __init__(self):
        self.db = Database()

c = Controller()

# printer(c.db.read("friends",["id"]))#read test
# printer(c.db.insert("friends",["status","id_user"], ["best","+380679201293"]))#insert test ничего не вернёт, поэтому нужно смотреть таблицу
# printer(c.db.delete("friends","id_user = '+380679201293'"))#delete test норм удалило
def print_footer(len):
    print("-" * len)


def menu():
    print_footer(38)
    print("Hello, it`s bdlab2 from Ivanenko Sanya")
    print_footer(38)
    print("Choose option:")
    print("1. Get all tables")
    print("2. Read")
    print("3. Insert")
    print("4. Delete")
    print("5. Update")
    print("6. Search")
    print("7. Fill random")
    chosen = input("Please, choose one: ")
    try:
        chosen = int(chosen)
    except Exception as error:
        print(error)
        return None
    return chosen


while (True):
    menu_number = menu()
    if menu_number == all_tables_list:
        for index, elem in enumerate(tables):
            print("Table:" + elem + "\n With columns: " + ",".join(columns[index]))
    elif menu_number == random_fill:
        c.db.fill_random()
    elif menu_number == read_number:
        chosen_table = input("Please, enter table from this list: " + "(" + ",".join(tables) + ") >> ")
        if chosen_table in tables:
            chosen_column = input("Please, enter columns from this list (splitted by comma): " + "(" + ",".join(
                tables_dict[chosen_table]) + ") >> ")
            chosen_column = chosen_column.split(',')
            printer(c.db.read(chosen_table, chosen_column))
    elif menu_number == insert_number:
        chosen_table = input(("Please, enter table from this list: " + "(" + ",".join(tables) + ") >> "))
        if chosen_table in tables:
            columns_list = input("Please, enter columns from this list (splitted by comma): " + "(" + ",".join(
                tables_dict[chosen_table]) + ") >> ")
            columns_list = columns_list.split(",")
            values = input("Please, enter values for each column(splitted by comma: >>")
            values = values.split(",")
            printer(c.db.insert(chosen_table, columns_list, values))
    elif menu_number == delete_number:
        chosen_table = input(("Please, enter table from this list: " + "(" + ",".join(tables) + ") >> "))
        if chosen_table in tables:
            condition = input("Please, enter condition for items to be deleted):" + " >> ")
        printer(c.db.delete(chosen_table, condition))

    elif menu_number == update_number:
        chosen_table = input(("Please, enter table from this list: " + "(" + ",".join(tables) + ") >> "))
        if chosen_table in tables:
            columns_list = input("Please, enter columns from this list (splitted by comma): " + "(" + ",".join(
                tables_dict[chosen_table]) + ") >> ")
            columns_list = columns_list.split(",")
            values = input("Please, enter values for each column(splitted by comma): >>")
            values = values.split(",")
            condition = input("Please, enter condition for items to be deleted):" + " >> ")
            printer(c.db.update(chosen_table, columns_list, values, condition))
        else:
            print(str(chosen_table) + "is not in tables list")
    elif menu_number == search_number:
        print("1. Пошук постів та по номеру телефону автора, опису поста та даті публікації\n"
              "2. Пошук людей по групах, на які вони підписані, по телефону та по даті оформлення підписки \n"
              "3. Пошук кількості вподобань на пості за тематикою, айді автора та ліміту кількості лайків \n")
        chosen_num = int(input("Enter num: >> "))
        if chosen_num == 1:
            attributes = ["+380%","< '2018-31-12'","another %"]
            # attributes[0] = input("Phone like:")
            # attributes[1] = input("Date cond:")
            # attributes[2] = input("Descriprion cond:")
            printer(c.db.search(1,attributes))
        if chosen_num == 2:
            attributes = ["about japan","between '2000-01-01' and '2020-12-12'","like '+380%'"]
            printer(c.db.search(2,attributes))
        if chosen_num == 3:
            attributes = None
            printer(c.db.search(3,attributes))
