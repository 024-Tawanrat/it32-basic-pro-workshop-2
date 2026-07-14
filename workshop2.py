name = input("ชื่อ: ")
age = int(input("อายุ: "))
height = float(input("ส่วนสูง: "))
power = int(input("พละกำลัง: "))
money = int(input("เงินติดตัว: "))

if (power>=1) and (power<=10) :
    if age>=20:
        if (power>5) and (height>=160):
            if power>8:
                if (money >= 10000):
                    print("ผ่าน!!! ตำแหน่ง:ผู้บัญชาการ")
                else:
                    print("ผ่าน!!! ตำแหน่ง:รองผู้บัญชาการ")
            else:
                print("ผ่าน!!! ตำแหน่ง:จัดหาอาวุธ")
        elif height>=999:
            print("ผ่าน!!! ตำแหน่ง:ผู้สังเกตการ")
        elif money>=100000:
            print("ผ่าน!!! ตำแหน่ง:ผู้สนับสนุนทางการเงิน")
        else:
            print("ไม่ผ่าน:(")
    else:
        print("ไม่ผ่าน:(")
else:
    print("พละกำลัง 1-10 เท่านั้น")