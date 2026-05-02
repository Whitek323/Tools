import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.font_manager as fm
import numpy as np

# โหลดฟอนต์ภาษาไทย
font_path = './Sarabun-Medium.ttf'
font_prop = fm.FontProperties(fname=font_path)

# ข้อมูลจริง
y = [4e-5, 6.1e-4, 6.27e-3, 5.47e-2, 3.93e-1, 6]
x = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

fig, ax = plt.subplots()
ax.plot(x, y, marker='o')

# log scale
ax.set_yscale("log")
ax.set_ylim(1e-5, 1e1)

# Format label แกน Y เป็น latex
def latex_sci_formatter(x_val, pos):
    if x_val == 0:
        return r"$0$"
    exponent = int(np.floor(np.log10(abs(x_val))))
    base = x_val / 10**exponent
    return r"${:.2f} \times 10^{{{}}}$".format(base, exponent)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(latex_sci_formatter))
ax.yaxis.set_minor_formatter(ticker.NullFormatter())

# แสดงค่าตัวเลขบนจุด
for xi, yi in zip(x, y):
    exponent = int(np.floor(np.log10(abs(yi))))
    base = yi / 10**exponent
    latex_label = r"${:.2f} \times 10^{{{}}}$".format(base, exponent)
    ax.text(xi, yi, latex_label,
            ha='left',
            va='bottom',
            rotation=0,
            bbox=dict(boxstyle="round,pad=0.2", edgecolor="blue", facecolor="white", alpha=0.6))

# ชื่อกราฟ
ax.set_title('กราฟความสัมพันธ์ระหว่างกระแสไฟฟ้าและแรงดันไฟฟ้าของไดโอด', fontproperties=font_prop)
ax.set_xlabel('แรงดันไฟฟ้าของไดโอด (Vd)', fontproperties=font_prop)
ax.set_ylabel('กระแส (mA)', fontproperties=font_prop)

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
