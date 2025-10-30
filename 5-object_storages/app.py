from flask import Flask, render_template, request
from minio import Minio
from minio.error import S3Error
import os

app = Flask(__name__)

MINIO_ENDPOINT = "localhost:9005"
MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "password"
BUCKET_NAME = "photos"


client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

if not client.bucket_exists(BUCKET_NAME):
    client.make_bucket(BUCKET_NAME)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")

        if file:
            # filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            # file.save(filepath)

            try:

                client.put_object(
                    bucket_name=BUCKET_NAME,
                    object_name=file.filename,
                    data=file.stream,
                    length=-1,
                    part_size=10 * 1024 * 1024, # 10mb
                    content_type=file.content_type
                )

                # client.fput_object(BUCKET_NAME, file.filename, filepath)
                url = client.presigned_get_object(BUCKET_NAME, file.filename)

                return f"Link to the file: {url}"

            except S3Error as e:
                return f"Uploading error: {e}"

            finally:
                pass
                # os.remove(filepath)

    return render_template("upload.html")


@app.route("/images")
def gallery():
    objects = client.list_objects(BUCKET_NAME, recursive=True)
    image_urls = []

    for obj in objects:
        url = client.presigned_get_object(BUCKET_NAME, obj.object_name)
        print(url)
        image_urls.append({
            "name": obj.object_name,
            "url": url
        })

    return render_template("images.html", images=image_urls)


app.run(debug=True, port=5005)

if __name__ == "__main__":
    pass