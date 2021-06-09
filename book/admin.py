from django.contrib import admin
from .models import Category, Author, Book, BookComment

# Register your models here.
class BookCommentStackedInline(admin.StackedInline):
    model = BookComment

class BookTabularInline(admin.TabularInline):
    model = BookComment
    extra = 2

class BookAdmin(admin.ModelAdmin):
    #เอาชื่อฟังก์ชันจากโมเดลมาใส่ เพื่อให้เเสดงผลในหน้าเเอดมิน
    list_display = ['code', 'name', 'category', 'price', 'level','published','show_image']
    list_filter = ['published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug':['name']}

    #เอาชื่อตัวแปรมาใส่ในเพื่อให้ระบบเเสดงค่าให้เรา เช่น การอัพโหลดรูปจะมีปุ่มมาให้เรา
    fieldsets = (
        (None, {
            "fields": ['code','slug','name','description','price', 'level', 'image','published']}), 
        ('Category',{
            "fields": ['category','author'],'classes':['collapse']}),
       
    )
    
    inlines = [ BookTabularInline ]



admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)

