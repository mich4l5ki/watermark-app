import tkinter as tk
from tkinter import ttk

class AppWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.top_frame = ttk.Frame(self.window)
        self.left_frame = ttk.Frame(self.window)
        self.right_frame = ttk.Frame(self.window)
        self.button_upload_image = ttk.Button(self.left_frame, text="UPLOAD IMAGE")
        self.welcome_label = ttk.Label(self.top_frame,
                                      text="Welcome to WaterMarkIt")
        self.watermark_input_label = ttk.Label(self.right_frame,
                                      text="Insert watermark text: (max. 12 characters)")
        self.watermark_input = ttk.Entry(self.right_frame, width=13)
        self.button_create_watermark = ttk.Button(self.right_frame, text="CREATE WATERMARK")


    def create_window(self):
        self.window.title("WaterMarkIt")
        self.window.geometry("700x250+300+300")
        self.window.resizable(0, 0)

        # Top frame
        self.top_frame.place(relx=0, y=0, relheight=0.1, relwidth=1)
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.rowconfigure(0, weight=1)
        self.welcome_label.grid(row=0, column=0, rowspan=6, padx=5, pady=3)

        # Left frame
        self.left_frame.place(x=0, rely=0.1, relwidth=0.5, relheight=0.9)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, weight=1)
        self.button_upload_image.grid(row=0, column=0)

        # Right frame
        self.right_frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)
        self.right_frame.columnconfigure(0, weight=1)
        self.right_frame.rowconfigure((0, 1, 2), weight=1)
        self.watermark_input_label.grid(row=0, column=0, padx=5, pady=0, sticky='s')
        self.watermark_input.grid(row=1, column=0, sticky='n')
        self.button_create_watermark.grid(row=2, column=0, sticky='n')


    def upload_image(self):
        self.welcome_label.configure(text = "Harder Daddy")


    def create_upload_button(self):
        pass

    def create_watermark_text_entry(self):
        pass

while __name__ == '__main__':
    app_window = AppWindow()
    app_window.create_window()
    app_window.window.mainloop()