# Nuitka Splash Screen Loading Code
# Use this code to signal the splash screen removal.
import os
import tempfile

try:
    if "NUITKA_ONEFILE_PARENT" in os.environ:
        splash_filename = os.path.join(
            tempfile.gettempdir(),
            "onefile_%d_splash_feedback.tmp" % int(os.environ["NUITKA_ONEFILE_PARENT"]),
        )

        if os.path.exists(splash_filename):
            os.unlink(splash_filename)

    print("Splash Screen has been removed")
except Exception as e:
    print (e)