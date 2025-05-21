import streamlit as st
import utils

# Load and prepare data
combined_df = utils.load_data()

# Sidebar for interactivity
st.sidebar.header('Filters')
selected_countries = st.sidebar.multiselect(
    'Select Countries', ['Benin', 'Sierra Leone', 'Togo'], default=['Togo']
)

selected_metrics = st.sidebar.multiselect(
    'Select Metrics to Visualize', ['GHI', 'DNI', 'DHI'], default=['GHI', 'DNI', 'DHI']
)

# Filter data
filtered_df = utils.filter_data(combined_df, selected_countries)

# Visualizations
st.title('Solar Energy Insights Dashboard : For MoonLight Energy Solution')

if selected_metrics:
    st.header('Boxplots')
    fig = utils.plot_boxplots(filtered_df, selected_metrics)
    st.pyplot(fig)

    st.header('Average Metrics by Country')
    avg_data = utils.calculate_average_metrics(filtered_df, selected_metrics)
    st.bar_chart(avg_data.set_index('Country')[selected_metrics])

    st.header('Top Regions by GHI')
    # Still sort by GHI for ranking (if included)
    if 'GHI' in selected_metrics:
        top_regions = utils.get_top_regions_by_ghi(avg_data)
        st.table(top_regions)
    else:
        st.write("Top regions table is only shown when GHI is selected.")
else:
    st.warning("Please select at least one metric to visualize.")
