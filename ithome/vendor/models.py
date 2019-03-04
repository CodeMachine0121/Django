from django.db import models
# Create your models here.


class Vendor(models.Model):
    vendor_name=models.CharField(max_length = 20) #攤販名稱
    store_name = models.CharField(max_length=10)#攤販店家名稱
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    price_name = models.DecimalField(max_digits=3,decimal_places=0)
    #店家價錢(最高位數,小數後位數)
    food_vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    #這食物是哪間攤販做的 (多對一(many-to-one)的關聯)
    #on_delete 代表的是當對應的類別被刪除之後，這些對應到別人的資料要怎麼被處理，而 CASCADE 就是一倂刪除
    #一個攤販會賣各式各樣的食物，當它今天收店了，你就也再也吃不到它賣的每一樣食物了

#變更完 打 python manage.py makemigrations vendor
