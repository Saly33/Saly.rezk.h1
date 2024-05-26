def main():
    while True:
        binary_num = input("أدخل رقماً ثنائياً: ")
        try:
            decimal_num = int(binary_num, 2)
            print(f"الرقم العشري المكافئ هو: {decimal_num}")
            break  
        except ValueError:
            print("الرجاء إدخال رقم ثنائي صحيح.")
main()

