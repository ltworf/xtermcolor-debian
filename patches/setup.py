Description: Prevents installation of shell script.
 .
 python-xtermcolor (1.2-1) unstable; urgency=low
 .
Author: Salvo 'LtWorf' Tomaselli <tiposchi@tiscali.it>

--- python-xtermcolor-1.2.orig/setup.py
+++ python-xtermcolor-1.2/setup.py
@@ -12,7 +12,7 @@ setup(
   author='Scott Frazer',
   author_email='sfrazer@broadinstitute.org',
   packages=['xtermcolor'],
-  scripts=['scripts/xtermcolor'],
+  #scripts=['scripts/xtermcolor'],
   license = "MIT",
   keywords = "xterm, ANSI, xterm-256, terminal, color",
   url = "http://github.com/broadinstitute/xtermcolor",
