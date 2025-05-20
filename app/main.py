import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
benin_df = pd.read_csv('data/benin_clean.csv')
sierraleone_df = pd.read_csv('data/sierraleone_clean.csv')
togo_df = pd.read_csv('data/togo_clean.csv')
combined_df = pd.concat([benin_df.assign(Country='Benin'),
                         sierraleone_df.assign(Country='Sierra Leone'),
                         togo_df.assign(Country='Togo')])

# Sidebar for interactivity
st.sidebar.header('Filters')
selected_countries = st.sidebar.multiselect('Select Countries', ['Benin', 'Sierra Leone', 'Togo'], default=['Benin', 'Sierra Leone', 'Togo'])

# Filter data
filtered_df = combined_df[combined_df['Country'].isin(selected_countries)]

# Visualizations
st.title('Solar Energy Insights Dashboard')
st.header('Boxplots')
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.boxplot(data=filtered_df, x='Country', y='GHI', ax=axes[0])
axes[0].set_title('GHI')
sns.boxplot(data=filtered_df, x='Country', y='DNI', ax=axes[1])
axes[1].set_title('DNI')
sns.boxplot(data=filtered_df, x='Country', y='DHI', ax=axes[2])
axes[2].set_title('DHI')
st.pyplot(fig)

st.header('Average Metrics by Country')
avg_data = filtered_df.groupby('Country')[['GHI', 'DNI', 'DHI']].mean().reset_index()
st.bar_chart(avg_data.set_index('Country')[['GHI', 'DNI', 'DHI']])

# Top Regions Table
top_regions = avg_data.sort_values(by='GHI', ascending=False)
st.table(top_regions)