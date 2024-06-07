from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/micro_servico")
async def root():
    subprocess.run(["python", "contar_palavras.ipynb"])
    return {"message": "rodou o microserviço com sucesso!"}



@app.get("/teste/{id}")
async def teste(id: int):
    return { "message": f'{id}' }