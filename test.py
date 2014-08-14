import ctypes

sumrange_ctypes = ctypes.CDLL('./sumrange.so').sumrange

sumrange_ctypes.restype = ctypes.c_ulonglong

sumrange_ctypes.argtypes = ctypes.c_ulonglong,


def sum_range_cpython(arg)
  sumrange_ctypes(arg)

def sum_range_python(arg):
  return sum(xrange(arg))

def gays_sum(arg):
  return (arg*(arg+1))/2 - arg
