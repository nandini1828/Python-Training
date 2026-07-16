import json
import csv
import os


UPLOAD_FOLDER = "uploads"


def create_folder():

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)


def save_json(filename, data):

    create_folder()

    path = os.path.join(UPLOAD_FOLDER, filename)

    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def read_json(filename):

    path = os.path.join(UPLOAD_FOLDER, filename)

    with open(path, "r") as file:
        return json.load(file)


def save_text(filename, content):

    create_folder()

    path = os.path.join(UPLOAD_FOLDER, filename)

    with open(path, "w") as file:
        file.write(content)


def read_text(filename):

    path = os.path.join(UPLOAD_FOLDER, filename)

    with open(path, "r") as file:
        return file.read()


def save_csv(filename, rows):

    create_folder()

    path = os.path.join(UPLOAD_FOLDER, filename)

    with open(path, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)