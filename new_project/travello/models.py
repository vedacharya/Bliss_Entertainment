# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.files.storage import FileSystemStorage

class BookingDetail(models.Model):
    booking_datail_id = models.AutoField(primary_key=True)
    ticket_type = models.ForeignKey('TicketTypeMaster', models.DO_NOTHING)
    customer = models.ForeignKey('Customer',on_delete=models.DO_NOTHING)
    ticket_unit = models.IntegerField()
    ticket_booking = models.ForeignKey('BookingMaster',on_delete=models.DO_NOTHING)
    auth_user = models.ForeignKey('AuthUser',on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = ' booking_detail'

    def __str__(self):
        return self.ticket_type


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup,on_delete=models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission',on_delete= models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType',on_delete=models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser,on_delete=models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser,on_delete=models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookingMaster(models.Model):
    ticket_booking_id = models.AutoField(db_column='Ticket_booking_id', primary_key=True)  # Field name made lowercase.
    ticket_amount = models.FloatField()
    commision = models.FloatField()
    tax = models.FloatField(db_column='Tax')  # Field name made lowercase.
    total_charges = models.FloatField(blank=True, null=True)
    event_event = models.ForeignKey('Event',on_delete=models.DO_NOTHING)
    payment_type = models.ForeignKey('PaymentType',on_delete=models.DO_NOTHING)
    transactopn_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'booking_master'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=45)
    state = models.ForeignKey('State',on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'city'

    def __str__(self):
        return self.city_name

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    costuemr_fname = models.CharField(max_length=45)
    custoemr_lname = models.CharField(max_length=45)
    costumer_email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.costuemr_fname

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType',on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EnquaryMaster(models.Model):
    enquary_master = models.AutoField(primary_key=True)
    service_type = models.ForeignKey('ServiceType',on_delete=models.DO_NOTHING)
    services_required = models.CharField(max_length=255)
    min_guest = models.IntegerField(blank=True, null=True)
    max_guest = models.IntegerField(blank=True, null=True)
    enquary_mastercol = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    inquary_cusotmer = models.ForeignKey('InquiryCustomer',on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'enquary_master'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    evemt_name = models.CharField(max_length=45)
    location_location = models.ForeignKey('Location',on_delete=models.DO_NOTHING)
    event_image = models.ImageField(upload_to='event_pics')
    event_description = models.TextField()
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_time = models.TimeField()
    ticket_details_type = models.IntegerField()
    end_time = models.TimeField()
    last_booking_date = models.DateField()
    facebook_link = models.CharField(max_length=1000, blank=True, null=True)
    instagram_link = models.CharField(max_length=1000, blank=True, null=True)
    twitter_link = models.CharField(max_length=1000, blank=True, null=True)
    linkedin_link = models.CharField(max_length=1000, blank=True, null=True)
    event_sub_category = models.ForeignKey('EventSubCategory',on_delete=models.DO_NOTHING)
    auth_user = models.ForeignKey(AuthUser,on_delete=models.DO_NOTHING)
    # event_image = models.ForeignKey(EventImage,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event'
    
   # def __str__(self):
    #    return str(self.event_id)




class EventCategory(models.Model):
    event_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_category'

    def __str__(self):
        return self.category_name

class EventHasHashTag(models.Model):
    event = models.OneToOneField(Event,on_delete=models.DO_NOTHING, primary_key=True)
    hash_tag = models.ForeignKey('HashTag',on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_has_hash_tag'
        unique_together = (('event', 'hash_tag'),)

    def __str__(self):
        return self.hash_tag

class EventImage(models.Model):
    event_image = models.AutoField(primary_key=True)
    image_path = models.CharField(max_length=120)
    event = models.ForeignKey(Event,on_delete=models.DO_NOTHING)
    thumbnail_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_image'

    def first_image(self):
        # code to determine which image to show. The First in this case.
        return self.image_path[0]

    

class EventPayment(models.Model):
    event_payment_id = models.AutoField(primary_key=True)
    tickets_sold = models.IntegerField()
    commission_charges = models.FloatField()
    total_amount = models.FloatField()
    payment_date_time = models.DateTimeField()
    transaction_id = models.CharField(max_length=45)
    event = models.ForeignKey(Event,on_delete=models.DO_NOTHING)
    payment_type = models.ForeignKey('PaymentType',on_delete=models.DO_NOTHING)
    auth_user = models.ForeignKey(AuthUser,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_payment'

    

class EventSubCategory(models.Model):
    event_sub_category_id = models.AutoField(primary_key=True)
    event_sub_category_name = models.CharField(max_length=45)
    event_category = models.ForeignKey(EventCategory,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_sub_category'

    def __str__(self):
        return self.event_sub_category_name

class HashTag(models.Model):
    hash_tag_id = models.AutoField(primary_key=True)
    hash_tag_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'hash_tag'

    def __str__(self):
        return self.hash_tag_name

class InquiryCustomer(models.Model):
    inquary_cusotmer_id = models.AutoField(primary_key=True)
    contact_no = models.IntegerField()
    contact_name = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    organizer_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inquiry_customer'

    def __str__(self):
        return self.contact_name


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    full_address = models.CharField(max_length=100)
    landmark = models.CharField(max_length=45)
    postal_code = models.IntegerField()
    longitude = models.DecimalField(max_digits=10, decimal_places=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=10)
    city = models.ForeignKey(City,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'location'

    def __str__(self):
        return self.location_id


class OrganizerProfile(models.Model):
    organizer_profile_id = models.IntegerField(primary_key=True)
    oranizer_brand_name = models.CharField(max_length=45)
    about_organizer = models.TextField()
    profile_image_path = models.ImageField(upload_to='profile_photo')
    facebook_link = models.CharField(max_length=500, blank=True, null=True)
    instagrm_link = models.CharField(max_length=500, blank=True, null=True)
    twitter_link = models.CharField(max_length=500, blank=True, null=True)
    auth_user = models.ForeignKey(AuthUser,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'organizer_profile'

    def __str__(self):
        return self.oranizer_brand_name

class OrganizersType(models.Model):
    organizer_type_id = models.AutoField(primary_key=True)
    enquart_type = models.CharField(max_length=45)
    auth_user = models.ForeignKey(AuthUser,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'organizers_type'

    def __str__(self):
        return self.evquart_type

class PaymentType(models.Model):
    payment_type_id = models.AutoField(primary_key=True)
    payment_method = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment_type'

    def __str__(self):
        return self.payment_method

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=45)
    service_type = models.ForeignKey('ServiceType',on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service'

    def __str__(self):
        return self.sub_name

class ServiceType(models.Model):
    service_type_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=45)
    organizer_type = models.ForeignKey(OrganizersType,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'service_type'

    def __str__(self):
        return self.category_name

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=45)
    country = models.ForeignKey(Country,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state'

    def __str__(self):
        return self.state_name

class TicketCancellationMaster(models.Model):
    cancellation_id = models.AutoField(primary_key=True)
    booking_datail = models.ForeignKey(BookingDetail,on_delete=models.DO_NOTHING)
    units = models.IntegerField()
    cancellation_charges = models.FloatField()
    refund_amount = models.FloatField()
    transaction_id = models.CharField(max_length=45)
    payment_type = models.ForeignKey(PaymentType,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ticket_cancellation_master'


class TicketTypeMaster(models.Model):
    ticket_type = models.IntegerField(primary_key=True)
    ticket_name = models.CharField(max_length=45)
    ticket_total = models.IntegerField()
    ticket_available = models.IntegerField()
    ticket_sold = models.IntegerField()
    ticket_rate = models.IntegerField()
    event = models.ForeignKey(Event,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ticket_type_master'

    def __str__(self):
        return self.ticket_name


class UserHasLikeMaster(models.Model):
    auth_user = models.OneToOneField(AuthUser,on_delete=models.DO_NOTHING, primary_key=True)
    event_event = models.ForeignKey(Event,on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_has_like_master'
        unique_together = (('auth_user', 'event_event'),)


class UserReviewMaster(models.Model):
    auth_user = models.OneToOneField(AuthUser,on_delete=models.DO_NOTHING, primary_key=True)
    event = models.ForeignKey(Event,on_delete=models.DO_NOTHING)
    review = models.TextField(blank=True, null=True)
    star_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_review_master'
        unique_together = (('auth_user', 'event'),)
