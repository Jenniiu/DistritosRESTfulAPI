from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
import httpx, logging

app = FastAPI(title='DistritosAPI')

URL = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#requisição
async def fetch_distritos():
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        response.raise_for_status()
        return response.json()

@app.get ("/localidades/distritos")
async def get_distritos():
    async with httpx.AsyncClient() as client:
        response = await client.get (URL)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Erro ao buscar dados")

@app.get("/localidades/distritos/id/{id}", tags=["distritos"])
async def get_distrito_by_id(id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        distritos = response.json()
        for distrito in distritos:
            if distrito["id"] == id:
                return distrito
        raise HTTPException(status_code=404, detail="Distrito não encontrado")
    
@app.get("/localidades/distritos/nome/{nome}", tags=["distritos"])
async def get_distrito_by_nome(nome: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        distritos = response.json()
        if distritos:
            distritos_encontrados = [distrito for distrito in distritos if nome.lower() in distrito["nome"].lower()]
            if distritos_encontrados:
                return distritos_encontrados
            else:
                raise HTTPException(status_code=404, detail="Não encontrado")
        else:
            raise HTTPException(status_code=404, detail="Distritos não encontrados")
        
#Paginação
@app.get("/localidades/distritos/paginas", tags=["distritos paginação"])
async def get_localidades_by_distritos(
   offset: int = Query(0, ge=0, description="Numero de distritos a pular"),
   limit: int = Query(10, gt=0, description="Numero de distritos a retornar")
    ):
    
    distritos = await fetch_distritos()
    
    distritos_paginados = distritos[offset:offset + limit]
    
    if distritos_paginados:
        return distritos_paginados
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por município id
@app.get("/localidades/distritos/municipio/{id_municipio}", tags=["municípios"])
async def get_distritos_by_municipio(id_municipio: int):
    distritos = await fetch_distritos()
    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito["municipio"]["id"] == id_municipio]
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por município nome
@app.get("/localidades/distritos/municipio/nome/{nome_municipio}", tags=["municípios"])
async def get_municipios_by_nome(nome_municipio: str):
    distritos = await fetch_distritos()
    distritos_encontrados = [distrito for distrito in distritos if nome_municipio.lower() in distrito["municipio"]["nome"].lower()]
    if distritos_encontrados:
        return distritos_encontrados
    else:
        logger.info(f"Não foi encontrado distrito para o município")
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    
#Filtro: por microrregião id
@app.get("/localidades/distritos/microrregiao/{id_microrregiao}", tags=["microrregiões"])
async def get_distritos_by_microrregiao_id(id_microrregiao: int):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("id") == id_microrregiao]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por microrregião nome
@app.get("/localidades/distritos/microrregiao/nome/{nome_microrregiao}", tags=["microrregiões"])
async def get_distritos_by_microrregiao(nome_microrregiao: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("nome").lower() == nome_microrregiao.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    

#Filtro: por microrregião, mesorregião id    
@app.get("/localidades/distritos/mesorregiao/{id_mesorregiao}", tags=["mesorregiões"])
async def get_distritos_by_mesorregiao_id(id_mesorregiao: int):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("mesorregiao", {}).get("id") == id_mesorregiao]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por microrregião, mesorregião nome
@app.get("/localidades/distritos/mesorregiao/nome/{nome_mesorregiao}", tags=["mesorregiões"])
async def get_distritos_by_mesorregiao(nome_mesorregiao: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("mesorregiao", {}).get("nome").lower() == nome_mesorregiao.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por microrregião, UF id
@app.get("/localidades/distritos/mesorregiao/UF/{id_UF}", tags=["unidades federativas por microrregião"])
async def get_distritos_by_UF_id(id_UF: int):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("mesorregiao", {}).get("UF", {}).get("id") == id_UF]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por microrregião, UF sigla
@app.get("/localidades/distritos//mesorregiao/UF/sigla/{sigla_UF}", tags=["unidades federativas por microrregião"])
async def get_distritos_by_UF_sigla(sigla_UF: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("mesorregiao", {}).get("UF", {}).get("sigla").lower() == sigla_UF.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por microrregião, UF nome
@app.get("/localidades/distritos/mesorregiao/UF/nome/{nome_UF}", tags=["unidades federativas por microrregião"])
async def get_distritos_by_UF(nome_UF: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("mesorregiao", {}).get("UF", {}).get("nome").lower() == nome_UF.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por microrregião, regiões id
@app.get("/localidades/distritos/mesorregiao/regiao/{id_regiao}", tags=["regiões por microrregião"])
async def get_distritos_by_regiao_id(id_regiao: int):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("mesorregiao", {}).get("UF", {}).get("regiao", {}).get("id") == id_regiao]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por microrregião, regiões sigla
@app.get("/localidades/distritos/mesorregiao/regiao/sigla/{sigla_regiao}", tags=["regiões por microrregião"])
async def get_distritos_by_regiao_sigla(sigla_regiao: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("mesorregiao", {}).get("UF", {}).get("regiao", {}).get("sigla").lower() == sigla_regiao.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por microrregião, regiões nome
@app.get("/localidades/distritos/mesorregiao/regiao/nome/{nome_regiao}", tags=["regiões por microrregião"])
async def get_distritos_by_regiao(nome_regiao: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("microrregiao", {}).get("mesorregiao", {}).get("UF", {}).get("regiao", {}).get("nome").lower() == nome_regiao.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    
#Filtro: por região imediata id
@app.get("/localidades/distritos/regiao-imediata/{id_regiaoimediata}", tags=["região imediata"])
async def get_distritos_by_regiao_imediata_id(id_regiaoimediata: int):
    distritos = await fetch_distritos()
    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata", {}).get("id") == id_regiaoimediata]
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por região imediata nome
@app.get("/localidades/distritos/regiao-imediata/nome/{nome_regiao_imediata}", tags=["região imediata"])
async def get_distritos_by_regiao_imediata(nome_regiao_imediata: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata", {}).get("nome").lower() == nome_regiao_imediata.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    
#Filtro: por região imediata, região intermediária id
@app.get("/localidades/distritos/regiao-intermediaria/{id_regiaointermediaria}", tags=["região intermediária"])
async def get_distritos_by_regiao_intermediaria_id(id_regiaointermediaria: int):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata").get("regiao-intermediaria", {}).get("id") == id_regiaointermediaria]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por região imediata, região intermediária nome
@app.get("/localidades/distritos/regiao-intermediaria/nome/{nome_regiaointermediaria}", tags=["região intermediária"])
async def get_distritos_by_regiao_intermediaria(nome_regiaointermediaria: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata").get("regiao-intermediaria", {}).get("nome") == nome_regiaointermediaria]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    
#Filtro: por região imediata, UF id
@app.get("/localidades/distritos/regiao-imediata/UF/{id_UF_RI}", tags=["unidades federativas por região imediata"])
async def get_id_distritos_by_UF_RI(id_UF_RI: int):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata", {}).get("regiao-intermediaria", {}).get("UF", {}).get("id") == id_UF_RI]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    
#Filtro: por região imediata, UF sigla
@app.get("/localidades/distritos/regiao-imediata/UF/sigla/{sigla_UF_RI}", tags=["unidades federativas por região imediata"])
async def get_distritos_by_UF_sigla_RI(sigla_UF_RI: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata", {}).get("regiao-intermediaria", {}).get("UF", {}).get("sigla").lower() == sigla_UF_RI.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por região imediata, UF nome
@app.get("/localidades/distritos/regiao-imediata/UF/nome/{nome_UF_RI}", tags=["unidades federativas por região imediata"])
async def get_distritos_by_UF_RI(nome_UF_RI: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata", {}).get("regiao-intermediaria", {}).get("UF", {}).get("nome").lower() == nome_UF_RI.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    
#Filtro: por região imediata, região id
@app.get("/localidades/distritos/regiao-imediata/regiao/{id_regiao}", tags=["regiões por região imediata"])
async def get_distritos_by_regiao_id_RI(id_regiao_RI: int):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata", {}).get("regiao-intermediaria", {}).get("UF", {}).get("regiao", {}).get("regiao", {}).get("id") == id_regiao_RI]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    
#Filtro: por região imediata, região sigla
@app.get("/localidades/distritos/regiao-imediata/regiao/sigla/{sigla_regiao_RI}", tags=["regiões por região imediata"])
async def get_distritos_by_regiao_sigla_RI(sigla_regiao_RI: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata", {}).get("regiao-intermediaria", {}).get("UF", {}).get("regiao", {}).get("sigla", "").lower() == sigla_regiao_RI.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")

#Filtro: por região imediata, região nome
@app.get("/localidades/distritos/regiao-imediata/regiao/nome/{nome_regiao_RI}", tags=["regiões por região imediata"])
async def get_distritos_by_regiao_RI(nome_regiao_RI: str):
    distritos = await fetch_distritos()

    if distritos:
        distritos_encontrados = [distrito for distrito in distritos if distrito.get("municipio", {}).get("regiao-imediata", {}).get("regiao-intermediaria", {}).get("UF", {}).get("regiao", {}).get("nome").lower() == nome_regiao_RI.lower()]        
        if distritos_encontrados:
            return distritos_encontrados
        else:
            raise HTTPException(status_code=404, detail="Não encontrado")
    else:
        raise HTTPException(status_code=404, detail="Distritos não encontrados")
    

if __name__ == 'main':
    import uvicorn

    uvicorn.run('main:app', host = '0.0.0.0', port = 8000, log_level = 'info', reload = True)
