# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:26:47 2018

@author: frick
"""

import webbrowser
import pandas as pd
from tempfile import NamedTemporaryFile

def df_window(df):
    with NamedTemporaryFile(delete=False, suffix='.html') as f:
        df.to_html(f.name)
    webbrowser.open(f.name)
    
spam_data = pd.read_csv("Youtube01-Psy.csv", encoding='latin1')
df_window(spam_data)

