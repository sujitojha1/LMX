from django.contrib import admin
from django.contrib import messages

# LMS application imports.
<<<<<<< HEAD
from .models.course_model import Course, GradingSchemeName, Section, GradingScheme
from .models.enrollment_model import Enrollment
from .models.users_model import Staff, Student


# Registers the student profile model at the admin backend.
class StudentAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user__username',)
    ordering = ['user__username', ]
=======
from .models.profile_model import Profile
from .models.course_model import Course, StudentCourse
from .models.assignment_model import Assignment, StudentAssignment
from .models.user_role_model import Role
from .models.files_model import File
from .models.blog_model import Post
from .models.notification_settings_model import NotificationSetting

class NotificationSettingAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)
    ordering = ['user', ]
>>>>>>> week1-patch-integration

# Registers the notification setting model for user at the admin backend.
admin.site.register(NotificationSetting, NotificationSettingAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user', 'email_confirmed')
    search_fields = ('user','user_tz')
    ordering = ['user', ]

admin.site.register(Student, StudentAdmin)


# Registers the staff profile model at the admin backend.
class StaffAdmin(admin.ModelAdmin):
    list_filter = ('is_admin', 'is_teacher', 'is_teaching_assistant')
    search_fields = ('user__username',)
    ordering = ['user__username', 'is_admin', 'is_teacher', 'is_teaching_assistant']


admin.site.register(Staff, StaffAdmin)

class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'courses', 'registered')
    list_filter = ('user',)
    search_fields = ('user__username', 'courses')
    ordering = ['user__username', ]

# Registers the student courses model at the admin backend.
admin.site.register(StudentCourse, StudentCourseAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_admin', 'is_teacher', 'is_teaching_assistant', 'is_student')
    list_filter = ('is_admin', 'is_teacher', 'is_teaching_assistant', 'is_student')
    search_fields = ('user__username',)
    ordering = ['user__username',]

# Registers the staff profile model at the admin backend.
admin.site.register(Role, RoleAdmin)

# Registers the course details model at the admin backend.
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('allow_self_enroll', 'enrollment_open_to_all', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    ordering = ['title', 'start_date']


admin.site.register(Course, CourseAdmin)


# Registers enrollment model at the admin backend.
class EnrollmentAdmin(admin.ModelAdmin):
    list_filter = ('course', 'section', 'student')
    search_fields = ('student__user__username', 'course__title')
    ordering = ['course__title', 'student__user__username']


admin.site.register(Enrollment, EnrollmentAdmin)


# Registers the course-section model at the admin backend.
class SectionAdmin(admin.ModelAdmin):
    list_filter = ('section_name', 'course')
    search_fields = ('section_name', 'course')
    ordering = ['section_name', 'course']


admin.site.register(Section, SectionAdmin)


# Registers the grading scheme name model at the admin backend.
class GradingSchemeNameAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['name']


admin.site.register(GradingSchemeName, GradingSchemeNameAdmin)


<<<<<<< HEAD
# Registers the grading scheme model at the admin backend.
class GradingSchemeAdmin(admin.ModelAdmin):
    list_filter = ('scheme_name',)
    search_fields = ('scheme_name__name', 'grade')
    ordering = ['scheme_name__name', '-score_range_begin']
=======
    list_display = ('title', 'user', 'published')
    list_filter = ('user',)
    search_fields = ('title',)
>>>>>>> week1-patch-integration

    def publish_course(modeladmin, request, queryset):
        queryset.update(published = 1)
        messages.success(request, "Selected courses are published successfully !!")

    def unpublish_course(modeladmin, request, queryset):
        queryset.update(published = 0)
        messages.success(request, "Selected courses are unpublished successfully !!")

    admin.site.add_action(publish_course, "Publish Course")
    admin.site.add_action(unpublish_course, "Unpublish Course")

# Registers the article model at the admin backend.
admin.site.register(Course, CourseAdmin)

class FileAdmin(admin.ModelAdmin):

    list_display = ('name', 'date_created',)
    list_filter = ('name',)
    search_fields = ('name',)
    raw_id_fields = ('course',)

<<<<<<< HEAD
admin.site.register(GradingScheme, GradingSchemeAdmin)
=======
# Registers the article model at the admin backend.
admin.site.register(File, FileAdmin)

class PostAdmin(admin.ModelAdmin):

    list_display = ('author', 'title', 'date_posted')
    list_filter = ('author','date_posted')
    search_fields = ('author','date_posted')

# Registers the Blog Post model at the admin backend.
admin.site.register(Post, PostAdmin)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'for_course', 'created_by')
    list_filter = ('for_course', 'created_by')

@admin.register(StudentAssignment)
class StudentAssignmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'assignment',)
    list_filter = ('user__username', 'assignment__name',)
>>>>>>> week1-patch-integration
