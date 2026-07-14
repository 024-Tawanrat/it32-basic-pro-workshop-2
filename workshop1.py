quantity = int(input("รับมากี่กระบอก"))
cost_price = float(input("ต้นทุนกระบอกละ"))
sell_price = float(input("ราคาที่จะนำไปขายต่อ"))
team_member = int(input("จำนวนลูกน้อง"))

total = quantity*cost_price
cost = quantity*sell_price
profit = cost-total
boss = (20/100) * profit
member = (profit - boss)/team_member

print(f"ต้นทุนทั้งหมด {total}")
print(f"รายรับทั้งหมด{cost}")
print(f"กำไรสุทธิ{profit}")
print(f"หักให้บอส{boss}")
print(f"จำนวนที่ได้{member}")
