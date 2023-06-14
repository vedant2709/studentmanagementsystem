from cx_Freeze import *
import sys
includefiles=['icon.ico','bg.jpg','logo.png','password.png','student.png','student1.png','user.png']
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "student management system",
     "TARGETDIR",
     "[TARGETDIR]\login.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="STUDENT MANAGEMENT SYSTEM",
    author="Vedant Chaudhary",
    name="student management system",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="login.py",
            base=base,
            icon='icon.ico',
        )
    ]
)
