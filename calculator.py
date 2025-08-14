number = float(input("数字を入力してください："))
operator = input("演算子を入力してください：")
next_number = float(input("次の数字を入力してください："))

result = number

if operator == "+":
    result += next_number
elif operator == "-":
    result -= next_number
elif operator == "*":
    result *= next_number
elif operator == "/":
    result /= next_number
else:
    print("無効な演算子です。")
    exit()

print("計算結果：", result)
