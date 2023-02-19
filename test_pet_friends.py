from api import PetFriends
from settings import valid_email, valid_password,invalid_password, invalid_email

pf=PetFriends()

#1
def test_get_api_key_for_valid_user (email=valid_email,password=valid_password):
    status,result=pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in result

#2
def test_get_list_of_pets_with_valid_key(filter='my_pets'):
    _, auth_key=pf.get_api_key(valid_email,valid_password)
    status, result= pf.get_list_of_pets(auth_key,filter)
    assert status == 200
    assert len(result['pets']) > 0

#3
def test_add_new_pet_with_photo_with_valid_key(name='Utka', animal_type='Ptica', age='4', pet_photo='images/Utka.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result= pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'age' in result

#4
def test_add_photo_of_pet_with_valid_key (pet_photo='images/Utka2.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = result['pets'][0]['id']
    status, result =pf.add_photo_of_pet(auth_key, pet_id,pet_photo)
    assert status == 200
    assert 'pet_photo' in result

#5
def test_delete_pet_with_valid_key ():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result= pf.get_list_of_pets(auth_key,"my_pets")
    pet_id=result['pets'][0]['id']
    status, result =pf.delete_pet(auth_key, pet_id)
    assert status == 200

#6
def test_update_pet_with_valid_key (name='Utka2.0', animal_type='Ptica2.0', age='4.2'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = result['pets'][0]['id']
    status, result =pf.update_pet(auth_key,pet_id , name,animal_type,age)
    assert status == 200
    assert 'created_at' in result

#7
def test_add_inform_new_pet_without_photo_with_valid_key (name='Utka3.0', animal_type='Ptica3.0', age='4.3'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_inform_about_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert 'age' in result

#8 негативных тестов+2 недостающих вверху =10
#1- не верный логин и пас(ошибка)
def test_get_api_key_for_invalid_user (email=invalid_email,password=invalid_password):
    status,result=pf.get_api_key(email,password)
    assert status == 200

#2- Не верный фильтр(ошибка)
def test_get_list_of_pets_with_valid_key_invalid_filter():
    _, auth_key=pf.get_api_key(valid_email,valid_password)
    status, result= pf.get_list_of_pets(auth_key, 'your_pets')
    assert status == 200

#3- Не заполненные поля name, animal_type, age (создаёт карточку с пустыми полями)
def test_add_new_pet_with_invalid_key_0_params(name='', animal_type='', age='', pet_photo='images/Utka.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result= pf.add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert 'created_at' in result

#4-Использование чужого id при замене фото(ошибка)
def test_add_photo_of_pet_with_valid_key_wrong_id (pet_photo='images/Utka2.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id='35bb5e14-9a14-4e6e-84c3-f2e5213cf288' #изменять в ручную
    status, result =pf.add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert 'pet_photo' in result

#5-Использование чужого id при удаление(удаляет, а не должен)
def test_delete_pet_with_valid_key_wrong_id():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id = '0098cf06-8fef-4f30-b620-d12c83a15efc' #изменять в ручную
    status, result =pf.delete_pet(auth_key, pet_id)
    assert status == 200

#6-Изменение чужого питомца (изменяет, а не должен)
def test_update_pet_with_valid_key_wrong_id (name='!@#$%^&*()', animal_type='Ptica2.0', age='три'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_id='2584bb7c-be63-4ff2-a0a7-eca473edf50b' #изменять в ручную
    status, result =pf.update_pet(auth_key,pet_id , name,animal_type,age)
    assert status == 200
    assert 'created_at' in result

#7-Создание карточки питомца c неверными параметрами (нет ограничения в используемых символах)
def test_add_inform_new_pet_without_photo_with_valid_key_wrong_params (name='!"№%::%№"!1', animal_type='<>/|', age='two'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_inform_about_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert 'age' in result

#8-Создание карточки питомца c параметрами большой длины (ругается на длину string longer than 2147483647 bytes)
def test_add_inform_new_pet_without_photo_with_valid_key_wrong_params2 (name='!"№%::%№"!'*1000, animal_type='<>/|'*1000000, age='two'*1000000000):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_inform_about_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert 'age' in result
