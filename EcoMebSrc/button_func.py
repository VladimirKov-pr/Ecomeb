# Приложение А
import sqlite3


class A_button_func:
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cur = self.conn.cursor()

    def A_add_row(self, data):
        print(data)
        self.cur.execute("INSERT INTO Finished_products (name_of_production,name_of_part,amount,not_enough,"
                         "needed) VALUES(?,?,?,?,?)",
                         (data[0], data[1], data[2], data[3], data[4]))
        self.conn.commit()

    def A_delete_row(self, Id):
        self.cur.execute("DELETE FROM Finished_products WHERE ready_part_id=?", (Id,))
        self.conn.commit()

    def A_update_row(self, Id, data):
        self.cur.execute("UPDATE Finished_products SET name_of_production = ?, name_of_part = ?, amount = ?, "
                         "not_enough = ?, needed = ?  WHERE ready_part_id = ?",
                         (data[0], data[1], data[2], data[3], data[4], Id))
        self.conn.commit()

    def A_summ_set(self, data):
        self.cur.execute("SELECT * FROM Finished_products WHERE name_of_production = ?", (data[0],))
        data_to_check = self.cur.fetchall()
        data_to_summ = []
        ready_counter = 0
        for i in range(len(data_to_check)):
            if (data_to_check[i][3] - data_to_check[i][5]) >= 0:
                ready_counter += 1
                data_to_summ.append([data_to_check[i][0], data_to_check[i][1], data_to_check[i][2], data_to_check[i][3],
                                     data_to_check[i][4], data_to_check[i][5]])
        print(ready_counter)
        if ready_counter == len(data_to_check):
            for j in range(len(data_to_summ)):
                print(data_to_summ)
                print(j)
                data_to_summ[j][3] = data_to_summ[j][3] - data_to_summ[j][5]
                self.cur.execute('UPDATE Finished_products SET amount= ?,not_enough= ? WHERE name_of_part = ?',
                                 (data_to_summ[j][3], data_to_summ[j][4], data_to_summ[j][2]))
                self.conn.commit()
            self.cur.execute('SELECT * FROM Ready_made_kitchen_sets WHERE name_of_production = ?', (data[0],))
            data_from_B = self.cur.fetchall()
            print(data_from_B)
            data_plus_to_B = [data_from_B[0][2] + 1, data_from_B[0][1]]
            self.cur.execute('UPDATE Ready_made_kitchen_sets SET amount = ? WHERE name_of_production = ?',
                             (data_plus_to_B[0], data_plus_to_B[1]))
            self.conn.commit()

    def A_select_set(self):
        self.cur.execute('SELECT DISTINCT name_of_production FROM Finished_products WHERE NOT '
                         'name_of_production="Доп. услуги"')
        return self.cur.fetchall()

    def A_select_details(self):
        self.cur.execute('SELECT DISTINCT name_of_part FROM Finished_products WHERE NOT '
                         'name_of_production="Доп. услуги"')
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()


