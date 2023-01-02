from fastapi import FastAPI,UploadFile
import numpy as np
import io
import cv2
import pytesseract



app = FastAPI()

def read_img(img):
 text = pytesseract.image_to_string(img)
 return(text)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents=await file.read()
    image_stream = io.BytesIO(contents)
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    label =  read_img(frame)

    return {"filename": file.filename,"label":label}

