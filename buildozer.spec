[app]

# (str) Title of your application
title = Chess Assistant

# (str) Package name
package.name = chessassistant

# (str) Package domain (needed for android packaging)
package.domain = org.chess

# (list) Source files to include (let it include python files and assets)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# تأكد من تضمين مكتبات Kivy و Chess و Pillow هنا
requirements = python3,kivy,chess,pillow

# (str) Supported orientations
orientation = portrait

# (list) Permissions
# صلاحيات الإنترنت أو قراءة الشاشة إن لزم الأمر
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
