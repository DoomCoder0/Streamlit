import streamlit as st
import pandas as pd

# Učitavanje datoteke
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    # Učitavanje podataka u DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Prikazivanje podataka
    st.write(df)

    # Izbor kolone za filtriranje
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter", columns)
    selected_value = st.selectbox(f"Select value in {selected_column}", df[selected_column].unique())

    # Filtriranje podataka
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Podnaslov za grafikon
    st.subheader("Plot Data")

    # Izbor za x i y os
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    # Generiranje grafikona
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file upload...")
