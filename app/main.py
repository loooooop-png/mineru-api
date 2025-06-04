from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
import os
import shutil
import subprocess

app = FastAPI()

UPLOAD_DIR = "/data/pdf"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/mineru/")
async def mineru(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return JSONResponse(status_code=400, content={"message": "只允许上传PDF文件"})
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # 调用magic-pdf命令
    try:
        # 使用conda run在mineru环境中执行magic-pdf
        result = subprocess.run([
            "conda", "run", "-n", "mineru", "magic-pdf", "-p", file_path, "-o", "./output"
        ], capture_output=True, text=True, check=True)
        message = "上传并处理成功"
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"message": f"PDF处理失败: {e.stderr}"})
    download_url = f"/download_pdf/{file.filename}"
    return {"filename": file.filename, "message": message, "download_url": download_url}

@app.get("/mineru_download/{foldername}")
def mineru_download(foldername: str):
    folder_path = os.path.join("./output", foldername)
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return JSONResponse(status_code=404, content={"message": "文件夹未找到"})
    zip_path = f"{folder_path}.zip"
    shutil.make_archive(folder_path, 'zip', folder_path)
    if not os.path.exists(zip_path):
        return JSONResponse(status_code=500, content={"message": "压缩失败"})
    return FileResponse(zip_path, media_type="application/zip", filename=f"{foldername}.zip")
