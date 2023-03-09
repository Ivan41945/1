import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/Users/ivan/PycharmProjects/Selenium/tests/chromedriver')
   pytest.driver.implicitly_wait(5)
   pytest.driver.maximize_window()

   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   pytest.driver.find_element_by_id('email').send_keys('redchief21@mail.ru')
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()

   yield

   pytest.driver.quit()

def test_all_pets(): #Присутствуют все питомцы
   element=WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
   element=WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   #К-во петов из профиля
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   #К-во карточек
   number_of_pets = len(pets)

   assert number == number_of_pets,'Не все питомцы'


def test_photo():#Хотя бы у половины питомцев есть фото.
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "th img")))
   photos = pytest.driver.find_elements_by_css_selector('th img')
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   number_of_pets = len(pets)
   photo=0
   for i in range(len(photos)):
      if photos[i].get_attribute("src") !='':
        photo+=1
   number_of_pets = number_of_pets / 2
   assert photo>=number_of_pets,'Более чем у половины карточек нет фото'

def test_name_breed_age ():#У всех питомцев есть имя, возраст и пород
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[1]")))
   names=pytest.driver.find_elements_by_xpath('//table/tbody/tr/td[1]')
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[2]")))
   breeds=pytest.driver.find_elements_by_xpath('//table/tbody/tr/td[2]')
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[3]")))
   ages = pytest.driver.find_elements_by_xpath('//table/tbody/tr/td[3]')
   nm=0
   for i in range(len(names)):
      if names[i].text =='' or breeds[i].text =='' or ages[i].text =='':
         nm+=1
   assert nm==0,'Не заполненно одно из полей(имя,порода,возраст)'

def test_different_name ():#У всех питомцев разные имена
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[1]")))
   names = pytest.driver.find_elements_by_xpath('//table/tbody/tr/td[1]')
   nm,nm1=[],[]
   for i in names:
      nm.append(i.text)
      if i.text in nm1:
         continue
      else:
         nm1.append(i.text)
   assert nm==nm1, "Повторяются имена"

def test_unique():#В списке нет повторяющихся питомцев. 
   time.sleep(5)
   cards = pytest.driver.find_elements_by_xpath('//table/tbody/tr')
   crd, crd_unq = [], []
   for i in cards:
      crd.append(i.text)
      if i.text in crd_unq:
         continue
      else:
         crd_unq.append(i.text)
   assert crd == crd_unq, 'Повторяются карточки'






