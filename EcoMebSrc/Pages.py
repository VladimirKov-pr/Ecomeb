from tkinter import *
import tkinter.ttk as ttk
import sqlite3
from EcoMebSrc import button_func
from tkinter import messagebox

'''
------------------------------
(написать документацию к проге со всеми нюансами и порядком добавления данных



Показать вадику прогу и спросить про связи таблиц (из каких таблиц брать данные для выбора из списка в поля ввода)
сказать оплату проги (7к + 3к(доработка с выпадающим меню и исключениями) в момент установки программы на комп и 
акцепта)
Протестировать на тестовых данных (попросить вадика сфотать каждую таблицу и самому заполнить)
руками писать с бумажки БД)
------------------------------
'''


class PageOne(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='#555')
        Label(self, text="Клиенты", width=700, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.tree = ttk.Treeview(self, column=("ID",
                                               "Имя",
                                               "Номер телефона",
                                               'e-mail',
                                               'Название продукции',
                                               'Дополнительные товары',
                                               'Дополнительные услуги'
                                               ), show='headings', selectmode="extended")
        self.tree.heading("#1", text="ID")
        self.tree.column("#1", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#2", text="Имя")
        self.tree.column("#2", minwidth=0, width=70, stretch=NO)
        self.tree.heading("#3", text="Номер телефона")
        self.tree.column("#3", minwidth=0, width=80, stretch=NO)
        self.tree.heading("#4", text="e-mail")
        self.tree.column("#4", minwidth=0, width=70, stretch=NO)
        self.tree.heading("#5", text="Название продукции")
        self.tree.column("#5", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#6", text="Дополнительные товары")
        self.tree.column("#6", minwidth=0, width=100, stretch=NO)
        self.tree.heading("#7", text="Дополнительные услуги")
        self.tree.column("#7", minwidth=0, width=170, stretch=NO)
        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        self.selected_data = []

        s = ttk.Style(self)
        s.theme_use('clam')

        b11 = Button(self, text="Добавить", command=self.on_add, width=10)
        b11.place(x=600, y=100)

        b12 = Button(self, text="Изменить", command=self.on_change, width=10)
        b12.place(x=600, y=130)

        b13 = Button(self, text="Удалить", command=self.on_delete, width=10)
        b13.place(x=600, y=160)

        conn = sqlite3.connect("example.db")
        cur = conn.cursor()
        select = cur.execute("SELECT * FROM Clients")

        for row in select:
            self.tree.insert('', END, values=row)
        conn.close()
        self.tree.pack(side=LEFT)

    def choose_set(self):
        inside_other = Toplevel()
        inside_other.geometry("500x250")
        inside_other.title("Выбрать набор")

        def set_data_from_listbox():
            selected = list(self.box.curselection())
            data_from_fields = []
            print(selected)
            for i in selected:
                data_from_fields.append(self.box.get(i))
            text_to_field = ';'.join(map(str, data_from_fields))
            print(text_to_field)
            self.prod.set(0)
            self.prod.set(text_to_field)
            inside_other.destroy()

        select = button_func.D_button_func()
        data_to_select = select.D_select_set()
        print(data_to_select)
        self.box = Listbox(inside_other, selectmode=MULTIPLE)
        self.box.grid(row=0, column=0)
        scroll = Scrollbar(inside_other, command=self.box.yview)
        scroll.grid(row=0, column=1)
        self.box.config(yscrollcommand=scroll.set)

        for i in range(len(data_to_select)):
            self.box.insert(END, data_to_select[i][0])

        Button(inside_other, text="Cохранить", command=set_data_from_listbox).grid(row=6, column=2,
                                                                                   padx=5, pady=5)
        Button(inside_other, text="Закрыть", command=inside_other.destroy).grid(row=6, column=0,
                                                                                padx=5, pady=5)

    def choose_details(self):
        inside_other = Toplevel()
        inside_other.geometry("500x250")
        inside_other.title("Выбрать Детали")

        def set_data_from_listbox():
            selected = list(self.box.curselection())
            data_from_fields = []
            print(selected)
            for i in selected:
                data_from_fields.append(self.box.get(i))
            text_to_field = ';'.join(map(str, data_from_fields))
            print(text_to_field)
            self.additional_goods.set(0)
            self.additional_goods.set(text_to_field)
            inside_other.destroy()

        select = button_func.D_button_func()
        data_to_select = select.D_select_details()
        print(data_to_select)

        self.box = Listbox(inside_other, selectmode=MULTIPLE)
        self.box.grid(row=0, column=0)
        scroll = Scrollbar(inside_other, command=self.box.yview)
        scroll.grid(row=0, column=1)
        self.box.config(yscrollcommand=scroll.set)

        for i in range(len(data_to_select)):
            self.box.insert(END, data_to_select[i][0])

        Button(inside_other, text="Cохранить", command=set_data_from_listbox).grid(row=6, column=2,
                                                                                   padx=5, pady=5)
        Button(inside_other, text="Закрыть", command=inside_other.destroy).grid(row=6, column=0,
                                                                                padx=5, pady=5)

    def choose_additional(self):
        inside_other = Toplevel()
        inside_other.geometry("500x250")
        inside_other.title("Выбрать Допольнительные услуги")

        def set_data_from_listbox():
            selected = list(self.box.curselection())
            data_from_fields = []
            for i in selected:
                data_from_fields.append(self.box.get(i))
            text_to_field = ';'.join(map(str, data_from_fields))
            print(text_to_field)
            self.additional_serv.set(0)
            self.additional_serv.set(text_to_field)
            inside_other.destroy()

        select = button_func.D_button_func()
        data_to_select = select.D_select_additional()

        self.box = Listbox(inside_other, selectmode=MULTIPLE)
        self.box.grid(row=0, column=0)
        scroll = Scrollbar(inside_other, command=self.box.yview)
        scroll.grid(row=0, column=1)
        self.box.config(yscrollcommand=scroll.set)

        for i in range(len(data_to_select)):
            self.box.insert(END, data_to_select[i][0])

        Button(inside_other, text="Cохранить", command=set_data_from_listbox).grid(row=6, column=2,
                                                                                   padx=5, pady=5)
        Button(inside_other, text="Закрыть", command=inside_other.destroy).grid(row=6, column=0,
                                                                                padx=5, pady=5)

    def warning(self):
        messagebox.showwarning('Внимание', 'Не выбрана запись таблицы')

    def selectItem(self, a):
        curItem = self.tree.focus()
        self.selected_data = self.tree.item(curItem)['values']

    def on_add(self):
        otherFrame = Toplevel()
        otherFrame.geometry("600x250")
        otherFrame.title("Добавить")

        Label(otherFrame, text="ФИО:").grid(row=0, column=0, padx=5, pady=5)
        Label(otherFrame, text="Номер телефона:").grid(row=1, column=0, padx=5, pady=5)
        Label(otherFrame, text="E-mail:").grid(row=2, column=0, padx=5, pady=5)
        Label(otherFrame, text="Название продукции:").grid(row=3, column=0, padx=5, pady=5)
        Label(otherFrame, text="Дополнительные товары:").grid(row=4, column=0, padx=5, pady=5)
        Label(otherFrame, text="Дополнительные услуги:").grid(row=5, column=0, padx=5, pady=5)

        name = StringVar()
        phone = StringVar()
        email = StringVar()
        self.prod = StringVar()
        self.additional_goods = StringVar()
        self.additional_serv = StringVar()

        def save_to_db1():
            data = [(name.get(), phone.get(), email.get(), self.prod.get(), self.additional_goods.get(),
                     self.additional_serv.get())]
            check = True
            for i in range(len(data[0])):
                if data[0][i] != '':
                    continue
                else:
                    check = False
            if not check:
                print('Пустые поля')
            else:
                add = button_func.D_button_func()
                add.D_add_row(data[0])
                # данные для удаления товара из приложения А
                diff_data = {}
                for i in range(len(data[0][3:])):
                    break_row_to_words_changed = data[0][i + 3].split(';')
                    diff_data[i + 4] = {'add': break_row_to_words_changed}

                for key, value in diff_data.items():
                    if key == 4:
                        add.D_set_from_A(value)
                    elif key == 5:
                        add.D_adiition_goods_from_A(value)
                    elif key == 6:
                        add.D_adiition_services_from_A(value)

                otherFrame.destroy()
                conn = sqlite3.connect('example.db')
                cur = conn.cursor()
                cur.execute("SELECT * FROM Clients ORDER BY client_id DESC LIMIT 1")
                self.tree.insert('', END, values=cur.fetchone())
                conn.close()

        Entry(otherFrame, textvariable=name).grid(row=0, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=phone).grid(row=1, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=email).grid(row=2, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=self.prod).grid(row=3, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=self.additional_goods).grid(row=4, column=1,
                                                                   padx=5, pady=5)
        Entry(otherFrame, textvariable=self.additional_serv).grid(row=5, column=1, padx=5,
                                                                  pady=5)

        Button(otherFrame, text="Выбрать из списка наборов", command=self.choose_set).grid(row=3, column=2,
                                                                                           padx=5, pady=5)
        Button(otherFrame, text="Выбрать из списка деталей набора", command=self.choose_details).grid(row=4, column=2,
                                                                                                      padx=5, pady=5)
        Button(otherFrame, text="Выбрать из списка дополнительных услуг", command=self.choose_additional).grid(row=5,
                                                                                                               column=2,
                                                                                                               padx=5,
                                                                                                               pady=5)
        Button(otherFrame, text="Cохранить", command=save_to_db1).grid(row=6, column=2,
                                                                       padx=5, pady=5)
        Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=6, column=0,
                                                                            padx=5, pady=5)

    def on_change(self):
        if len(self.selected_data) > 0:
            otherFrame = Toplevel()
            otherFrame.geometry("600x300")
            otherFrame.title("Изменить")

            Label(otherFrame, text="ФИО:").grid(row=0, column=0, padx=5, pady=5)
            Label(otherFrame, text="Номер телефона:").grid(row=1, column=0, padx=5, pady=5)
            Label(otherFrame, text="E-mail:").grid(row=2, column=0, padx=5, pady=5)
            Label(otherFrame, text="Название продукции:").grid(row=3, column=0, padx=5, pady=5)
            Label(otherFrame, text="Дополнительные товары:").grid(row=4, column=0, padx=5, pady=5)
            Label(otherFrame, text="Дополнительные услуги:").grid(row=5, column=0, padx=5, pady=5)

            name = StringVar()
            phone = StringVar()
            email = StringVar()
            self.prod = StringVar()
            self.additional_goods = StringVar()
            self.additional_serv = StringVar()

            def save_to_db1():
                data = [(name.get(), phone.get(), email.get(), self.prod.get(), self.additional_goods.get(),
                         self.additional_serv.get())]
                check = True
                for i in range(len(data[0])):
                    if data[0][i] != '':
                        continue
                    else:
                        check = False
                if not check:
                    print('Пустые поля')
                else:
                    change = button_func.D_button_func()
                    change.D_update_row(data[0], self.selected_data[0])
                    # разница списков для функции D_set_decimal_from_A, D_adiition_goods_decimal_from_A,
                    # D_adiition_services_decimal_from_A
                    diff_data = {}
                    for i in range(len(self.selected_data[4:])):
                        if self.selected_data[i + 4] not in data[0]:
                            break_row_to_words_selected = self.selected_data[i + 4].split(';')
                            break_row_to_words_changed = data[0][i + 3].split(';')
                            selected_shorter = list(set(break_row_to_words_changed) - set(break_row_to_words_selected))
                            selected_longer = list(set(break_row_to_words_selected) - set(break_row_to_words_changed))
                            selected_equal = [list(set(break_row_to_words_changed) - set(break_row_to_words_selected)),
                                              list(
                                                  set(break_row_to_words_selected) - set(break_row_to_words_changed))]
                            if len(break_row_to_words_selected) > len(break_row_to_words_changed):
                                diff_data[i + 4] = {'delete': selected_longer}
                            elif len(break_row_to_words_selected) < len(break_row_to_words_changed):
                                diff_data[i + 4] = {'add': selected_shorter}
                            elif len(break_row_to_words_selected) == len(break_row_to_words_changed):
                                diff_data[i + 4] = {'add': selected_equal[0], 'delete': selected_equal[1]}
                    # функции в зависимости от измененных данных
                    for key, value in diff_data.items():
                        if key == 4:
                            change.D_set_from_A(value)
                        elif key == 5:
                            change.D_adiition_goods_from_A(value)
                        elif key == 6:
                            change.D_adiition_services_from_A(value)
                    # очистка таблицы и вывод заново
                    otherFrame.destroy()
                    for i in self.tree.get_children():
                        self.tree.delete(i)
                    conn = sqlite3.connect('example.db')
                    cur = conn.cursor()
                    select = cur.execute("SELECT * FROM Clients")
                    for row in select:
                        self.tree.insert('', END, values=row)
                    conn.close()

            Entry(otherFrame, textvariable=name).grid(row=0, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=phone).grid(row=1, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=email).grid(row=2, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=self.prod).grid(row=3, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=self.additional_goods).grid(row=4, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=self.additional_serv).grid(row=5, column=1, padx=5, pady=5)
            name.set(self.selected_data[1])
            phone.set(self.selected_data[2])
            email.set(self.selected_data[3])
            self.prod.set(self.selected_data[4])
            self.additional_goods.set(self.selected_data[5])
            self.additional_serv.set(self.selected_data[6])
            Button(otherFrame, text="Выбрать из списка наборов", command=self.choose_set).grid(row=3, column=2,
                                                                                               padx=5, pady=5)
            Button(otherFrame, text="Выбрать из списка деталей набора", command=self.choose_details).grid(row=4,
                                                                                                          column=2,
                                                                                                          padx=5,
                                                                                                          pady=5)
            Button(otherFrame, text="Выбрать из списка дополнительных услуг", command=self.choose_additional).grid(
                row=5,
                column=2,
                padx=5,
                pady=5)

            Button(otherFrame, text="Cохранить", command=save_to_db1).grid(row=6, column=2,
                                                                           padx=5, pady=5)
            Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=6, column=0,
                                                                                padx=5, pady=5)
        else:
            self.warning()

    def on_delete(self):
        if len(self.selected_data) > 0:
            delete = button_func.D_button_func()
            delete.D_delete_row(self.selected_data[0])
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect('example.db')
            cur = conn.cursor()
            select = cur.execute("SELECT * FROM Clients")
            for row in select:
                self.tree.insert('', END, values=row)
            conn.close()
        else:
            self.warning()


class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='#555')
        Label(self, text="Детали", width=700, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        self.tree = ttk.Treeview(self, column=("ID детали",
                                               "Название детали",
                                               "Есть",
                                               "Готово",
                                               "Не хватает",
                                               "Нужно"), show='headings', selectmode="extended")
        self.tree.heading("#1", text="ID детали")
        self.tree.column("#1", minwidth=0, width=100, stretch=NO)
        self.tree.heading("#2", text="Название детали")
        self.tree.column("#2", minwidth=0, width=150, stretch=NO)
        self.tree.heading("#3", text="Есть")
        self.tree.column("#3", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#4", text="Готово")
        self.tree.column("#4", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#5", text="Не хватает")
        self.tree.column("#5", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#6", text="Нужно")
        self.tree.column("#6", minwidth=0, width=50, stretch=NO)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)

        b21 = Button(self, text="Добавить", command=self.on_add, width=10)
        b21.place(x=460, y=100)

        b22 = Button(self, text="Изменить", command=self.on_change, width=10)
        b22.place(x=460, y=130)

        b23 = Button(self, text="Удалить", command=self.on_delete, width=10)
        b23.place(x=460, y=160)

        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Details")
        self.tree.tag_configure('odd', background='#ffcccb')
        self.tree.tag_configure('even', background='#fed8b1')
        selected_data = cur.fetchall()
        for row in selected_data:
            if row[4] > 0:
                self.tree.insert('', END, values=row, tags=('odd',))
            else:
                self.tree.insert('', END, values=row)
        conn.close()
        self.tree.pack(side=LEFT)

    def selectItem(self, a):
        curItem = self.tree.focus()
        self.selected_data1 = self.tree.item(curItem)['values']

    def warning(self):
        messagebox.showwarning('Внимание', 'Не выбрана запись таблицы')

    def on_add(self):
        otherFrame = Toplevel()
        otherFrame.geometry("550x250")
        otherFrame.title("Добавить")
        Label(otherFrame, text="Наименование детали:").grid(row=2, column=2, padx=5, pady=5)
        Label(otherFrame, text="Количество:").grid(row=3, column=2, padx=5, pady=5)
        Label(otherFrame, text="Готово:").grid(row=4, column=2, padx=5, pady=5)
        Label(otherFrame, text="Нехватает:").grid(row=5, column=2, padx=5, pady=5)
        Label(otherFrame, text="Необходимо:").grid(row=6, column=2, padx=5, pady=5)

        self.name_of_detail = StringVar()
        amount = IntVar()
        ready = IntVar()
        not_enough = IntVar()
        need = IntVar()

        def save_to_db2():
            data = [self.name_of_detail.get(), amount.get(), ready.get(), not_enough.get(), need.get()]
            check = True
            for i in range(len(data[0])):
                if data[0][i] != '':
                    continue
                else:
                    check = False
            if not check:
                print('Пустые поля')
            else:
                if int(data[2]) > 0:
                    data[1] = data[1] - data[2]
                    print(data)
                    if data[2] < data[4]:
                        data[3] = data[4] - data[2]
                    print(data)
                    data_to_F = 0
                    if data[2] >= data[4]:
                        while data[2] >= data[4]:
                            data_to_F += 1
                            data[2] = data[2] - data[4]
                        print([data[0], data_to_F])
                        add = button_func.C_button_func()
                        add.C_set_ready_to_F([data[0], data_to_F])
                        add.C_add_row(data)
                else:
                    add = button_func.C_button_func()
                    add.C_add_row(data)
                otherFrame.destroy()
                for i in self.tree.get_children():
                    self.tree.delete(i)
                conn = sqlite3.connect('example.db')
                cur = conn.cursor()
                cur.execute("SELECT * FROM Details")
                selected_data = cur.fetchall()
                for row in selected_data:
                    if row[4] > 0:
                        self.tree.insert('', END, values=row, tags=('odd',))
                    else:
                        self.tree.insert('', END, values=row)
                conn.close()

        Entry(otherFrame, textvariable=self.name_of_detail).grid(row=2, column=3, padx=5, pady=5)
        Entry(otherFrame, textvariable=amount).grid(row=3, column=3, padx=3, pady=5)
        Entry(otherFrame, textvariable=ready).grid(row=4, column=3, padx=4, pady=5)
        Entry(otherFrame, textvariable=not_enough).grid(row=5, column=3, padx=5, pady=5)
        Entry(otherFrame, textvariable=need).grid(row=6, column=3, padx=6, pady=5)

        Button(otherFrame, text="Cохранить", command=save_to_db2).grid(row=9, column=3, padx=5, pady=5)
        Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=9, column=2, padx=5,
                                                                            pady=5)

    def on_change(self):
        try:
            otherFrame = Toplevel()
            otherFrame.geometry("400x300")
            otherFrame.title("Изменить")

            Label(otherFrame, text="Наименование детали:").grid(row=2, column=2, padx=5, pady=5)
            Label(otherFrame, text="Количество:").grid(row=3, column=2, padx=5, pady=5)
            Label(otherFrame, text="Готово:").grid(row=4, column=2, padx=5, pady=5)
            Label(otherFrame, text="Нехватает:").grid(row=5, column=2, padx=5, pady=5)
            Label(otherFrame, text="Необходимо:").grid(row=6, column=2, padx=5, pady=5)

            self.name_of_detail = StringVar()
            amount = StringVar()
            ready = StringVar()
            not_enough = StringVar()
            need = StringVar()

            def save_to_db2():
                data = [self.name_of_detail.get(), int(amount.get()), int(ready.get()), int(not_enough.get()),
                        int(need.get())]
                check = True
                for i in range(len(data[0])):
                    if data[0][i] != '':
                        continue
                    else:
                        check = False
                if not check:
                    print('Пустые поля')
                else:
                    if int(data[2]) > 0:
                        data[1] = data[1] - data[2]
                        print(data)
                        if data[2] < data[4]:
                            data[3] = data[4] - data[2]
                        print(data)
                        data_to_F = 0
                        if data[2] >= data[4]:
                            while data[2] >= data[4]:
                                data_to_F += 1
                                data[2] = data[2] - data[4]
                            print([data[0], data_to_F])
                            change = button_func.C_button_func()
                            change.C_set_ready_to_F([data[0], data_to_F])
                            print(self.selected_data1)
                            change.C_update_row(data, self.selected_data1[0])
                    else:
                        change = button_func.C_button_func()
                        change.C_update_row(data, self.selected_data1[0])

                    otherFrame.destroy()
                    for i in self.tree.get_children():
                        self.tree.delete(i)
                    conn = sqlite3.connect('example.db')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Details")
                    selected_data = cur.fetchall()
                    for row in selected_data:
                        if row[4] > 0:
                            self.tree.insert('', END, values=row, tags=('odd',))
                        else:
                            self.tree.insert('', END, values=row)
                    conn.close()

            Entry(otherFrame, textvariable=self.name_of_detail, state=DISABLED).grid(row=2, column=3, padx=5, pady=5)
            Entry(otherFrame, textvariable=amount).grid(row=3, column=3, padx=3, pady=5)
            Entry(otherFrame, textvariable=ready).grid(row=4, column=3, padx=4, pady=5)
            Entry(otherFrame, textvariable=not_enough).grid(row=5, column=3, padx=5, pady=5)
            Entry(otherFrame, textvariable=need).grid(row=6, column=3, padx=6, pady=5)

            self.name_of_detail.set(self.selected_data1[1])
            amount.set(self.selected_data1[2])
            ready.set(self.selected_data1[3])
            not_enough.set(self.selected_data1[4])
            need.set(self.selected_data1[5])

            Button(otherFrame, text="Cохранить", command=save_to_db2).grid(row=9, column=3, padx=5, pady=5)
            Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=9, column=2, padx=5,
                                                                                pady=5)
        except AttributeError as er:
            self.warning()

    def on_delete(self):
        try:
            delete = button_func.C_button_func()
            delete.C_delete_row(self.selected_data1[0])
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect('example.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM Details")
            selected_data = cur.fetchall()
            for row in selected_data:
                if row[4] > 0:
                    self.tree.insert('', END, values=row, tags=('odd',))
                else:
                    self.tree.insert('', END, values=row)
            conn.close()
        except AttributeError as er:
            self.warning()


class PageThree(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='#555')
        Label(self, text="Готовая продукция", width=700, font=('Helvetica', 18, "bold")).pack(side="top", fill="x",
                                                                                              pady=5)

        self.tree = ttk.Treeview(self, column=("ID готовой продукции",
                                               "Название продукции",
                                               "Название детали",
                                               "Количество",
                                               "Не хватает",
                                               "Нужно"), show='headings', selectmode="extended")
        self.tree.heading("#1", text="ID готовой продукции")
        self.tree.column("#1", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#2", text="Название продукции")
        self.tree.column("#2", minwidth=0, width=150, stretch=NO)
        self.tree.heading("#3", text="Название детали")
        self.tree.column("#3", minwidth=0, width=150, stretch=NO)
        self.tree.heading("#4", text="Количество")
        self.tree.column("#4", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#5", text="Не хватает")
        self.tree.column("#5", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#6", text="Нужно")
        self.tree.column("#6", minwidth=0, width=50, stretch=NO)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)

        b31 = Button(self, text="Добавить", command=self.on_add, width=10)
        b31.place(x=510, y=100)

        b32 = Button(self, text="Изменить", command=self.on_change, width=10)
        b32.place(x=510, y=130)

        b33 = Button(self, text="Удалить", command=self.on_delete, width=10)
        b33.place(x=510, y=160)

        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Finished_products")

        self.tree.tag_configure('odd', background='#ffcccb')
        self.tree.tag_configure('even', background='white')

        selected_data = cur.fetchall()

        for row in selected_data:
            if 0 < int(row[4]) < int(row[5]):
                self.tree.insert('', END, values=row, tags=('odd',))
            else:
                self.tree.insert('', END, values=row, tags=('even',))
        conn.close()
        self.tree.pack(side=LEFT)

    def selectItem(self, a):
        curItem = self.tree.focus()
        self.selected_data = self.tree.item(curItem)['values']

    def warning(self):
        messagebox.showwarning('Внимание', 'Не выбрана запись таблицы')

    def choose_set(self):
        inside_other = Toplevel()
        inside_other.geometry("500x250")
        inside_other.title("Выбрать набор")

        def set_data_from_listbox():
            selected = list(self.box.curselection())
            data_from_fields = []
            print(selected)
            for i in selected:
                data_from_fields.append(self.box.get(i))
            text_to_field = ';'.join(map(str, data_from_fields))
            print(text_to_field)
            self.name_of_prod.set(0)
            self.name_of_prod.set(text_to_field)
            inside_other.destroy()

        select = button_func.D_button_func()
        data_to_select = select.D_select_set()
        print(data_to_select)
        self.box = Listbox(inside_other, selectmode=SINGLE)
        self.box.grid(row=0, column=0)
        scroll = Scrollbar(inside_other, command=self.box.yview)
        scroll.grid(row=0, column=1)
        self.box.config(yscrollcommand=scroll.set)

        for i in range(len(data_to_select)):
            self.box.insert(END, data_to_select[i][0])

        Button(inside_other, text="Cохранить", command=set_data_from_listbox).grid(row=6, column=2,
                                                                                   padx=5, pady=5)
        Button(inside_other, text="Закрыть", command=inside_other.destroy).grid(row=6, column=0,
                                                                                padx=5, pady=5)

    def choose_details(self):
        inside_other = Toplevel()
        inside_other.geometry("500x250")
        inside_other.title("Выбрать Детали")

        def set_data_from_listbox():
            selected = list(self.box.curselection())
            data_from_fields = []
            print(selected)
            for i in selected:
                data_from_fields.append(self.box.get(i))
            text_to_field = ';'.join(map(str, data_from_fields))
            print(text_to_field)
            self.name_of_set.set(0)
            self.name_of_set.set(text_to_field)
            inside_other.destroy()

        select = button_func.D_button_func()
        data_to_select = select.D_select_details()
        print(data_to_select)

        self.box = Listbox(inside_other, selectmode=SINGLE)
        self.box.grid(row=0, column=0)
        scroll = Scrollbar(inside_other, command=self.box.yview)
        scroll.grid(row=0, column=1)
        self.box.config(yscrollcommand=scroll.set)

        for i in range(len(data_to_select)):
            self.box.insert(END, data_to_select[i][0])

        Button(inside_other, text="Cохранить", command=set_data_from_listbox).grid(row=6, column=2,
                                                                                   padx=5, pady=5)
        Button(inside_other, text="Закрыть", command=inside_other.destroy).grid(row=6, column=0,
                                                                                padx=5, pady=5)

    def on_add(self):
        otherFrame = Toplevel()
        otherFrame.geometry("550x250")
        otherFrame.title("Добавить")
        Label(otherFrame, text="Название продукции:").grid(row=0, column=0, padx=5, pady=5)
        Label(otherFrame, text="Название детали:").grid(row=1, column=0, padx=5, pady=5)
        Label(otherFrame, text="Количество:").grid(row=2, column=0, padx=5, pady=5)
        Label(otherFrame, text="Не хватает:").grid(row=3, column=0, padx=5, pady=5)
        Label(otherFrame, text="Нужно:").grid(row=4, column=0, padx=5, pady=5)

        self.name_of_prod = StringVar()
        self.name_of_set = StringVar()
        amount = IntVar()
        not_enough = IntVar()
        needed = IntVar()

        def save_to_db3():
            data = [self.name_of_prod.get(), self.name_of_set.get(), amount.get(), not_enough.get(), needed.get()]
            check = True
            for i in range(len(data)):
                if data[i] != '':
                    continue
                else:
                    check = False
            if not check:
                print('Пустые поля')
            else:
                if int(data[2]) > int(data[4]):
                    data[3] = 0
                    add = button_func.A_button_func()
                    add.A_add_row(data)
                    add.A_summ_set(data)
                else:
                    data[3] = int(data[4]) - int(data[2])
                    add = button_func.A_button_func()
                    add.A_add_row(data)
                    add.A_summ_set(data)

                    otherFrame.destroy()
                    for i in self.tree.get_children():
                        self.tree.delete(i)
                    conn = sqlite3.connect('example.db')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Finished_products")
                    selected_data = cur.fetchall()
                    for row in selected_data:
                        if 0 < int(row[4]) < int(row[5]):
                            self.tree.insert('', END, values=row, tags=('odd',))
                        else:
                            self.tree.insert('', END, values=row)
                    conn.close()

        Entry(otherFrame, textvariable=self.name_of_prod).grid(row=0, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=self.name_of_set).grid(row=1, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=amount).grid(row=2, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=not_enough).grid(row=3, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=needed).grid(row=4, column=1, padx=5, pady=5)

        Button(otherFrame, text="Выбрать из списка наборов", command=self.choose_set).grid(row=0, column=2,
                                                                                           padx=5, pady=5)
        Button(otherFrame, text="Выбрать из списка деталей набора", command=self.choose_details).grid(row=1, column=2,
                                                                                                      padx=5, pady=5)
        Button(otherFrame, text="Cохранить", command=save_to_db3).grid(row=5, column=2, padx=5, pady=5)
        Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=5, column=0, padx=5,
                                                                            pady=5)

    def on_change(self):
        try:
            otherFrame = Toplevel()
            otherFrame.geometry("550x250")
            otherFrame.title("Изменить")
            Label(otherFrame, text="Название продукции:").grid(row=0, column=0, padx=5, pady=5)
            Label(otherFrame, text="Название детали:").grid(row=1, column=0, padx=5, pady=5)
            Label(otherFrame, text="Количество:").grid(row=2, column=0, padx=5, pady=5)
            Label(otherFrame, text="Не хватает:").grid(row=3, column=0, padx=5, pady=5)
            Label(otherFrame, text="Нужно:").grid(row=4, column=0, padx=5, pady=5)

            self.name_of_prod = StringVar()
            self.name_of_set = StringVar()
            amount = IntVar()
            not_enough = IntVar()
            needed = IntVar()

            def save_to_db3():
                data = [self.name_of_prod.get(), self.name_of_set.get(), amount.get(), not_enough.get(), needed.get()]
                check = True
                for i in range(len(data)):
                    if data[i] != '':
                        continue
                    else:
                        check = False
                if not check:
                    print('Пустые поля')
                else:
                    if int(data[2]) > int(data[4]):
                        data[3] = 0
                        change = button_func.A_button_func()
                        change.A_update_row(self.selected_data[0], data)
                        change.A_summ_set(data)
                    else:
                        data[3] = int(data[4]) - int(data[2])
                        change = button_func.A_button_func()
                        change.A_update_row(self.selected_data[0], data)
                        change.A_summ_set(data)

                    otherFrame.destroy()
                    for i in self.tree.get_children():
                        self.tree.delete(i)
                    conn = sqlite3.connect('example.db')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Finished_products")
                    selected_data = cur.fetchall()
                    for row in selected_data:
                        if 0 < int(row[4]) < int(row[5]):
                            self.tree.insert('', END, values=row, tags=('odd',))
                        else:
                            self.tree.insert('', END, values=row)
                    conn.close()

            Entry(otherFrame, textvariable=self.name_of_prod).grid(row=0, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=self.name_of_set).grid(row=1, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=amount).grid(row=2, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=not_enough).grid(row=3, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=needed).grid(row=4, column=1, padx=5, pady=5)

            self.name_of_prod.set(self.selected_data[1])
            self.name_of_set.set(self.selected_data[2])
            amount.set(self.selected_data[3])
            not_enough.set(self.selected_data[4])
            needed.set(self.selected_data[5])

            Button(otherFrame, text="Выбрать из списка наборов", command=self.choose_set).grid(row=0, column=2,
                                                                                               padx=5, pady=5)
            Button(otherFrame, text="Выбрать из списка деталей набора", command=self.choose_details).grid(row=1,
                                                                                                          column=2,
                                                                                                          padx=5,
                                                                                                          pady=5)

            Button(otherFrame, text="Cохранить", command=save_to_db3).grid(row=5, column=2, padx=5, pady=5)
            Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=5, column=0, padx=5,
                                                                                pady=5)
        except AttributeError as er:
            self.warning()

    def on_delete(self):
        try:
            delete = button_func.A_button_func()
            delete.A_delete_row(self.selected_data[0])
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect('example.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM Finished_products")
            self.tree.tag_configure('odd', background='#ffcccb')
            self.tree.tag_configure('even', background='#fed8b1')
            selected_data = cur.fetchall()
            for row in selected_data:
                if 0 < int(row[4]) < int(row[5]):
                    self.tree.insert('', END, values=row, tags=('odd',))
                else:
                    self.tree.insert('', END, values=row)
            conn.close()
        except AttributeError as er:
            self.warning()


class PageFour(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='#555')
        Label(self, text="Упаковка", width=700, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        self.tree = ttk.Treeview(self, column=("ID Упаковки",
                                               "Название набора",
                                               "Количество",
                                               "Упаковано"), show='headings', selectmode="extended")
        self.tree.heading("#1", text="ID упаковки")
        self.tree.column("#1", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#2", text="Название набора")
        self.tree.column("#2", minwidth=0, width=150, stretch=NO)
        self.tree.heading("#3", text="Количество")
        self.tree.column("#3", minwidth=0, width=100, stretch=NO)
        self.tree.heading("#4", text="Упаковано")
        self.tree.column("#4", minwidth=100, width=100, stretch=NO)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)

        b41 = Button(self, text="Добавить", command=self.on_add, width=10)
        b41.place(x=560, y=100)

        b42 = Button(self, text="Изменить", command=self.on_change, width=10)
        b42.place(x=560, y=130)

        b43 = Button(self, text="Удалить", command=self.on_delete, width=10)
        b43.place(x=560, y=160)

        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        select = cur.execute("SELECT * FROM Packaging")
        for row in select:
            self.tree.insert('', END, values=row)
        conn.close()
        self.tree.pack(side=LEFT, padx=150)

    def choose_details(self):
        inside_other = Toplevel()
        inside_other.geometry("500x250")
        inside_other.title("Выбрать Детали")

        def set_data_from_listbox():
            selected = list(self.box.curselection())
            data_from_fields = []
            print(selected)
            for i in selected:
                data_from_fields.append(self.box.get(i))
            text_to_field = ';'.join(map(str, data_from_fields))
            print(text_to_field)
            self.name_of_set.set(0)
            self.name_of_set.set(text_to_field)
            inside_other.destroy()

        select = button_func.F_button_func()
        data_to_select = select.F_select_details()
        print(data_to_select)

        self.box = Listbox(inside_other, selectmode=MULTIPLE)
        self.box.grid(row=0, column=0)
        scroll = Scrollbar(inside_other, command=self.box.yview)
        scroll.grid(row=0, column=1)
        self.box.config(yscrollcommand=scroll.set)

        for i in range(len(data_to_select)):
            self.box.insert(END, data_to_select[i][0])

        Button(inside_other, text="Cохранить", command=set_data_from_listbox).grid(row=6, column=2,
                                                                                   padx=5, pady=5)
        Button(inside_other, text="Закрыть", command=inside_other.destroy).grid(row=6, column=0,
                                                                                padx=5, pady=5)

    def selectItem(self, a):
        curItem = self.tree.focus()
        self.selected_data = self.tree.item(curItem)['values']

    def warning(self):
        messagebox.showwarning('Внимание', 'Не выбрана запись таблицы')

    def on_add(self):
        otherFrame = Toplevel()
        otherFrame.geometry("400x300")
        otherFrame.title("Добавить")
        Label(otherFrame, text="Название набора:").grid(row=0, column=0, padx=5, pady=5)
        Label(otherFrame, text="Количество:").grid(row=1, column=0, padx=5, pady=5)
        Label(otherFrame, text="Упаковано:").grid(row=2, column=0, padx=5, pady=5)

        self.name_of_set = StringVar()
        amount = IntVar()
        packed = IntVar()

        def save_to_db4():
            data = [(self.name_of_set.get(), amount.get(), packed.get())]
            check = True
            for i in range(len(data[0])):
                if data[0][i] != '':
                    continue
                else:
                    check = False
            if not check:
                print('Пустые поля')
            else:
                add = button_func.F_button_func()
                diff_data = [data[0][0], data[0][1], data[0][2]]
                add.F_set_packed_to_A(diff_data)
                diff_data[1] = int(diff_data[1]) - int(diff_data[2])
                diff_data[2] = 0
                add.F_add_row(diff_data)

                otherFrame.destroy()
                conn = sqlite3.connect('example.db')
                cur = conn.cursor()
                cur.execute("SELECT * FROM Packaging ORDER BY package_id DESC LIMIT 1")
                self.tree.insert('', END, values=cur.fetchone())
                conn.close()

        Entry(otherFrame, textvariable=self.name_of_set).grid(row=0, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=amount).grid(row=1, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=packed).grid(row=2, column=1, padx=5, pady=5)

        Button(otherFrame, text="Выбрать из списка деталей набора", command=self.choose_details).grid(row=0, column=2,
                                                                                                      padx=5, pady=5)
        Button(otherFrame, text="Cохранить", command=save_to_db4).grid(row=3, column=2, padx=5, pady=5)
        Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=3, column=0, padx=5,
                                                                            pady=5)

    def on_change(self):
        try:
            otherFrame = Toplevel()
            otherFrame.geometry("400x300")
            otherFrame.title("Изменить")
            Label(otherFrame, text="Название набора:").grid(row=0, column=0, padx=5, pady=5)
            Label(otherFrame, text="Количество:").grid(row=1, column=0, padx=5, pady=5)
            Label(otherFrame, text="Упаковано:").grid(row=2, column=0, padx=5, pady=5)

            self.name_of_set = StringVar()
            amount = IntVar()
            packed = IntVar()

            def save_to_db4():
                data = [(self.name_of_set.get(), amount.get(), packed.get())]
                check = True
                for i in range(len(data[0])):
                    if data[0][i] != '':
                        continue
                    else:
                        check = False
                if not check:
                    print('Пустые поля')
                else:
                    change = button_func.F_button_func()
                    diff_data = [data[0][0], data[0][1], data[0][2]]
                    change.F_set_packed_to_A(diff_data)
                    diff_data[1] = int(diff_data[1]) - int(diff_data[2])
                    diff_data[2] = 0
                    change.F_update_row(diff_data, self.selected_data[0])

                    otherFrame.destroy()
                    for i in self.tree.get_children():
                        self.tree.delete(i)
                    conn = sqlite3.connect('example.db')
                    cur = conn.cursor()
                    select = cur.execute("SELECT * FROM Packaging")
                    for row in select:
                        self.tree.insert('', END, values=row)
                    conn.close()

            Entry(otherFrame, textvariable=self.name_of_set, state=DISABLED).grid(row=0, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=amount).grid(row=1, column=1, padx=5, pady=5)
            Entry(otherFrame, textvariable=packed).grid(row=2, column=1, padx=5, pady=5)
            self.name_of_set.set(self.selected_data[1])
            amount.set(self.selected_data[2])
            packed.set(self.selected_data[3])

            Button(otherFrame, text="Cохранить", command=save_to_db4).grid(row=3, column=2, padx=5, pady=5)
            Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=3, column=0, padx=5,
                                                                                pady=5)
        except AttributeError as er:
            self.warning()

    def on_delete(self):
        try:
            delete = button_func.F_button_func()
            delete.F_delete_row(self.selected_data[0])
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect('example.db')
            cur = conn.cursor()
            select = cur.execute("SELECT * FROM Packaging")
            for row in select:
                self.tree.insert('', END, values=row)
            conn.close()
        except AttributeError as er:
            self.warning()


class PageFive(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg='#555')
        Label(self, text="Готовые кухонные наборы", width=700, font=('Helvetica', 18, "bold")).pack(side="top",
                                                                                                    fill="x", pady=5)

        self.tree = ttk.Treeview(self, column=("ID готового набора",
                                               "Название продукции",
                                               "Количество"), show='headings', selectmode="extended")
        self.tree.heading("#1", text="ID готового набора")
        self.tree.column("#1", minwidth=0, width=50, stretch=NO)
        self.tree.heading("#2", text="Название продукции")
        self.tree.column("#2", minwidth=0, width=150, stretch=NO)
        self.tree.heading("#3", text="Количество")
        self.tree.column("#3", minwidth=0, width=100, stretch=NO)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)

        b51 = Button(self, text="Добавить", command=self.on_add, width=10)
        b51.place(x=510, y=100)

        b52 = Button(self, text="Изменить", command=self.on_change, width=10)
        b52.place(x=510, y=130)

        b53 = Button(self, text="Удалить", command=self.on_delete, width=10)
        b53.place(x=510, y=160)

        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Ready_made_kitchen_sets")
        self.tree.tag_configure('odd', background='#ffcccb')
        self.tree.tag_configure('even', background='#fed8b1')
        selected_data = cur.fetchall()

        for row in selected_data:
            if 0 < int(row[2]) <= 5:
                self.tree.insert('', END, values=row, tags=('even',))
            elif int(row[2]) == 0:
                self.tree.insert('', END, values=row, tags=('odd',))
            else:
                self.tree.insert('', END, values=row)
        conn.close()
        self.tree.pack(side=LEFT, padx=200)

    def selectItem(self, a):
        curItem = self.tree.focus()
        self.selected_data1 = self.tree.item(curItem)['values']

    def warning(self):
        messagebox.showwarning('Внимание', 'Не выбрана запись таблицы')

    def on_add(self):
        otherFrame = Toplevel()
        otherFrame.geometry("550x250")
        otherFrame.title("Добавить")
        Label(otherFrame, text="Название продукции:").grid(row=0, column=0, padx=5, pady=5)
        Label(otherFrame, text="Количество:").grid(row=1, column=0, padx=5, pady=5)

        self.name_of_production = StringVar()
        amount = IntVar()

        def save_to_db2():
            data = [(self.name_of_production.get(), amount.get())]
            check = True
            for i in range(len(data[0])):
                if data[0][i] != '':
                    continue
                else:
                    check = False
            if not check:
                print('Пустые поля')
            else:
                add = button_func.B_button_func()
                add.B_add_row(data[0])
                otherFrame.destroy()
                for i in self.tree.get_children():
                    self.tree.delete(i)
                conn = sqlite3.connect('example.db')
                cur = conn.cursor()
                cur.execute("SELECT * FROM Ready_made_kitchen_sets")
                self.tree.tag_configure('odd', background='#ffcccb')
                self.tree.tag_configure('even', background='#fed8b1')
                selected_data = cur.fetchall()

                for row in selected_data:
                    if 0 < int(row[2]) <= 5:
                        self.tree.insert('', END, values=row, tags=('even',))
                    elif int(row[2]) == 0:
                        self.tree.insert('', END, values=row, tags=('odd',))
                    else:
                        self.tree.insert('', END, values=row)
                conn.close()

        Entry(otherFrame, textvariable=self.name_of_production).grid(row=0, column=1, padx=5, pady=5)
        Entry(otherFrame, textvariable=amount).grid(row=1, column=1, padx=3, pady=5)

        Button(otherFrame, text="Cохранить", command=save_to_db2).grid(row=2, column=3, padx=5, pady=5)
        Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=2, column=1, padx=5,
                                                                            pady=5)

    def on_change(self):
        try:
            otherFrame = Toplevel()
            otherFrame.geometry("550x250")
            otherFrame.title("Добавить")
            Label(otherFrame, text="Название продукции:").grid(row=0, column=0, padx=5, pady=5)
            Label(otherFrame, text="Количество:").grid(row=1, column=0, padx=5, pady=5)

            self.name_of_production = StringVar()
            amount = IntVar()

            def save_to_db2():
                data = [(self.name_of_production.get(), amount.get())]
                check = True
                for i in range(len(data[0])):
                    if data[0][i] != '':
                        continue
                    else:
                        check = False
                if not check:
                    print('Пустые поля')
                else:
                    add = button_func.B_button_func()
                    add.B_update_row(self.selected_data1[0], data[0])
                    otherFrame.destroy()
                    for i in self.tree.get_children():
                        self.tree.delete(i)
                    conn = sqlite3.connect('example.db')
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM Ready_made_kitchen_sets")
                    self.tree.tag_configure('odd', background='#ffcccb')
                    self.tree.tag_configure('even', background='#fed8b1')
                    selected_data = cur.fetchall()

                    for row in selected_data:
                        if 0 < int(row[2]) <= 5:
                            self.tree.insert('', END, values=row, tags=('even',))
                        elif int(row[2]) == 0:
                            self.tree.insert('', END, values=row, tags=('odd',))
                        else:
                            self.tree.insert('', END, values=row)
                    conn.close()

            Entry(otherFrame, textvariable=self.name_of_production, state=DISABLED).grid(row=0, column=1, padx=5,
                                                                                         pady=5)
            Entry(otherFrame, textvariable=amount).grid(row=1, column=1, padx=3, pady=5)

            self.name_of_production.set(self.selected_data1[1])
            amount.set(self.selected_data1[2])

            Button(otherFrame, text="Cохранить", command=save_to_db2).grid(row=2, column=2, padx=5, pady=5)
            Button(otherFrame, text="Закрыть", command=otherFrame.destroy).grid(row=2, column=1, padx=5,
                                                                                pady=5)
        except AttributeError as er:
            self.warning()

    def on_delete(self):
        try:
            delete = button_func.B_button_func()
            delete.B_delete_row(self.selected_data1[0])
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect('example.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM Ready_made_kitchen_sets")
            self.tree.tag_configure('odd', background='#ffcccb')
            self.tree.tag_configure('even', background='#fed8b1')
            selected_data = cur.fetchall()

            for row in selected_data:
                if 0 < int(row[2]) <= 5:
                    self.tree.insert('', END, values=row, tags=('even',))
                elif int(row[2]) == 0:
                    self.tree.insert('', END, values=row, tags=('odd',))
                else:
                    self.tree.insert('', END, values=row)
            conn.close()
        except AttributeError as er:
            self.warning()
