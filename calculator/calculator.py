while True:
    number = float(input("数字を入力してください："))

    while True:
        operator = input("演算子を入力してください(計算を終了する場合はeを入力)：").lower()

        if operator == "e":
            break

        try:
            next_number = float(input("次の数字を入力してください："))
        except ValueError:
            print("数字を入力してください。")
            continue

        if operator == "+":
            number += next_number
        elif operator == "-":
            number -= next_number
        elif operator == "*":
            number *= next_number
        elif operator == "/":
            if next_number == 0:
                print("0で割ることはできません。")
                continue
            number /= next_number
        else:
            print("無効な演算子です。")
            continue

        print("途中結果：", number)

    print("最終結果：", number)
