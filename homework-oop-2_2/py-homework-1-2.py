cook_book = {}


def book():
    with open('recipes.txt', encoding='utf-8') as f:
        for i in f.read().split('\n\n'):
            lst = i.split('\n')
            dish = []
            for x in range(2, int(lst[1]) + 2):
                prod = lst[x].split(' | ')
                mini_dict = {'ingredient_name': prod[0], 'quantity': prod[1], 'measure': prod[2]}
                dish.append(mini_dict)
            cook_book[lst[0]] = dish


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            raise TypeError('Блюда нет')
        for ing in cook_book[dish]:
            if ing['ingredient_name'] not in shop_list:
                shop_list[ing['ingredient_name']] = (
                    {'measure': ing['measure'], 'quantity': int(ing['quantity']) * person_count})
            else:
                shop_list[ing['ingredient_name']]['quantity'] += int(ing['quantity']) * person_count
    print(shop_list)


book()
print(get_shop_list_by_dishes(['Омлет'], 3))
