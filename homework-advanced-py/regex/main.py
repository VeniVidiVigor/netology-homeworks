from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код


def get_fio(text):
    res = re.findall(r"\b\w+\b", text)
    return res


def get_phone(text):
    if not text:
        return text
    else:
        number_by_groups = re.match(r"(\+7|8)\s*\D*\(*(\d{3,5})\)*\s*\D*(\d{3})\D*(\d{2})\D*(\d{2})\s*\D*(\d*)", text)
        if not number_by_groups:
            return text
        res = f"{'+7' if number_by_groups.group(1) == '+7' else '8'}({number_by_groups.group(2)})" \
              f"{number_by_groups.group(3)}-" \
              f"{number_by_groups.group(4)}-" \
              f"{number_by_groups.group(5)}{' доб. ' + number_by_groups.group(6) if number_by_groups.group(6) else ''}"
        return res


if __name__ == '__main__':
    new_phone_data = {}
    phone_data = contacts_list[1:]
    for row in phone_data:
        fio = get_fio(" ".join(row[0:3]))
        lastname = fio[0]
        my_dict = {'ФИО': fio, 'Организация': row[3],
                   'Должность': row[4], 'Телефон': get_phone(row[5]),
                   'Email': row[6]}
        if lastname not in new_phone_data:
            new_phone_data[lastname] = my_dict
        else:
            for key, new_val in my_dict.items():
                old_val = new_phone_data[lastname][key]
                if len(str(old_val)) < len(str(new_val)):
                    new_phone_data[lastname][key] = new_val
    new_phone_data_list = list(new_phone_data.values())
    rows = [['lastname', 'firstname', 'surename', 'organization', 'position', 'phone', 'email']]
    for dict_item in new_phone_data_list:
        sub_list = list(dict_item.values())
        row = sub_list[:1][0]
        row.extend(sub_list[1:len(sub_list)])
        rows.append(row)
        with open("phonebook.csv", "w", encoding="utf-8") as f:
            datawriter = csv.writer(f, delimiter=',')
            # Вместо contacts_list подставьте свой список
            datawriter.writerows(rows)

