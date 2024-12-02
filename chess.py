import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance
root = tk.Tk()
root.title("Fotoğraf Yükleme ve Düzenleme")
root.geometry("600x800")

file_path = filedialog.askopenfilename()
if file_path:
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)

    root.image = image  # Orijinal resmi saklayın


    #image_label.config(image=photo)
    #image_label.image = photo
    #root.image = image  # Orijinal resmi saklayın
def enhance_image():
    if hasattr(root, 'image'):
        enhancer = ImageEnhance.Brightness(root.image)
        enhanced_image = enhancer.enhance(1.5)  # Parlaklığı artırma örneği
        photo = ImageTk.PhotoImage(enhanced_image)
        image_label.config(image=photo)
        image_label.image = photo
load_button = tk.Button(root, text="Fotoğraf Yükle")
load_button.pack()

enhance_button = tk.Button(root, text="Parlaklığı Artır", command=enhance_image)
enhance_button.pack()

image_label = tk.Label(root)
image_label.pack()
image.show()
root.mainloop()
