import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image, ImageTk

def select_input_file():
    input_path = filedialog.askopenfilename(title="Select Input Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    input_label.config(text=input_path)
    global input_image
    input_image = Image.open(input_path)
    input_photo = ImageTk.PhotoImage(input_image)
    input_canvas.create_image(0, 0, anchor=tk.NW, image=input_photo)
    input_canvas.image = input_photo

def save_output_file():
    output_path = filedialog.asksaveasfilename(title="Save Output Image", defaultextension=".png", filetypes=[("PNG files", "*.png")])
    output_label.config(text=output_path)
    output_image.save(output_path)
    print("Image saved!")

def remove_background():
    global output_image
    output_image = remove(input_image)
    output_photo = ImageTk.PhotoImage(output_image)
    output_canvas.create_image(0, 0, anchor=tk.NW, image=output_photo)
    output_canvas.image = output_photo

# Create the main window
root = tk.Tk()
root.title("Background Remover")

# Create frames for input and output images
input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT, padx=10, pady=10)

output_frame = tk.Frame(root)
output_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create labels to display file paths
input_label = tk.Label(input_frame, text="No input file selected")
input_label.pack()

output_label = tk.Label(output_frame, text="No output file selected")
output_label.pack()

# Create canvas to display images
input_canvas = tk.Canvas(input_frame, width=300, height=300)
input_canvas.pack()

output_canvas = tk.Canvas(output_frame, width=300, height=300)
output_canvas.pack()

# Create buttons
select_input_button = tk.Button(input_frame, text="Select Input Image", command=select_input_file)
select_input_button.pack(pady=5)

remove_bg_button = tk.Button(input_frame, text="Remove Background", command=remove_background)
remove_bg_button.pack(pady=5)

save_output_button = tk.Button(output_frame, text="Save Output Image", command=save_output_file)
save_output_button.pack(pady=5)

# Run the application
root.mainloop()
