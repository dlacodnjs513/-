def get_area(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return width * height

def get_perimeter(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return 2 * (width + height)

def show_rectangle(x1, y1, x2, y2):
    print(f'좌측 상단 꼭지점이 ({x1}, {y1})이고 우측 하단 꼭지점이 ({x2}, {y2})인 사각형입니다.')

# 주 프로그램부
x1, y1 = 5, 5
x2, y2 = 20, 10

a = get_area(x1, y1, x2, y2)
p = get_perimeter(x1, y1, x2, y2)
show_rectangle(x1, y1, x2, y2)
print(f'\n넓이는 {a}, 둘레는 {p}')
