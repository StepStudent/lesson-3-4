import random
class Human:
  def __init__(self, name = "Яна Сергіївна", job = None,home = None, car = None):
    self.name = name
    self.job = job
    self.home = home
    self.car = car
    self.money = 10000
    self.gladness = 50
    self.satiety = 50
  def get_home(self):
    pass
  def get_car(self):
    pass
  def get_job(self):
    pass
  def food(self):
    pass
  def money(self):
    pass
  def work(self):
    pass
  def shopping(self):
    pass
  def chill(self):
    pass
  def clean_home(self):
    pass

  def day_indexes(self, day):
    pass
  def is_alive(self):
    pass
  def live(self, day):
    pass

class Auto:
  def __init__(self, brand_list):
    self.brand = random.choice(list(brand_list))
    self.strength = brand_list[self.brand]['strength']
    self.fuel = brand_list[self.brand]['fuel']
    self.consumption = brand_list[self.brand]['consumption']

