from django.db import models

# for deletion of the attachments after deletion of object
from django.db.models.signals import post_delete
from django.dispatch import receiver

# for slugifying the fields
from django.utils.text import slugify



# Page Handler ===================================================================================== >

class Page_Handler(models.Model) :
    page_name = models.CharField(max_length=100, null=True, blank=True)
    page_name_slug = models.CharField(max_length=100, null=True, blank=True)
    meta_title = models.CharField(max_length=200, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.page_name_slug = slugify(self.page_name)
        super(Page_Handler, self).save(*args, **kwargs)
    
    def __str__(self) :
        return self.page_name + " (pk=" + str(self.pk) + ")"



class Home(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    image1 = models.ImageField(upload_to='home', null=True, blank=True)

    def __str__(self) :
        return str(self.index) + "- " + self.title

@receiver(post_delete, sender=Home)
def submission_delete2(sender, instance, **kwargs) :
    instance.image1.delete(False)


# Portfolio ===================================================================================== >

class Portfolio(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_name_slug = models.CharField(max_length=100, null=True, blank=True)
    client_tagline = models.TextField(null=True, blank=True)

    service_advt = models.TextField(null=True, blank=True)
    service_advt_bool = models.BooleanField(default=False, null=True, blank=True)
    service_bi = models.TextField(null=True, blank=True)
    service_bi_bool = models.BooleanField(default=False, null=True, blank=True)
    service_digital = models.TextField(null=True, blank=True)
    service_digital_bool = models.BooleanField(default=False, null=True, blank=True)

    detail = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='portfolio', null=True, blank=True)
    image_wide = models.BooleanField(default=False, null=True, blank=True)

    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.client_name_slug = slugify(self.client_name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self) :
        return str(self.index) + " (" + self.client_name + " )"

    def get_absolute_url(self) :
        return f'/portfolio/{self.client_name_slug}/'

@receiver(post_delete, sender=Portfolio)
def submission_delete(sender, instance, **kwargs) :
    instance.image1.delete(False)



class Portfolio_Image(models.Model) :

    fk = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)
    image1 = models.ImageField(upload_to='portfolio', null=True, blank=True)
    
    def __str__(self) :
        if self.fk :
            return str(self.index) + " (" + self.client_name + " )"
        else :
            return str(self.index) + " ( None, pk =" + self.pk + " )"

@receiver(post_delete, sender=Portfolio_Image)
def submission_delete1(sender, instance, **kwargs) :
    instance.image1.delete(False)



# Services ===================================================================================== >

class Service(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    service_name = models.CharField(max_length=150, null=True, blank=True)
    service_name_slug = models.CharField(max_length=150, null=True, blank=True)
    service_inner = models.TextField(null=True, blank=True)
    service_intro = models.TextField(null=True, blank=True)
    service_detail = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to="service", null=True, blank=True)
    image2 = models.ImageField(upload_to="service", null=True, blank=True)
    image_before = models.ImageField(upload_to="service", null=True, blank=True)
    image_after = models.ImageField(upload_to="service", null=True, blank=True)

    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.service_name_slug = slugify(self.service_name)
        super(Service, self).save(*args, **kwargs)

    def __str__(self) :
        return self.service_name + " (pk=" + str(self.pk) + ")" 

    def get_absolute_url(self) :
        return f'/service/{self.service_name_slug}/'

@receiver(post_delete, sender=Service)
def submission_delete3(sender, instance, **kwargs) :
    instance.image1.delete(False)
    instance.image2.delete(False)
    instance.image_before.delete(False)
    instance.image_after.delete(False)



class Service_Sub(models.Model) :

    fk = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    tiny_head = models.CharField(max_length=250, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to="service", null=True, blank=True)

    def __str__(self) :
        if self.fk :
            return str(self.index) + " (" + self.name + " )"
        else :
            return str(self.index) + " ( None, pk =" + self.pk + " )"

@receiver(post_delete, sender=Service_Sub)
def submission_delete4(sender, instance, **kwargs) :
    instance.image1.delete(False)



class Our_Team(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    desg = models.CharField(max_length=200, null=True, blank=True)
    image1 = models.ImageField(upload_to='team', null=True, blank=True)

    def __str__(self) :

        return self.name

@receiver(post_delete, sender=Our_Team)
def submission_delete5(sender, instance, **kwargs) :
    instance.image1.delete(False)





    

