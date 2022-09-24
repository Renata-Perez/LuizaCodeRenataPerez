import email
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()

OK = "OK"
FALHA = "FALHA"


@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')


#USUÁRIO



# Classe representando os dados do cliente
MEMORIA_USUARIO = []


#ENDEREÇO

# Classe representando os dados do endereço do cliente
MEMORIA_ENDERECO = []

class Endereco(BaseModel):
    id_endereco: str
    rua: str
    cep: str
    cidade: str
    estado: str


class Usuario(BaseModel):
    id: str
    nome: str
    email: str
    senha: str
    enderecos: List[Endereco] = []

@app.post("/usuario")
async def cadastrar_usuario(novo_usuario: Usuario):
    print("Registrar novo usuário: ",novo_usuario.dict())
    return salvar_usuario(novo_usuario)


def salvar_usuario(novo_usuario):
    MEMORIA_USUARIO.append(novo_usuario)
    return novo_usuario


# Criar um usuário,
# se tiver outro usuário com o mesmo ID retornar falha, 
# se o email não tiver o @ retornar falha, 
# senha tem que ser maior ou igual a 3 caracteres, 
# senão retornar OK
@app.post("/usuario/")
async def criar_usuario(usuario: Usuario):
    if usuario.id in db_usuarios:
        return FALHA
    db_usuarios[usuario.id] = usuario
    return OK


# Se o id do usuário existir, retornar os dados do usuário
# senão retornar falha
@app.get("/usuario")
async def retornar_usuario(id:str):
    return pesquisar_usuario_por_id(id)
    

def pesquisar_usuario_por_id(id:str):
    usuario_pesquisado = FALHA
    for usuario in MEMORIA_USUARIO:
        if usuario.id == id:
            usuario_pesquisado = usuario
            break
    return usuario_pesquisado



# Se existir um usuário com exatamente o mesmo nome, retornar os dados do usuário
# senão retornar falha
@app.get("/usuario/nome/{nome}")
async def retornar_usuario_com_nome(nome:str):
    nome_pesquisado = FALHA
    for usuario in MEMORIA_USUARIO:
        if usuario.nome == nome:
            nome_pesquisado = usuario
            break  
    return nome_pesquisado


# Se o id do usuário existir, deletar o usuário e retornar OK
# senão retornar falha
# ao deletar o usuário, deletar também endereços e carrinhos vinculados a ele
@app.delete("/usuario/{id}")
async def deletar_usuario(id: str):
    for usuario in MEMORIA_USUARIO:
        if usuario.id == id:
            MEMORIA_USUARIO.remove(usuario)
            return OK
    return FALHA


# Se não existir usuário com o id_usuario retornar falha, 
# senão retornar uma lista de todos os endereços vinculados ao usuário
# caso o usuário não possua nenhum endereço vinculado a ele, retornar 
# uma lista vazia
### Estudar sobre Path Params (https://fastapi.tiangolo.com/tutorial/path-params/)
@app.get("/usuario/{id}/enderecos")
async def retornar_enderecos_do_usuario(id: str):
    for usuario in MEMORIA_USUARIO:
        if usuario.id != id:
            return FALHA
    return usuario.enderecos


# Retornar todos os emails que possuem o mesmo domínio
# (domínio do email é tudo que vêm depois do @)
# senão retornar falha
@app.get("/usuarios/emails/{dominio}")
async def retornar_emails(dominio: str):
    print("Consulta pelo domínio: ", dominio)
    email_pesquisado= FALHA
    lista_email = []
    for usuario in MEMORIA_USUARIO:
        if usuario.email.endswith(dominio):
            lista_email.append(usuario.email)
    if len(lista_email) == 0:
        return FALHA
    return lista_email
    






# Classe representando a lista de endereços de um cliente
class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []



@app.post("/endereco")
async def cadastrar_endereco(novo_endereco: Endereco):
    print("Resgistrar novo endereço: ", novo_endereco.dict())    
    return salvar_endereco(novo_endereco)


def salvar_endereco(novo_endereco: Endereco):
    MEMORIA_ENDERECO.append(novo_endereco)
    return novo_endereco



# Se não existir usuário com o id_usuario retornar falha, 
# senão cria um endereço, vincula ao usuário e retornar OK
@app.post("/endereco/{id_usuario}")
async def criar_endereco(endereco: Endereco, id_usuario: str):
    usuario_encontrado = pesquisar_usuario_por_id(id_usuario)
    if usuario_encontrado == FALHA:
        return FALHA
    
    endereco_salvo = salvar_endereco(endereco)
    usuario_encontrado.enderecos.append(endereco_salvo)
    return OK


# Se não existir endereço com o id_endereco retornar falha, 
# senão deleta endereço correspondente ao id_endereco e retornar OK
# (lembrar de desvincular o endereço ao usuário)
@app.delete("/endereco/{id_endereco}")
async def deletar_endereco(id_endereco: str):
    for endereco in MEMORIA_ENDERECO:
        if endereco.id_endereco != id_endereco:
            return FALHA
        MEMORIA_ENDERECO.remove(endereco)
        endereco_usuario(id_endereco)
    return OK

    


def endereco_usuario(id_endereco):
    for usuario in MEMORIA_USUARIO:
        for endereco in usuario.enderecos:
            if endereco.id_endereco == id_endereco:
                usuario.enderecos.remove(endereco)
        
    return OK



#PRODUTO

# Classe representando os dados do produto
MEMORIA_PRODUTO = []

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float


# @app.post("/produto")
# def cadastrar_produto(novo_produto: Produto):
#     print("Registrar novo produto: ", novo_produto.dict())
#     return salvar_produto(novo_produto)


# def salvar_produto(novo_produto):
#     MEMORIA_PRODUTO.append(novo_produto)
#     return novo_produto


# Se tiver outro produto com o mesmo ID retornar falha, 
# senão cria um produto e retornar OK
@app.post("/produto")
async def criar_produto(produto: Produto):
    for produto_existente in MEMORIA_PRODUTO:
        if produto_existente.id == produto.id:
            return FALHA
    MEMORIA_PRODUTO.append(produto)
    return OK


# Se não existir produto com o id_produto retornar falha, 
# senão deleta produto correspondente ao id_produto e retornar OK
# (lembrar de desvincular o produto dos carrinhos do usuário)
@app.delete("/produto/{id_produto}")
async def deletar_produto(id_produto: int):
    for produto in MEMORIA_PRODUTO:
        if produto.id == id_produto:
            MEMORIA_PRODUTO.remove(produto)
            return OK
    return FALHA
    






#CARRINHO

# Classe representando o carrinho de compras de um cliente com uma lista de produtos
class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    id_produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int


db_usuarios = {}
db_produtos = {}
db_end = {}        # enderecos_dos_usuarios
db_carrinhos = {}

# Se não existir usuário com o id_usuario ou id_produto retornar falha, 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
@app.post("/carrinho/{id_usuario}/{id_produto}/")
async def adicionar_carrinho(id_usuario: int, id_produto: int):
    return OK


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_carrinho(id_usuario: int):
    return CarrinhoDeCompras


# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o o número de itens e o valor total do carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_total_carrinho(id_usuario: int):
    numero_itens, valor_total = 0
    return numero_itens, valor_total


# Se não existir usuário com o id_usuario retornar falha, 
# senão deleta o carrinho correspondente ao id_usuario e retornar OK
@app.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    return OK