from bson.objectid import ObjectId

from src.models.address import (
    create_addresses,
    get_addresses_by_id,
    get_addresses_by_user_id,
    delete_addresses,
    delete_addresses_by_user_id
   )

from src.server.database import connect_db, db, disconnect_db


async def addresses_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    addresses_collection = db.address_collection

    addresses =  {
        "user_id": ObjectId("6325bffa0293e14622983528"),
        "address": [
        {
            "street": "Rua Quarenta e Sete, Numero 3",
            "cep": "8465312",
            "district": "São Paulo",
            "city": "São Paulo",
            "state": "São Paulo",
            "is_delivery": True
        }
        ]
    }

    if option == '1':
        # create addresses
        addresses = await create_addresses(
            addresses_collection,
            addresses
        )
        print(addresses)
    elif option == '2':
        # get addresses
        addresses = await get_addresses_by_user_id(
            addresses_collection,
            addresses["user_id"]
        )
        print(addresses)
   
    elif option == '3':
        # delete
        result = await delete_addresses_by_user_id(
            addresses_collection,
            addresses["user_id"]
        )

        print(result)


    await disconnect_db()