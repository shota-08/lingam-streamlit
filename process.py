import numpy as np
import pandas as pd
from IPython.display import Image
import category_encoders as ce

from graphviz import Digraph
import lingam
from lingam.utils import make_dot, make_prior_knowledge
from sklearn.preprocessing import StandardScaler

import warnings
warnings.simplefilter('ignore')

scaler = StandardScaler()

def make_dot(adjacency_matrix, labels, lower_limit=0.0):
    dot = Digraph(format='png')
    for i, label in enumerate(labels):
        dot.node(str(i), label, fontname="MS Gothic")
    for i in range(adjacency_matrix.shape[0]):
        for j in range(adjacency_matrix.shape[1]):
            if abs(adjacency_matrix[i, j]) >= lower_limit:
                dot.edge(str(j), str(i), label=f"{adjacency_matrix[i, j]:.2f}", fontname="MS Gothic")
    return dot

def preprocess_data(df):
    df = df.dropna(how="any")
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    if not categorical_columns.empty:
        encoder = ce.OrdinalEncoder(cols=categorical_columns)
        df = encoder.fit_transform(df)
    return df

def make_lingam_plot(df, object):
    df = preprocess_data(df)
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    df_dict = {}
    for i, column in enumerate(df_scaled.columns):
        df_dict[column] = i

    prior_knowledge = make_prior_knowledge(
        n_variables = len(df_scaled.columns),
        sink_variables = [df_dict[object]],
    )
    model = lingam.DirectLiNGAM(prior_knowledge = prior_knowledge)
    model.fit(df_scaled)

    dot = make_dot(
        model.adjacency_matrix_,
        labels=df.columns.to_list(),
        lower_limit=0.1 #0~1で設定可能
    )

    dot.format = 'png'
    return dot.render(f'./output/output', view=True)