import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm
import numpy as np

# โหลดฟอนต์ภาษาไทย
font_path = './Sarabun-Medium.ttf'   # ชี้ path ไปยังไฟล์ฟอนต์ไทย
font_prop = fm.FontProperties(fname=font_path)

# ข้อมูลจากตาราง
Vs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Iz = [0, 0, 0, 4e-8, 4e-8, 6.9e-2, 1, 2, 2, 3, 4]  # mA
Vz = [0, 1, 2, 3, 4, 4.76, 4.97, 5.03, 5.05, 5.06, 5.07]  # V

fig, ax1 = plt.subplots()

# --- กราฟ Iz ---
color = 'tab:red'
ax1.set_xlabel('แรงดันไฟฟ้า Vs (V)', fontproperties=font_prop)
ax1.set_ylabel('กระแส Iz (mA)', color=color, fontproperties=font_prop)
ax1.plot(Vs, Iz, 'o-', color=color, label='Iz (mA)')
ax1.tick_params(axis='y', labelcolor=color)

# ทำแกน y ซ้ายให้เป็น log scale
ax1.set_yscale("log")
ax1.set_ylim(1e-8, 1e1)

# ฟังก์ชัน formatter แกน y (เลขยกกำลังแบบ LaTeX)
def latex_sci_formatter(x_val, pos):
    if x_val == 0:
        return r"$0$"
    exponent = int(np.floor(np.log10(abs(x_val))))
    base = x_val / 10**exponent
    return r"${:.2f} \times 10^{{{}}}$".format(base, exponent)

ax1.yaxis.set_major_formatter(ticker.FuncFormatter(latex_sci_formatter))
ax1.yaxis.set_minor_formatter(ticker.NullFormatter())

# --- กราฟ Vz ---
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('แรงดัน Vz (V)', color=color, fontproperties=font_prop)
ax2.plot(Vs, Vz, 's--', color=color, label='Vz (V)')
ax2.tick_params(axis='y', labelcolor=color)

# ชื่อกราฟ
plt.title('ความสัมพันธ์ระหว่าง Vs, Iz และ Vz ของไดโอดซีเนอร์ 1N4733A',
          fontproperties=font_prop)

# Grid
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()
