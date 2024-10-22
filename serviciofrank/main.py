from fastapi import FastAPI

app = FastAPI()

@app.get("/hotel")
def read_hotel():
    return {
        "ubicacion": ["222222222", "aaaaaaaaaaa", "Pfffffffff"],
        "datos": ["juan chichon", "manu lindo", "sebas el puyo"]
    }
