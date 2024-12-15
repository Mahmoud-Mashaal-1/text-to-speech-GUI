import tkinter as tk
from tkinter import messagebox
import pyttsx3

# إعداد محرك تحويل النص إلى كلام
engine = pyttsx3.init()

# ضبط السرعة الافتراضية للصوت
default_rate = 150
engine.setProperty('rate', default_rate)

# إعداد الصوت الافتراضي
voices = engine.getProperty('voices')
default_voice = voices[0].id
engine.setProperty('voice', default_voice)

# تبديل الوضع بين المضيء والمظلم
is_dark_mode = False

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    if is_dark_mode:
        root.configure(bg="black")
        label.configure(bg="gray20", fg="white")
        text_entry.configure(bg="gray", fg="white", insertbackground="white")
        rate_label.configure(bg="black", fg="white")
        voice_button.configure(bg="purple", fg="white")
        play_button.configure(bg="green", fg="white")
        set_button.configure(bg="blue", fg="white")
        exit_button.configure(bg="red", fg="white")
        theme_button.configure(text="Light Mode", bg="gray10", fg="white")
    else:
        root.configure(bg="white")
        label.configure(bg="white", fg="black")
        text_entry.configure(bg="white", fg="black", insertbackground="black")
        rate_label.configure(bg="white", fg="black")
        voice_button.configure(bg="purple", fg="black")
        play_button.configure(bg="green", fg="black")
        set_button.configure(bg="blue", fg="black")
        exit_button.configure(bg="red", fg="black")
        theme_button.configure(text="Dark Mode", bg="white", fg="black")

def play_text():
    text = text_entry.get()
    if text.strip():
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("تحذير", "الرجاء إدخال نص لتشغيله!")

def set_text():
    text_entry.delete(0, tk.END)

def exit_app():
    root.destroy()

def change_rate(rate):
    engine.setProperty('rate', int(rate))

def change_voice():
    current_voice = engine.getProperty('voice')
    new_voice = voices[1].id if current_voice == voices[0].id else voices[0].id
    engine.setProperty('voice', new_voice)
    messagebox.showinfo("تغيير الصوت", "تم تغيير الصوت!")

# إعداد نافذة التطبيق
root = tk.Tk()
root.title("Text to Speech")
root.configure(bg="white")

# مكونات الواجهة
label = tk.Label(root, text="Enter text:", font=("Arial", 14), bg="white", fg="black")
label.pack(pady=10)

text_entry = tk.Entry(root, font=("Arial", 14), width=30, bg="white", fg="black", insertbackground="black")
text_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

play_button = tk.Button(button_frame, text="Play", font=("Arial", 12), bg="green", command=play_text)
play_button.grid(row=0, column=0, padx=10)

set_button = tk.Button(button_frame, text="Set", font=("Arial", 12), bg="blue", command=set_text)
set_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="Exit", font=("Arial", 12), bg="red", command=exit_app)
exit_button.grid(row=0, column=2, padx=10)

# إضافة شريط التحكم في السرعة
rate_label = tk.Label(root, text="Speed:", font=("Arial", 12), bg="white", fg="black")
rate_label.pack(pady=5)

rate_slider = tk.Scale(root, from_=50, to=300, orient="horizontal", command=change_rate, bg="white", fg="black")
rate_slider.set(default_rate)
rate_slider.pack(pady=5)

# زر تغيير الصوت
voice_button = tk.Button(root, text="Change Voice", font=("Arial", 12), bg="purple", command=change_voice)
voice_button.pack(pady=10)

# زر التبديل بين الوضعين
theme_button = tk.Button(root, text="Dark Mode", font=("Arial", 12), bg="white", fg="black", command=toggle_theme)
theme_button.pack(pady=10)

# تشغيل التطبيق
root.mainloop()
