# -*- coding:utf-8 -*-
import re
va = 'ming'
print va
vva = va.encode('utf-8').decode("unicode_escape")
print vva


def detect_landline(landline_number):
    if landline_number[0:1] == '0':
        return True
    else:
        return False


print  detect_landline('01080456811')
print  detect_landline('13937501357')



