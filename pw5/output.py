import zipfile
import os

def compress_files():
    with zipfile.ZipFile('students.dat', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write('students.txt')
        zipf.write('courses.txt')
        zipf.write('marks.txt')

def decompress_files():
    if os.path.exists('students.dat'):
        with zipfile.ZipFile('students.dat', 'r') as zipf:
            zipf.extractall()
