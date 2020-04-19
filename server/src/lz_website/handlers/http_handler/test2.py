from plotnine import *
import pandas as pd
import json
import numpy as np
import math
import json


data = [{'padj': 2.1e-12, 'condition': 'DK_vs_CT', 'locus_tags': 'M744_RS13775', 'log2': 1.6, 'threshold': True}, {'padj': 0.677, 'condition': 'HL_vs_CT', 'locus_tags': 'M744_RS13775', 'log2': -0.14, 'threshold': False}, {'padj': '', 'condition': 'HT_vs_CT', 'locus_tags': 'M744_RS13775', 'log2': 'hypothetical protein', 'threshold': False}]
data = json.dumps(data)
df = pd.read_json(data)
img = ggplot(df, aes(x='log2', y='padj', color='factor(threshold)')) + \
      theme(axis_line=element_line(color="black"), panel_background=element_rect(fill='white')) + \
      geom_point() + \
      geom_text(aes(label='condition'),hjust='left',vjust='bottom', size =10, position=position_dodge(width=1)) + \
      scale_color_manual(values=("grey", "red")) + \
      geom_hline(aes(yintercept=2, ), color="gray", linetype='dotted') + \
      geom_vline(aes(xintercept=-1), color="gray", linetype='dotted') + \
      geom_vline(aes(xintercept=1), color="gray", linetype='dotted') + \
      labs(title='1234') + xlab("log2FoldChange") + ylab("-1*log10(padj)")
print(img)