from minio import Minio
from minio.error import S3Error

MINIO_ENDPOINT = "http://localhost:9005"
MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "password"
BUCKET_NAME = "photos"

FILE_PATH = "cat.png"
OBJECT_NAME = "uploads/cat.png"

# Create MinIO client
client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

if not client.bucket_exists(BUCKET_NAME):
    client.make_bucket(BUCKET_NAME)

client.fput_object(
        bucket_name=BUCKET_NAME,
        object_name=OBJECT_NAME,
        file_path=FILE_PATH,
        content_type="image/jpeg"
    )

print(f"File '{FILE_PATH}' successfully uploaded as '{OBJECT_NAME}'")

url = client.presigned_get_object(BUCKET_NAME, OBJECT_NAME)
print("Link to the file", url)


if __name__ == "__main__":
    pass
