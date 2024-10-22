from fastapi import FastAPI

app = FastAPI()

@app.get("/menu")
def read_menu():
    return {
        "cachetada": ["fuerte", "media", "suave"],
        "truchas": ["trucha roja", "trucha de goma", "trucha de fibra de carbobno"]
    }