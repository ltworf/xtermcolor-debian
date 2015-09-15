Description: normal distutils setup
 Changes the setup.py to use the standard distutils to install,
 rather than that weird stuff that will attempt to download files.
 .
 Also removes the command xtermcolor which would require an extra package
 to be shipped correctly.
 .
 python-xtermcolor (1.2.1-1) unstable; urgency=low
 .
   * New upstream release
   * Updated patches to work with different path
   * Dropped vt100 patch, now part of upstream
Author: Salvo 'LtWorf' Tomaselli <tiposchi@tiscali.it>

--- python-xtermcolor-1.2.1.orig/setup.py
+++ python-xtermcolor-1.2.1/setup.py
@@ -1,9 +1,6 @@
 import os
 
-from xtermcolor import distribute_setup
-distribute_setup.use_setuptools()
-
-from setuptools import setup
+from distutils.core import setup
 
 version = '1.2.1'
 README = os.path.join(os.path.dirname(__file__), 'README')
@@ -18,11 +15,6 @@ setup(
   packages=['xtermcolor'],
   package_data={'xtermcolor': ['distribute_setup.py']},
   install_requires=[],
-  entry_points={
-    'console_scripts': [
-      'xtermcolor = xtermcolor.Main:Cli'
-    ]
-  },
   license = "MIT",
   keywords = "xterm, ANSI, xterm-256, terminal, color",
   url = "http://github.com/broadinstitute/xtermcolor",