# Приложение В
class B_button_func:
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cur = self.conn.cursor()

    def B_add_row(self, data):
        self.cur.execute("INSERT INTO Ready_made_kitchen_sets (name_of_production, amount) VALUES (?, ?)",
                         (data[0], data[1]))
        self.conn.commit()

    def B_delete_row(self, Id):
        self.cur.execute("DELETE FROM Ready_made_kitchen_sets WHERE ready_set_id=?", (Id,))
        self.conn.commit()

    def B_update_row(self, Id, data):
        self.cur.execute("UPDATE Ready_made_kitchen_sets SET name_of_production = ?, amount = ? WHERE ready_set_id = ?",
                         (data[0], data[1], Id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# Приложение С
class C_button_func:
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cur = self.conn.cursor()

    def C_add_row(self, data):
        self.cur.execute("INSERT INTO Details (name_of_detail, amount, ready, not_enough, need) VALUES (?, ?, ?, ?, ?)",
                         (data[0], data[1], data[2], data[3], data[4]))
        self.conn.commit()

    def C_delete_row(self, Id):
        self.cur.execute("DELETE FROM Details WHERE part_id=?", (Id,))
        self.conn.commit()

    def C_update_row(self, data, Id):
        self.cur.execute("UPDATE Details SET name_of_detail = ?, amount = ?, ready = ?, not_enough = ?, need = ? "
                         "WHERE part_id = ?",
                         (data[0], data[1], data[2], data[3], data[4], Id))
        self.conn.commit()

    def C_set_ready_to_F(self, data):
        self.cur.execute("SELECT amount FROM Packaging WHERE set_name = ?", (data[0],))
        amount_from_F = self.cur.fetchall()
        print(amount_from_F)
        amount_to_F = [int(amount_from_F[0][0]) + int(data[1])]
        self.cur.execute("UPDATE Packaging SET amount = ?  WHERE set_name = ?", (amount_to_F[0], data[0]))

    def __del__(self):
        self.conn.close()


# Приложение F
class F_button_func:
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cur = self.conn.cursor()

    def F_add_row(self, data):
        self.cur.execute("INSERT INTO Packaging (set_name, amount, packed) VALUES ( ?, ?, ?)",
                         (data[0], data[1], data[2]))
        self.conn.commit()

    def F_delete_row(self, Id):
        self.cur.execute("DELETE FROM Packaging WHERE package_id=?", (Id,))
        self.conn.commit()

    def F_update_row(self, data, Id):
        self.cur.execute("UPDATE Packaging SET set_name = ?, amount = ?, packed = ? WHERE package_id = ?",
                         (data[0], data[1], data[2], Id))
        self.conn.commit()

    def F_set_packed_to_A(self, data):
        try:
            self.cur.execute('SELECT * FROM Finished_products WHERE name_of_part = ?', (data[0],))
            selected = self.cur.fetchall()
            print(selected)
            data_to_A = [int(selected[0][3]) + data[2], selected[0][2]]
            print(data_to_A)
            self.cur.execute('UPDATE Finished_products SET amount = ? WHERE name_of_part = ?', (data_to_A[0],
                                                                                                data_to_A[1]))
            self.conn.commit()
            self.cur.execute('SELECT * FROM Finished_products WHERE name_of_part = ?', (data[0],))
            data_from_A = self.cur.fetchall()
            if data_from_A[0][3] >= data_from_A[0][5]:
                data_to_A_recount = [data_from_A[0][2], 0]
                self.cur.execute('UPDATE Finished_products SET not_enough = ? WHERE name_of_part = ?', (
                    data_to_A_recount[1], data_to_A_recount[0]))
                self.conn.commit()
            else:
                data_to_A_recount = [data_from_A[0][2], data_from_A[0][5] - data_from_A[0][3]]
                self.cur.execute('UPDATE Finished_products SET not_enough = ? WHERE name_of_part = ?', (
                    data_to_A_recount[1], data_to_A_recount[0]))
                self.conn.commit()
        except IndexError:
            print('error')

    def F_select_details(self):
        self.cur.execute('SELECT DISTINCT name_of_detail FROM Details')
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()


# Приложение D
class D_button_func:
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cur = self.conn.cursor()

    def D_add_row(self, data):
        self.cur.execute("INSERT INTO Clients (name, phone_number, email, name_of_production, adiition_goods, "
                         "addition_services) VALUES (?, ?, ?, ?, ?, ?)", (data[0], data[1],
                                                                          data[2], data[3],
                                                                          data[4], data[5]))
        self.conn.commit()

    def D_delete_row(self, Id):
        self.cur.execute("DELETE FROM Clients WHERE client_id=?", (Id,))
        self.conn.commit()

    def D_update_row(self, data, Id):
        self.cur.execute("UPDATE Clients SET name = ?, phone_number = ?, email = ?, name_of_production = ?, "
                         "adiition_goods = ?, addition_services = ? WHERE client_id = ?",
                         (data[0], data[1], data[2], data[3], data[4], data[5], Id))
        self.conn.commit()

    def D_set_from_A(self, data):  # проверить
        print(data)
        for key, value in data.items():
            # сделать циклы как в D_set_from_A в 2х след функциях
            if key == 'add':
                for i in value:
                    self.cur.execute("SELECT amount-1,not_enough+1,name_of_part FROM Finished_products WHERE "
                                     "name_of_production = ?",
                                     (i,))
                    exist_data = self.cur.fetchall()
                    print(exist_data)
                    for j in exist_data:
                        self.cur.execute(
                            "UPDATE Finished_products SET amount = ?, not_enough = ? WHERE name_of_production = ? AND "
                            "name_of_part = ?",
                            (j[0], j[1], i, j[2]))
                    self.conn.commit()
            elif key == 'delete':
                for i in value:
                    self.cur.execute("SELECT amount+1,not_enough-1,name_of_part FROM Finished_products WHERE "
                                     "name_of_production = ?",
                                     (i,))
                    exist_data = self.cur.fetchall()
                    print(exist_data)
                    for j in exist_data:
                        self.cur.execute(
                            "UPDATE Finished_products SET amount = ?, not_enough = ? WHERE name_of_production = ? AND "
                            "name_of_part = ?",
                            (j[0], j[1], i, j[2]))
                    self.conn.commit()

    def D_adiition_goods_from_A(self, data):  # проверить
        print(data)
        for key, value in data.items():
            if key == 'add':
                for i in value:
                    self.cur.execute("SELECT amount-1,not_enough+1 FROM Finished_products WHERE "
                                     "name_of_part = ?",
                                     (i,))
                    exist_data = self.cur.fetchall()
                    print(exist_data)
                    for j in exist_data:
                        self.cur.execute("UPDATE Finished_products SET amount = ?, not_enough = ? WHERE "
                                         "name_of_part = ?",
                                         (j[0], j[1], i))
                        self.conn.commit()
            elif key == 'delete':
                for i in value:
                    self.cur.execute("SELECT amount+1,not_enough-1 FROM Finished_products WHERE "
                                     "name_of_part = ?",
                                     (i,))
                    exist_data = self.cur.fetchall()
                    for j in exist_data:
                        self.cur.execute("UPDATE Finished_products SET amount = ?, not_enough = ? WHERE "
                                         "name_of_part = ?",
                                         (j[0], j[1], i))
                        self.conn.commit()

    def D_adiition_services_from_A(self, data):  # проверить
        print(data)
        for key, value in data.items():
            if key == 'add':
                for i in value:
                    self.cur.execute("SELECT amount-1,not_enough+1 FROM Finished_products WHERE "
                                     "name_of_part = ?",
                                     (i,))
                    exist_data = self.cur.fetchall()
                    print(exist_data)
                    for j in exist_data:
                        self.cur.execute("UPDATE Finished_products SET amount = ?, not_enough = ? WHERE "
                                         "name_of_part = ?",
                                         (j[0], j[1], i))
                        self.conn.commit()
            elif key == 'delete':
                for i in value:
                    self.cur.execute("SELECT amount+1,not_enough-1 FROM Finished_products WHERE "
                                     "name_of_part = ?",
                                     (i,))
                    exist_data = self.cur.fetchall()
                    for j in exist_data:
                        self.cur.execute("UPDATE Finished_products SET amount = ?, not_enough = ? WHERE "
                                         "name_of_part = ?",
                                         (j[0], j[1], i))
                        self.conn.commit()

    def D_select_set(self):
        self.cur.execute('SELECT DISTINCT name_of_production FROM Finished_products WHERE NOT '
                         'name_of_production="Доп. услуги"')
        return self.cur.fetchall()

    def D_select_details(self):
        self.cur.execute('SELECT DISTINCT name_of_part FROM Finished_products WHERE NOT '
                         'name_of_production="Доп. услуги" ')
        return self.cur.fetchall()

    def D_select_additional(self):
        self.cur.execute('SELECT DISTINCT name_of_part FROM Finished_products WHERE '
                         'name_of_production="Доп. услуги"')
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()
