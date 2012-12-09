Description: normal distutils setup
 also removes the command xtermcolor which would require an extra package
 to be shipped correctly.
 .
 python-xtermcolor (1.2-1) unstable; urgency=low
 .
   * Initial release. (Closes: #695210)
Author: Salvo 'LtWorf' Tomaselli <tiposchi@tiscali.it>

--- python-xtermcolor-1.2.orig/setup.py
+++ python-xtermcolor-1.2/setup.py
@@ -1,9 +1,6 @@
 import os
 
-from xtermcolor import distribute_setup
-distribute_setup.use_setuptools()
-
-from setuptools import setup
+from distutils.core import setup
 
 version = '1.2'
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
