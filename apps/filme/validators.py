import re
from datetime import datetime

def validate_data(data):
    """
        função para validação de dadas.

        - args:
            - data: data;

        - return: 
            - True: caso a data esteja no futuro.
            - False: caso a data esteja valida.
    """
    day = data.day
    month = data.month
    year = data.year

    if year > datetime.now().year or year < 1895:   # analisando o ano
        return True
    elif month > datetime.now().month and year == datetime.now().year():  # analisando o mes
        return True
    elif day > datetime.now().day and month == datetime.now().month and year == datetime.now().year():  # analisando o dia
        return True
    else: 
        return False
