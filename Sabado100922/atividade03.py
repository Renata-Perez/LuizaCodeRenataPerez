# =====================================
# Persistência / Repositório
# =====================================

MEMORIA_MUSICAS = []

def persistencia_musica_salvar(nova_musica):
    codigo_nova_musica = len(MEMORIA_MUSICAS) + 1
    # Ajuste da persistência
    nova_musica["codigo"] = codigo_nova_musica
    # Salvei na persistência/repositório.
    MEMORIA_MUSICAS.append(nova_musica)
    return nova_musica

def persistencia_musica_pesquisar_todas():
    lista_musicas = list(MEMORIA_MUSICAS)
    return lista_musicas

def persistencia_pesquisar_pelo_codigo(codigo):
    musica_procurada = None
    for musica in MEMORIA_MUSICAS:
        if musica["codigo"] == codigo:
            musica_procurada = musica
            # Pode parar o 'for' e sair dele
            break 
    # Fim do for
    return musica_procurada


# =====================================
# Regras / Casos de Uso / BO
# =====================================

def regras_musica_cadastrar(nova_musica):
    # TODO Validar a nova música
    # Exemplo: Nome de música é unico.
    # regras_musica_validar_nova_musica(nova_musica)
    nova_musica = persistencia_musica_salvar(nova_musica)
    return nova_musica

def regras_musica_pesquisar_todas():
    return persistencia_musica_pesquisar_todas()

def regras_musica_pesquisar_pelo_codigo(codigo):
    return persistencia_pesquisar_pelo_codigo(codigo)

# =====================================
# API Rest / Controlador
# =====================================

import fastapi

aplicacao_web = fastapi.FastAPI()

# ----- rotas / caminhos / salas

# ** Rota raiz ***

@aplicacao_web.get("/")
def rota_raiz():
    return {
        "ok": True,
        "versao": "Fase 1"
    }

# ** Rota músicas ***
from typing import Optional
import pydantic

class NovaMusica(pydantic.BaseModel):
    nome: str
    artista: str
    tempo:Optional[int]

@aplicacao_web.post("/musicas")
def rota_musica_cadastrar(nova_musica: NovaMusica):
    print("Registrando uma nova música: ", nova_musica.dict())
    nova_musica = regras_musica_cadastrar(nova_musica.dict())
    return nova_musica

@aplicacao_web.get("/musicas")
def rota_musica_pesquisar_todas():
    return regras_musica_pesquisar_todas()


@aplicacao_web.get("/musicas/{codigo}")
def rota_musica_pesquisar_pelo_codigo(codigo: int):
    print("Consulta pelo código: ", codigo)
    return regras_musica_pesquisar_pelo_codigo(codigo)