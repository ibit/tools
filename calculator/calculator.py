number = float(input("数字を入力してください："))
operator = input("演算記号を選択してください：")

result = number

if operator == "+":
    result += number
elif operator == "-":
    result -= number
elif operator == "*":
    result *= number
elif operator == "/":
    result /= number

print("計算結果：", result)