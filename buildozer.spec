[app]

# (str) Title of your application
title = SafeDrive Ultimate

# (str) Package name
package.name = safedrive

# (str) Package domain (needed for android packaging)
package.domain = org.zeynep

# (str) Source files where the let be stored (relative to directory)
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application version
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Custom source folders for requirements
#requirements.source_dirs = ../ext_libs/kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services = NAME:ENTRYPOINT_TO_PYTHON_SCRIPT,NAME2:ENTRYPOINT2...

#
# OSX Specific
#

#
# Number of logical cpu to use for compile
#
#osx.cpu_count = 4

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version
android.build_tools_version = 33.0.2

# (bool) Use --private data storage (True) or --public storage (False)
#android.private_storage = True

# (list) The android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (str) Bootstrap to use for kivy
p4a.bootstrap = sdl2

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command with output)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
