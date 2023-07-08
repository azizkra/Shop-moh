from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
# Create your models here.


class Tool(models.Model):
    name = models.CharField(max_length=350)
    image = models.ImageField(upload_to='tools/images')
    rating = models.FloatField(default=1)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upload_tool = models.FileField(upload_to='tools/uploads')
    quantity = models.PositiveIntegerField()
    is_visible = models.BooleanField(default=True)
    tool_sold = models.PositiveIntegerField(default=0)
    coinbase_payment_id = models.CharField(max_length=100)
    token = models.CharField(max_length=250)
    token_expiration = models.DateTimeField(blank=True, null=True) #يحدد تاريخ انتهاء سريان التوكن.
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-created_at']
    
    
    def get_absolute_url(self):
        return reverse('tool-detail', kwargs={'pk': self.pk})
    
    
    def activate_token(self):
        # تحديد مدة السريان بناءً على المبلغ المدفوع (مثلاً بالأشهر)
        if self.price <= 100:
            duration = timedelta(days=30) # تشغيل التوكن لمدة شهر
        else:
            duration = timedelta(days=365)  # تشغيل التوكن لمدة سنة
        
        
        # حساب تاريخ انتهاء السريان بناءً على تاريخ اليوم ومدة السريان
        expiration_date = timezone.now() + duration
        
        # حفظ تاريخ انتهاء السريان في حقل التوكن
        self.token_expiration = expiration_date
        self.save()
        
    
    # تقليل الكمية عندما المستخدمون يقومون بشراء الاداة
    def reduce_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
            if self.quantity == 0:
                self.is_visible = False
            self.save()

    
    def purchase_tool(self, payment_id):
        self.tool_sold += 1 #  زيادة عدد المبيعات للاداة
        self.coinbase_payment_id = payment_id # تخزن معرّف عملية الدفع المرتبطة بالأداة
        self.activate_token() #تقوم بتشغيل التوكن للأداة باستخدام دالة عند عملة الشراء
        self.reduce_quantity() # تقلل الكمية المتاحة للأداة بواحد
        self.save() #يتم حفظ التغييرات المحدثة في قاعدة البيانات