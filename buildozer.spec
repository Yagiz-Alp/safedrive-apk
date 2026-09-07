[app]

title = SafeDrive Ultimate
package.name = safedrive
package.domain = org.zeynep

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version
android.build_tools_version = 33.0.2

# (list) The android archs to build for
android.archs = arm64-v8a

# (str) Bootstrap to use for kivy
p4a.bootstrap = sdl2
