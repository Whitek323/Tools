from PIL import Image
import os

def convert_image(input_path, output_format):
    img = Image.open(input_path)

    # ตัดนามสกุลไฟล์เดิม
    filename = os.path.splitext(input_path)[0]
    output_path = f"{filename}.{output_format.lower()}"

    # แปลงโหมดสีให้เหมาะกับ JPG
    if output_format.lower() in ["jpg", "jpeg"]:
        img = img.convert("RGB")

    # กรณี ICO (ต้องกำหนดขนาด)
    if output_format.lower() == "ico":
        img.save(output_path, format="ICO", sizes=[(256, 256)])
    else:
        img.save(output_path, format=output_format.upper())

    print(f"แปลงไฟล์สำเร็จ ➜ {output_path}")

if __name__ == "__main__":
    input_path = input("ใส่ path รูปภาพต้นทาง: ")
    print("เลือกฟอร์แมตปลายทาง: png / jpg / webp / ico")
    output_format = input("ฟอร์แมตที่ต้องการ: ")

    convert_image(input_path, output_format)

