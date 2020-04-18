#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author ：biocoder
# Date   ：2020/4/2 0002 上午 10:10
# *********************************
from plotnine import *
import pandas as pd
import json
import numpy as np
import math
data = [
    {
        "Conditions": "HT",
        "log2FoldChange": -0.001094437,
        "padj": 0.998253682,
        "threshold": False
    },
    {
        "Conditions": "HL",
        "log2FoldChange": 0.813145327,
        "padj": 0.00090524,
"threshold": False
    },
    {
        "Conditions": "DK",
        "log2FoldChange": 3.527543482,
        "padj": 5.54E-53,
"threshold": True
    }
]
data = json.dumps(data)
df = pd.read_json(data)
a = ggplot(df, aes('log2FoldChange', "-1*np.log10(padj)",color='factor(threshold)')) +\
theme(axis_line=element_line(color="black"), panel_background= element_rect(fill='white')) + \
    geom_point()+ \
    scale_color_manual(values=("grey", "red")) +\
    geom_hline(aes(yintercept=2,), color="gray", linetype='dotted') + \
    geom_vline(aes(xintercept=-1), color="gray", linetype='dotted') + \
    geom_vline(aes(xintercept=1), color="gray", linetype='dotted') + \
    geom_text(aes(label="Conditions", x ="log2FoldChange", y='padj')) + \
    labs(title= 'MRRR7544')

print(a.save(filename="12345", path=))
