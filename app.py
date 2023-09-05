from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Get a list of all subdirectories (folders) in E:/Mangas/mergeFlies
    base_directory = "E:/Mangas/mergeFlies"
    folders = [folder for folder in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, folder))]
    
    return render_template('index.html', folders=folders)

@app.route('/images/<folder>/<image>')
def get_image(folder, image):
    directory = os.path.join("E:/Mangas/mergeFlies", folder)
    return send_from_directory(directory, image)

@app.route('/images/<folder>')
def list_images_in_folder(folder):
    directory = os.path.join("E:/Mangas/mergeFlies", folder)
    images = [image for image in os.listdir(directory) if os.path.isfile(os.path.join(directory, image))]
    
    return render_template('image_folder.html', folder=folder, images=images)

if __name__ == '__main__':
    app.run(host='192.168.0.30', port=5000, debug=False)
