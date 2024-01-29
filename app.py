from flask import Flask, render_template, send_file
import os
import re

app = Flask(__name__)

# Replace 'path/to/mangas' with the actual base directory for your mangas folder
base_directory = "E:/Mangas(webp)"

def extract_numbers(chapter_name):
    # Extract numeric parts from the chapter name
    numeric_parts = re.findall(r'\d+', chapter_name)
    # Convert numeric parts to integers and return as tuple
    return tuple(map(int, numeric_parts))

def sort_chapters(chapters):
    return sorted(chapters, key=extract_numbers)

@app.route('/')
def index():
    mangas_list = os.listdir(base_directory)
    return render_template('index.html', mangas=mangas_list)

@app.route('/<manga_name>/')
def manga(manga_name):
    manga_path = os.path.join(base_directory, manga_name)
    chapters_list = sort_chapters(os.listdir(manga_path))
    return render_template('manga.html', manga_name=manga_name, chapters=chapters_list)

@app.route('/<manga_name>/<chapter_name>/')
def chapter(manga_name, chapter_name):
    chapter_path = os.path.join(base_directory, manga_name, chapter_name)
    pages_list = os.listdir(chapter_path)
    return render_template('chapter.html', manga_name=manga_name, chapter_name=chapter_name, pages=pages_list)

@app.route('/<manga_name>/<chapter_name>/<page_name>')
def page(manga_name, chapter_name, page_name):
    page_path = os.path.join(base_directory, manga_name, chapter_name, page_name)
    return send_file(page_path)

if __name__ == '__main__':
    app.run(host='192.168.0.30', port=5000, debug=False)
