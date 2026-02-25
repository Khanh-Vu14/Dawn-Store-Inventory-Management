from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Xin chào! Hệ thống đã kết nối thành công!"}
