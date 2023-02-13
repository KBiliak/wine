from server import wineRepository


def create_wine(wine):
    print("create wine: wine =", wine)
    all_wines = wineRepository.get_wine()
    sort = wine['sort']

    for ex_wine in all_wines:
        if ex_wine['sort'] == sort:
            return {'error': 'wine with this sort already exists'}

    wineRepository.post_wine(wine)
    return None


def show_wine():
    wine = wineRepository.get_wine()
    print('all wines', wine)
    return wine
