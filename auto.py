import time

# تحديد اسم الملف
file_name = "log.txt"

# الحصول على الوقت الحالي بصيغة (سنة-شهر-يوم ساعة:دقيقة:ثانية)
current_time = time.strftime("%Y-%m-%d %H:%M:%S")

# فتح الملف وإضافة اسم yousifù مع الوقت
with open(file_name, "a") as file:
    file.write(f"yousif - {current_time}\n")

print(f"تم إضافة السطر بنجاح: yousif - {current_time}")
