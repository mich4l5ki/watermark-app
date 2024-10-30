import tkinter as tk

class AppWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.top_frame = tk.Frame(self.window)
        self.left_frame = tk.Frame(self.window)
        self.right_frame = tk.Frame(self.window)
        self.button_upload_image = tk.Button(self.left_frame, text="UPLOAD IMAGE")
        self.welcome_label = tk.Label(self.top_frame,
                                      text="Welcome to WaterMarkIt")
        self.watermark_input_label = tk.Label(self.right_frame,
                                      text="Insert watermark text: (max. 12 characters)")
        self.watermark_input = tk.Entry(self.right_frame, width=13)
        self.button_create_watermark = tk.Button(self.right_frame, text="CREATE WATERMARK")


    def create_window(self):
        self.window.title("WaterMarkIt")
        self.window.geometry("700x500+300+300")
        self.window.resizable(0, 0)
        self.left_frame.place(x=0, rely=0.1, relwidth=0.5, relheight=0.9)
        self.right_frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)
        self.top_frame.place(relx=0, y=0, relheight=0.1, relwidth=1)
        self.right_frame.columnconfigure(0, weight=1)
        self.right_frame.rowconfigure((0,1,2), weight=1)
        self.button_upload_image.grid(row=0, column=0)


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