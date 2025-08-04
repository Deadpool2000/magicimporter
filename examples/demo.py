from magicimporter import magic_import

# This will auto-install AND lazy-load numpy
np = magic_import("numpy", lazy=True, auto_install=True)

# Still not loaded...
print("Preparing to use numpy...")

# Now numpy is imported:
print(np.zeros((2, 2)))
