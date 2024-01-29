print(f"ROI for the rental property is: {(lambda purchase_price, monthly_rent, annual_expenses: (lambda annual_income, annual_net_income, roi: roi)(
    monthly_rent * 12,
    monthly_rent * 12 - annual_expenses,
    (monthly_rent * 12 - annual_expenses) / purchase_price * 100
))(150000, 1200, 6000):.2f}%")




