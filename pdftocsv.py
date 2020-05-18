# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:52:05 2020

@author: Sritej. N
"""

import tabula
import os
os.chdir("C:/Users/Sritej. N/Desktop")
df = tabula.read_pdf("1.pdf", pages='all')
tabula.convert_into("1.pdf", "output.csv", output_format="csv", pages='all')
