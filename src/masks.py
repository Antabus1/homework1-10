from settings import MASK1


def get_mask_card_number(number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера.
    То есть видны первые 6 цифр и последние 4 цифры,
    остальные символы отображаются звездочками, номер разбит
    по блокам по 4 цифры, разделенным пробелами.
    Пример работы функции:
    7000792289606361     # входной аргумент
    7000 79** **** 6361  # выход функции
    """
    temp_number = str(number)
    res = []
    for i in MASK1:
        if i == "*":
            temp_number = temp_number[1:]
            res.append("*")
        elif i == " ":
            res.append(" ")
        else:
            res.append(temp_number[0])
            temp_number = temp_number[1:]
    return "".join(res)


def get_mask_account(account: int) -> str:
    """Функция get_mask_account принимает на вход номер счета
    и возвращает его маску. Номер счета замаскирован и отображается
    в формате **XXXX, где X — это цифра номера. То есть видны
    только последние 4 цифры номера, а перед ними — две звездочки.
    Пример работы функции:
    73654108430135874305  # входной аргумент
    **4305  # выход функции
    """
    return "**" + str(account)[-4:]
