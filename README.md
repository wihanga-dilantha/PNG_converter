# Background Remover App
This is a simple Python application built with Tkinter that allows you to select an input image, remove its background using rembg, and save the output image.

## Features
  
  Select an input image file (supports JPG, JPEG, and PNG formats).
  Remove the background from the selected image.
  Save the processed image with the background removed.

## Installation

  To run this application locally, follow these steps:

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/background-remover.git
```
```bash
cd background-remover
```

**2. Install dependencies:**

*Make sure you have Python installed. This project requires _Python 3.6_ or higher.*



**3. Install the required Python packages:**

```bash
pip install rembg Pillow
```

**4. Run the application:**

```bash
python background_remover.py
```
## Usage

**1. Select Input Image:**

  Click on the "Select Input Image" button to choose an image file from your computer.
  Supported formats: JPG, JPEG, PNG.

**2. Remove Background:**

  After selecting an image, click on the "Remove Background" button to process the image and display the result in the output canvas.

**3. Save Output Image:**

  Once the background is removed and you're satisfied with the result, click on the "Save Output Image" button to save the processed image with the background removed.

# License

This project is licensed under the [MIT License](LICENSE.txt). See the LICENSE.txt file for details.
