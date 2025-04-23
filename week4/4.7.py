balance = 0  # Khởi tạo số dư ban đầu

while True:
    transaction = input().strip()

    # Kết thúc khi gặp dòng trống
    if not transaction:
        break

    # Tách loại giao dịch và số tiền
    parts = transaction.split()
    if len(parts) != 2:
        continue

    transaction_type = parts[0].upper()
    amount = parts[1]

    # Kiểm tra số tiền hợp lệ
    if not amount.isdigit():
        continue

    amount = int(amount)

    # Xử lý giao dịch
    if transaction_type == 'D':
        balance += amount
    elif transaction_type == 'W':
        balance -= amount

# In số dư cuối cùng
print(f"{balance}")
