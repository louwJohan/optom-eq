from django.contrib import admin
from loan.models import Student, Loan

# Register your models here.
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    """
    Registering the Timeslot database in the admin panel.
    Setting list display and filter items
    """
    list_filter = ('date',
                   'all_returned',
                   'room',
                   )
    list_display = (
                    'date',
                    'time_taken',
                    'time_returned',
                    'student',
                    'equipment',
                    'room',
                    'equipment_returned',
                    'all_returned',
                    )
    search_fields = ['room', 'student', 'time_taken']

admin.site.register(Student)