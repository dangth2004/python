def loan(A, r, n):
    X = (A * (1 + r) ** n * r) / ((1 + r) ** n - 1)
    print(f"Vay: {A:,.2f} Đồng")
    print(f"Lãi suất: {r * 100:.2f}%/tháng")
    print(f"Trong: {n:.2f} tháng")
    print(f"Mỗi tháng cần trả:  {X:,.3f} Đồng")
