import pandas as pd
import altair as alt
import streamlit as st


def plot_emotion_probabilities(emotion_probs):
    # Helper function to plot emotion probabilities

    emotions = list(emotion_probs.keys())
    probabilities = list(emotion_probs.values())

    # Bar chart showing probabilities for each class
    df_prob = pd.DataFrame({'Class': emotions, 'Probability': probabilities})
    chart = alt.Chart(df_prob).mark_bar().encode(
        x='Probability',
        y=alt.Y('Class', sort='-x')
    ).properties(
        width=500,
        height=200
    )
    
    return chart