import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from image_processing import ImageLoader

class WaterMarkItApp:
    def __init__(self, root):
        self.image_loader = ImageLoader()
        self.main_image = None
        self.watermark_input = None
        self.image_preview = None

        self.window = root
        self.window.title("WaterMarkIt")
        self.top_frame = ttk.Frame(self.window)
        self.left_frame = ttk.Frame(self.window)
        self.right_frame = ttk.Frame(self.window)
        self.create_widgets()

    def create_widgets(self):
        self.configure_window()
        self.configure_top_frame()
        self.configure_left_frame()
        self.configure_right_frame()
        self.create_welcome_label()
        self.create_image_preview()
        self.create_upload_image_button()
        self.create_watermark_input()
        self.create_watermark_button()

    def configure_window(self):
        self.window.geometry("700x250+300+300")
        self.window.resizable(0, 0)


    def configure_top_frame(self):
        self.top_frame.place(relx=0, y=0, relheight=0.1, relwidth=1)
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.rowconfigure(0, weight=1)


    def configure_left_frame(self):
        self.left_frame.place(x=0, rely=0.1, relwidth=0.5, relheight=0.9)
        self.left_frame.columnconfigure(0, weight=1)
        self.left_frame.rowconfigure(0, weight=1)


    def configure_right_frame(self):
        self.right_frame.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)
        self.right_frame.columnconfigure(0, weight=1)
        self.right_frame.rowconfigure((0, 1, 2), weight=1)


    def create_upload_image_button(self):
        button_upload_image = ttk.Button(self.left_frame, text="UPLOAD IMAGE", command=self.command_load_image)
        button_upload_image.grid(row=0, column=0)


    def create_welcome_label(self):
        welcome_label = ttk.Label(self.top_frame, text="Welcome to WaterMarkIt")
        welcome_label.grid(row=0, column=0, rowspan=6, padx=5, pady=3)


    def create_watermark_input(self):
        watermark_input_label = ttk.Label(self.right_frame, text="Insert watermark text:")
        self.watermark_input = ttk.Entry(self.right_frame)
        watermark_input_label.grid(row=0, column=0, padx=5, pady=0, sticky='s')
        self.watermark_input.grid(row=1, column=0, sticky='n')

    def create_watermark_button(self):
        button_create_watermark = ttk.Button(self.right_frame, text="CREATE WATERMARK",
                                             command=self.command_add_watermark)
        button_create_watermark.grid(row=2, column=0, sticky='n')

    def create_download_button(self):
        ttk.Style().configure('Download.TButton',
                        foreground = 'green')
        button_downlaod = ttk.Button(self.right_frame, text="DOWNLOAD",
                                     command=self.download_image, style='Download.TButton')
        button_downlaod.grid(row=3, column=0, sticky='n', pady=(0,20))

    def create_image_preview(self):
        self.image_preview = tk.Label(self.left_frame)
        self.image_preview.grid(row=1, column=0)

    def command_load_image(self):
        filepath = filedialog.askopenfilename(
            filetypes=(
                ("Image files", ("*.jpeg", "*.jpg", "*.png")),
            )
        )
        if filepath:
            image = self.image_loader.load_image(filename=filepath)
            self.show_image(image)

    def command_add_watermark(self):
        watermark_text = self.watermark_input.get()
        if self.validate_watermark(watermark_text):
            watermarked_image = self.image_loader.add_watermark(watermark_text)
            if not watermarked_image:
                messagebox.showerror("Error", "No Image Loaded")
            else:
                self.show_image(watermarked_image)
                self.create_download_button()

    def show_image(self, image):
        max_img_display_height = 180
        max_img_display_width = 300

        img_width, img_height = image.size
        scaling_factor = min(max_img_display_width/img_width, max_img_display_height/img_height)
        display_image = image.resize((int(img_width*scaling_factor), int(img_height*scaling_factor)),
                                     Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(display_image, size=image.size)
        self.image_preview.configure(image=tk_image)
        self.image_preview.image = tk_image

    def validate_watermark(self, text):
        if not text:
            messagebox.showerror("Input error", "Input error: Please insert Watermark.")
            return False
        if not text.replace(' ','').isalpha():
            messagebox.showerror("Input error", "Input error: Only letters acceptable for watermark.")
            return False
        return True

    def download_image(self):
        filename =  filedialog.asksaveasfilename(initialdir = "/", title = "Select file",
                                                 filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        try:
            self.image_loader.watermarked_image.save(filename)
            messagebox.showinfo("Success", "Success: Image with watermark correctly downloaded")
        except Exception:
            messagebox.showinfo("Error", "Something went wrong.")