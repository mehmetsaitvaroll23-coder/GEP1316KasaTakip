transactions = []


def get_valid_amount():
    while True:
        try:
            amount = float(input("Tutar giriniz: ").replace(",", "."))

            if amount > 0:
                return amount
            else:
                print("Tutar sıfırdan büyük olmalıdır.")

        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


def add_transaction(transaction_type):
    category = input("Kategori giriniz: ").strip()
    description = input("Açıklama giriniz: ").strip()

    if category == "" or description == "":
        print("Kategori ve açıklama boş bırakılamaz.")
        return

    amount = get_valid_amount()

    transaction = {
        "type": transaction_type,
        "category": category,
        "description": description,
        "amount": amount
    }

    transactions.append(transaction)
    print("İşlem başarıyla kaydedildi.")


def calculate_totals():
    total_income = 0
    total_expense = 0

    for transaction in transactions:
        if transaction["type"] == "Gelir":
            total_income += transaction["amount"]
        else:
            total_expense += transaction["amount"]

    balance = total_income - total_expense

    return total_income, total_expense, balance


def show_report():
    income, expense, balance = calculate_totals()

    print("\n----- KASA RAPORU -----")
    print(f"Toplam Gelir: {income:.2f} TL")
    print(f"Toplam Gider: {expense:.2f} TL")
    print(f"Güncel Bakiye: {balance:.2f} TL")

    if balance > 0:
        print("Durum: Kasa pozitif.")
    elif balance < 0:
        print("Durum: Kasa negatif.")
    else:
        print("Durum: Gelir ve gider eşit.")

    print("\nİşlem Geçmişi:")

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index}. {transaction['type']} - "
            f"{transaction['category']} - "
            f"{transaction['description']} - "
            f"{transaction['amount']:.2f} TL"
        )


def save_report():
    income, expense, balance = calculate_totals()

    try:
        with open("kasa_raporu.txt", "w", encoding="utf-8") as file:
            file.write("KASA RAPORU\n")
            file.write("--------------------\n")
            file.write(f"Toplam Gelir: {income:.2f} TL\n")
            file.write(f"Toplam Gider: {expense:.2f} TL\n")
            file.write(f"Güncel Bakiye: {balance:.2f} TL\n\n")

            for transaction in transactions:
                file.write(
                    f"{transaction['type']} - "
                    f"{transaction['category']} - "
                    f"{transaction['description']} - "
                    f"{transaction['amount']:.2f} TL\n"
                )

        print("Rapor kasa_raporu.txt dosyasına kaydedildi.")

    except OSError:
        print("Rapor kaydedilirken bir hata oluştu.")


def main():
    while True:
        print("\n===== KASA TAKİP SİSTEMİ =====")
        print("1 - Gelir Ekle")
        print("2 - Gider Ekle")
        print("3 - Kasa Raporunu Göster")
        print("4 - Raporu Dosyaya Kaydet")
        print("5 - Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            add_transaction("Gelir")
        elif choice == "2":
            add_transaction("Gider")
        elif choice == "3":
            show_report()
        elif choice == "4":
            save_report()
        elif choice == "5":
            save_report()
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim! 1 ile 5 arasında bir değer giriniz.")


if __name__ == "__main__":
    main()
