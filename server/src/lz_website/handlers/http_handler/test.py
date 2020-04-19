# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author ：biocoder
# Date   ：2020/4/2 0002 上午 10:10
# *********************************
from plotnine import *
import pandas as pd
import json
import numpy as np
import math
from os.path import dirname, realpath, basename, join
def get_image_upload_path():
    """得到图片的保存路径"""
    work_dir = dirname(dirname(dirname(realpath(__file__))))
    upload_path = join(work_dir, 'media', 'image')
    return upload_path
data = [{'padj': 2.1e-12, 'condition': 'DK_vs_CT', 'locus_tags': 'M744_RS13775', 'log2': 1.6, 'threshold': True}, {'padj': 0.677, 'condition': 'HL_vs_CT', 'locus_tags': 'M744_RS13775', 'log2': -0.14, 'threshold': False}, {'padj': '', 'condition': 'HT_vs_CT', 'locus_tags': 'M744_RS13775', 'log2': 'hypothetical protein', 'threshold': False}]

data = json.dumps(data)
df = pd.read_json(data)
a = ggplot(df, aes('log2', "-1*np.log10(padj)",color='factor(threshold)')) +\
    theme(axis_line=element_line(color="black"), panel_background= element_rect(fill='white')) + \
    geom_point()+ \
    scale_color_manual(values=("grey", "red")) +\
    geom_hline(aes(yintercept=2,), color="gray", linetype='dotted') + \
    geom_vline(aes(xintercept=-1), color="gray", linetype='dotted') + \
    geom_vline(aes(xintercept=1), color="gray", linetype='dotted') + \
    labs(title="123") + xlab("log2FoldChange") + ylab("-1*log10(padj)")

    # geom_text(aes(label="Conditions", x ="log2FoldChange", y='padj')) + \

print(a.save(filename="12345", path=get_image_upload_path()))

# 测试系统调用

# import os
# print(os.system("mongoimport  --db lz_database --type csv --headerline --ignoreBlanks --file ../../media/csv/c8882f06-e524-4410-9e58-49ee71e6c1bb.csv"))
#
#
