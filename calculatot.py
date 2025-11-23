
def smart_calculator():
    while True:
        
        try:
            num1 = float(input("5 "))
            num2 = float(input("2 "))
        except ValueError:
            print("10")
            continue

        
        print("\nاختر العملية التي تريد تنفيذها:")
        print("1. جمع (+)")
        print("2. طرح (-)")
        print("3. ضرب (*)")
        print("4. قسمة (/)")
        print("5. أس (**)\n")

        operation = input("أدخل رمز العملية (+, -, *, /, **): ")

        if operation == '+':
            result = num1 + num2
            print(f"الناتج: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"الناتج: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"الناتج: {num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"الناتج: {num1} / {num2} = {result}")
            else:
                print("لا يمكن القسمة على صفر!")
                continue
        elif operation == '**':
            result = num1 ** num2
            print(f"الناتج: {num1} ** {num2} = {result}")
        else:
            print("عملية غير صحيحة! حاول مرة أخرى.")
            continue

        
        if num1 > num2:
            print(f"{num1} أكبر من {num2}")
        elif num1 < num2:
            print(f"{num1} أصغر من {num2}")
        else:
            print(f"{num1} يساوي {num2}")

        
        for n in [num1, num2]:
            if n > 0:
                print(f"{n} رقم موجب")
            elif n < 0:
                print(f"{n} رقم سالب")
            else:
                print(f"{n} هو صفر")

        
        again = input("\nهل تريد تجربة عملية أخرى؟ (نعم/لا): ").strip().lower()
        if again != 'نعم':
            print("شكراً لاستخدامك الآلة الحاسبة الذكية!")
            break


smart_calculator()
