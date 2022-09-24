
async def create_addresses(addresses_collection, address):
    try:
        address = await addresses_collection.insert_one(address)

        if address.inserted_id:
            address = await get_addresses(addresses_collection, address.inserted_id)
            return address

    except Exception as e:
        print(f'create_address.error: {e}')

async def get_addresses(addresses_collection, address_id):
    try:
        data = await addresses_collection.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

async def get_addresses_by_id(addresses_collection, id):
    address = await addresses_collection.find_one({'_id': id})
    return address

async def get_addresses_by_user_id(addresses_collection, user_id):
    address = await addresses_collection.find_one({'user_id': user_id})
    return address

async def delete_addresses(addresses_collection, address_id):
    try:
        address = await addresses_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')
        
async def delete_addresses_by_user_id(addresses_collection, user_id):
    try:
        address = await addresses_collection.delete_one(
            {'user_id': user_id}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')
