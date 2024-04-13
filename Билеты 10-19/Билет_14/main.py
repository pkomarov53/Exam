import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.simpledialog import askstring
import pandas as pd


def read_file():
    global df
    file_path = filedialog.askopenfilename(title="Выберите файл")
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            df = pd.DataFrame([line.strip().split(',') for line in lines],
                              columns=['дата', 'номер зачетки', 'ФИО', 'группа', 'МДК', 'раздел', 'номер работы'])
            messagebox.showinfo("Успех", "Файл успешно загружен!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")
            df = None

def show_records(student_id):
    if df is not None:
        filtered_df = df[df['МДК'] == student_id]
        if not filtered_df.empty:
            file_path = f"records_{student_id}.xlsx"
            filtered_df.to_excel(file_path, index=False)
            messagebox.showinfo("Успех", f"Записи успешно сохранены в файле: {file_path}")
        else:
            messagebox.showwarning("Предупреждение", "Записи с указанным МДК не найдены.")
    else:
        messagebox.showwarning("Предупреждение", "Сначала загрузите файл.")

def add_record():
    global df
    if df is not None:
        date = askstring("Введите дату", "Введите дату (дд-мм-гг):")
        student_id = askstring("Введите номер зачетки", "Введите номер зачетки:")
        name = askstring("Введите ФИО студента", "Введите ФИО студента:")
        group = askstring("Введите группу", "Введите группу:")
        discipline = askstring("Введите дисциплину", "Введите дисциплину:")
        grade = askstring("Введите номер пары", "Введите номер пары:")

        if date and student_id and name and group and discipline and grade:
            new_record = [date, student_id, name, group, discipline, grade]
            df.loc[len(df)] = new_record

            # Сохранение DataFrame в текстовый файл
            file_path = "records.txt"
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(','.join(new_record) + '\n')

            messagebox.showinfo("Успех", "Запись успешно добавлена!")
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, заполните все поля.")
    else:
        messagebox.showwarning("Предупреждение", "Сначала загрузите файл.")

def print_file():
    global df
    if df is not None:
        header = ','.join(df.columns)

        data = ''
        for _, row in df.iterrows():
            data += ','.join(map(str, row)) + '\n'

        printable_text = header + '\n' + data

        with open("print_file.txt", "w", encoding="utf-8") as file:
            file.write(printable_text)

        messagebox.showinfo("Успех", "Файл успешно напечатан!")
    else:
        messagebox.showwarning("Предупреждение", "Сначала загрузите файл.")

def create_gui():
    global df
    df = None

    root = tk.Tk()
    root.title("Управление данными")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.grid(row=0, column=0, sticky="nsew")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    btn_load = tk.Button(frame, text="Загрузить файл", command=read_file)
    entry_student_id = tk.Entry(frame, width=20)
    btn_show = tk.Button(frame, text="Показать в Excel", command=lambda: show_records(entry_student_id.get()))
    btn_add = tk.Button(frame, text="Добавить запись", command=add_record)
    btn_print = tk.Button(frame, text="Печать файла", command=print_file)

    btn_load.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    entry_student_id.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    btn_show.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    btn_add.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    btn_print.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    root.mainloop()

if __name__ == "__main__":
    create_gui()
