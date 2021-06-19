import time


class Data:

    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def parser_data(cls, date):

        if Data.valide_data(date):
            data_list_str = date.split('-')
            data_list = []
            for i in data_list_str:
                try:
                    data_list.append(int(i))
                except ValueError as e:
                    print(f'{e} <<Не удалось преобразовать в число {i}>>')

            print(data_list)
            return f'День: {data_list[0]}, Месяц: {data_list[1]}, Год: {data_list[2]}'

    @staticmethod
    def valide_data(data):
        try:
            valid_date = time.strptime(data, '%d-%m-%Y')

            return True
        except ValueError:
            print('Invalid date!')


data_input = input('Введите дату в формате «день-месяц-год»: ')

data_int = Data.parser_data(data_input)

print(f'Результат: {data_int}, тип: {type(data_int)}')
