# -*- coding: utf-8 -*-
import re
a = 'MEM_ARGS="-Xms256m -Xmx512m"'

print a.split('-Xms')[1].split('m')[0]
print a.split('Xmx')[1].split('m')[0]