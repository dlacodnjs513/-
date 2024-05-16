def buy(shopping_bag):
    print("[구입]")
    item = input("상품명? ")
    if item == '':
        return False
    quantity = int(input("수량은? "))
    shopping_bag[item] = quantity
    print(f'장바구니에 {item} {quantity}개가 담겼습니다.')
    return True

def show(shopping_bag):
    print(f'\n>>> 장바구니 보기: {shopping_bag}')

def find(shopping_bag):
    print("[검색]")
    search_item = input("장바구니에서 확인하고자 하는 상품은? ")
    if search_item in shopping_bag:
        print(f'{search_item}은(는) {shopping_bag[search_item]}개 담겨 있습니다.')
    else:
        print(f'{search_item}은(는) 장바구니에 없습니다.')

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
    show(shopping_bag)
    find(shopping_bag)
