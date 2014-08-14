import ctypes

sumrange_ctypes = ctypes.CDLL('./sumrange.so').sumrange

sumrange_ctypes.restype = ctypes.c_ulonglong

sumrange_ctypes.argtypes = ctypes.c_ulonglong,

print sumrange_ctypes(10**8)
