import tkinter as tk
from tkinter import Button, Label, filedialog
from tkinter import font
from tkinter.constants import BOTTOM
from PIL import ImageTk, Image
import numpy

from keras.models import load_model
model = load_model('sentiment.h5')

classes = {
    0: 'Airplane',
    1: 'Automobile',
    2: 'Bird',
    3: 'Cat',
    4: 'Deer',
    5: 'Dog',
    6: 'Frog',
    7: 'Horse',
    8: 'Ship',
    9: 'Truck'
}


def upload_Image():
    file_path = filedialog.askopenfilename()
    uploaded = Image.open(file_path)
    uploaded.thumbnail((((top.winfo_width()/2.25).top.winfo_height()/2.25)))
    im = ImageTk.PhotoImage(uploaded)
    sign_image.configure(image=im)
    sign_image.image = im
    label.configure(text=' ')
    show_classify_button(file_path)


def show_classify_button(file_path):
    classify_btn = Button(top, text="Classify Image", command=lambda:
                          classify(file_path), padx=10, pady=5)
    classify_btn.configure(background="#364156",
                           foreground='white', font=("ariel", 10, 'bold'))
    classify_btn.place(relx=0.79, rely=0.46)


def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((32, 32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)
    label.configure(foreground='#o11638', text=sign)


# initialize GUI
top = tk.TK()
top.geometry('800*600')
top.title("Image Classifier")
top.configure(background="#CDCDCD")

# heading

heading = Label(top, text="image classification",
                pady=20, font=('ariel', 20, 'bold'))
heading.configure(background="#CDCDCD", foreground='#364156')
heading.pack()

upload = Button(top, text="upload image", command="", padx=10, pady=5)
upload.configure(background="#364156", foreground='white',
                 font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)

sign_image = Label(top)
sign_image.pack(side=BOTTOM, expand=True)

label = Label(top, background="#364156", font=('ariel', 13, 'bold'))
label.pack(side=Button, expand=True)

top.mainloop()
