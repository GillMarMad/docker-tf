from fastapi import FastAPI, UploadFile
import tensorflow as tf

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
