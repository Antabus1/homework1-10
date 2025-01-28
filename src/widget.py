from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number: str) -> str:
    """
    принимает номер счёта или карты, маскирует его и возвращает
    :param number: номер карты или счёта
    :return: замаскированный номер карты или счета
    """
    if number[:4] == "Счет":
        res = get_mask_account(int(number[4:]))
    else:
        res = number[:-16] + get_mask_card_number(int(number[-16:]))
    return res


# "2024-03-11T02:26:18.671407"  "ДД.ММ.ГГГГ"
def get_date(date: str) -> str:
    """
    функция возвращает дату в формате "ДД.ММ.ГГГГ"
    :param date: дата в формате "2024-03-11T02:26:18.671407"
    :return: дата в формате "ДД.ММ.ГГГГ"
    """
    return date[8:10] + "." + date[5:7] + "." + date[:4]
    pass
