from kivy.app import App
from kivy.uix.label import Label

class PredatorApp(App):
    def build(self):
        return Label(text='IBLIS AYAKTA AVCI 👑\nAPK CALISIYOR')

PredatorApp().run()[app]
title = Predator
package.name = predator
package.domain = org.iblis

source.include_exts = py
version = 0.1

requirements = python3,kivy

[buildozer]
log_level = 2

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk_path =
android.ndk_path =
android.archs = arm64-v8a, armeabi-v7abuildozer android debug
