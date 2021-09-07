def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'


if __name__ == "__main__":
    result = format_price(56.24)
    print(result)
