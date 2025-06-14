import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import json
import datetime

class CalendarApp:
    def __init__(self, master):
        '''
        Инициализация календаря. Настройка представления через модуль datetime. Возможность считывать файлы JSON по прописанным путям в "load_...". Создание кнопки "Информация" с легендой цветов и мероприятий.
        '''
        self.master = master
        self.master.title('Календарь')
        
        self.calendar = Calendar(master, selectmode='day', year=datetime.datetime.now().year, 
                                 month=datetime.datetime.now().month, day=datetime.datetime.now().day)
        self.calendar.pack(pady=20)

        self.load_holidays_and_weekends('./days_off.json')
        self.load_study_periods('./study_periods.json')
        
        self.plot_calendar()
        
        self.btn_info = tk.Button(master, text='Информация', command=self.show_info)
        self.btn_info.pack(pady=10)

    def load_holidays_and_weekends(self, filename):
        '''
        Функция загрузки файла с праздниками и/или выходными. Часть с ошибками позволяет проверять выбранные файлы более эффективно.
        '''
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.weekends = data.get('Выходной', [])
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл с выходными днями не найден.")
            self.weekends = []
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
            self.weekends = []
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            self.weekends = []

    def load_study_periods(self, filename):
        '''
        Функция загрузки файла с учебными периодами. Последовательность периодов может быть произвольной. Часть с ошибками позволяет проверять выбранные файлы более эффективно.
        '''
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.study_periods = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл с учебными периодами не найден.")
            self.study_periods = []
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
            self.study_periods = []
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            self.study_periods = []

    def plot_calendar(self):
        '''
        Вывод виджета календаря. Считываются даты и тэги (типы мероприятий) в указанном формате из файлов, затем выводятся на календаре так, что каждый цвет определенной даты соответствует определенному событию. Легенда цветов прописана у каждого из методов tag_config и подлежит изменению. 
        '''
        for weekend in self.weekends:
            date = datetime.datetime.strptime(weekend, '%Y-%m-%d')
            self.calendar.calevent_create(date, "Выходной", 'weekend')

        for period in self.study_periods:
            self.add_study_period(period)

        self.calendar.tag_config('weekend', background='gray')
        self.calendar.tag_config('theory', background='steelblue')
        self.calendar.tag_config('practice', background='forestgreen')
        self.calendar.tag_config('exam', background='darkviolet')
        self.calendar.tag_config('consultation', background='orange')
        self.calendar.tag_config('trial_ride', background='indianred')

    def add_study_period(self, period):
        start_date = datetime.datetime.strptime(period['start_date'], '%Y-%m-%d')
        end_date = datetime.datetime.strptime(period['end_date'], '%Y-%m-%d')

        current_date = start_date
        while current_date <= end_date:
            if current_date.strftime('%Y-%m-%d') not in self.weekends:
                if period['type'] == 'theory':
                    self.calendar.calevent_create(current_date, "Период теории", 'theory')
                elif period['type'] == 'practice':
                    self.calendar.calevent_create(current_date, "Период практики", 'practice')
                elif period['type'] == 'exam':
                    self.calendar.calevent_create(current_date, "Экзамен", 'exam')
                elif period['type'] == 'consultation':
                    self.calendar.calevent_create(current_date, "Консультация", 'consultation')
                elif period['type'] == 'trial_ride':
                    self.calendar.calevent_create(current_date, "Пробная поездка", 'trial_ride')

            current_date += datetime.timedelta(days=1)

    def show_info(self):
        '''
        Текстовая часть, появляющаяся в окне при нажатии кнопки "Информация". Отражает легенду цветов мероприятий в виджете календаря.
        '''
        legend = (
            "Легенда цветов:\n"
            "Выходной - Серый\n"
            "Период теории - Синий\n"
            "Период практики - Зеленый\n"
            "Экзамен - Темно-фиолетовый\n"
            "Консультация - Оранжевый\n"
            "Пробная поездка - Розовый"
        )
        messagebox.showinfo("Информация", legend)

if __name__ == '__main__':
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()