import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# ตั้งค่าฟอนต์ภาษาไทย (ต้องมีไฟล์ Sarabun-Medium.ttf อยู่ในโฟลเดอร์เดียวกัน)
font_path = './Sarabun-Medium.ttf'
font_prop = fm.FontProperties(fname=font_path)

# ข้อมูลเครื่องจักรทั้ง 7 ชนิด (เปลี่ยนเป็นภาษาไทย)
machines = ['1. เครื่องรีดแป้ง', '2. แขนกล', '3. เครื่องห่อเกี๊ยว', '4. สายพาน 5 เมตร', 
            '5. เครื่องหั่นผัก', '6. เครื่องหั่นหมู', '7. เครื่องผสม']
p1 = 10950
p2 = 34650
p3 = 293673
p4 = 261800
p5 = 23760
p6 = 11583
p7 = 56430

prices = [p1, p2, p3, p4, p5, p6, p7]
lifespans = [8, 3, 7, 10, 5, 5, 8]
maintenances = [p1*0.05, p2*0.05, p3*0.05, p4*0.05, p5*0.05, p6*0.05, p7*0.05]
scraps = [p1/10, p2/10, p3/10, p4/10, p5/10, p6/10, p7/10]

# ตั้งค่า Figure สำหรับ 3D
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(projection='3d')

colors = ['#FF6666', '#FFCC66', '#99FF99', '#66B2FF', '#C299FF', '#FF99CC', '#99FFFF']
yticks = np.arange(len(machines))
years = 20
xs = np.arange(1, years + 1) 

for i, k in enumerate(yticks):
    p = prices[i]
    l = lifespans[i]
    m = maintenances[i]
    s = scraps[i]
    
    ys = [] # เก็บค่าแกน Z (รายจ่ายเฉพาะปีนั้นๆ)
    
    for x in xs:
        if x == 1:
            # ปีที่ 1: ซื้อเครื่องจักรใหม่ราคาเต็ม
            expense = p
        elif (x - 1) % l == 0:
            # ปีที่หมดอายุ: ซื้อเครื่องใหม่ - ขายซาก + ค่าซ่อม
            expense = (p - s) + m
        else:
            # ปีปกติทั่วไป: จ่ายแค่ค่าซ่อมบำรุง
            expense = m
            
        ys.append(expense) # ไม่นำไปบวกทบกับปีก่อนหน้าแล้ว
    
    ax.bar(xs, ys, zs=k, zdir='y', color=colors[i], alpha=0.8, edgecolor='black', width=0.6)

# ปรับแต่งกราฟ (ใส่ fontproperties=font_prop เพื่อให้แสดงภาษาไทยได้)
ax.set_xlabel('\nเวลา (ปี)', fontproperties=font_prop, fontsize=12)
# ax.set_ylabel('\nเครื่องจักร', fontproperties=font_prop, fontsize=12)
ax.set_zlabel('\nรายจ่ายต่อปี (บาท)', fontproperties=font_prop, fontsize=12)

ax.set_yticks(yticks)
ax.set_yticklabels(machines, fontproperties=font_prop, fontsize=10)
ax.set_xticks(np.arange(1, 21, 1))
ax.set_title('กราฟแท่ง 3 มิติ: กระแสเงินสดจ่ายรายปี (ไม่สะสม)', fontproperties=font_prop, fontsize=16, pad=20)

ax.view_init(elev=25, azim=-45)

plt.tight_layout()
plt.show()