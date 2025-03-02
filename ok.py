import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(layout="wide")

# Add custom CSS
st.markdown("""
    <style>
        .stPlotlyChart {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        section[data-testid="stSidebar"] {
            background-color: #f8f9fa;
        }
        .css-1d391kg {
            padding: 2rem 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sample data generation
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
np.random.seed(42)
data = {
    'Date': dates,
    'Users': np.random.normal(1000, 100, len(dates)).cumsum(),
    'Revenue': np.random.normal(5000, 500, len(dates)).cumsum(),
    'Engagement': np.random.normal(500, 50, len(dates))
}
df = pd.DataFrame(data)

# Device distribution data
device_data = {
    'Device': ['Mobile', 'Desktop', 'Tablet', 'Other'],
    'Users': [4500, 3000, 1500, 500]
}
device_df = pd.DataFrame(device_data)

# Title
st.title("📊 Modern Analytics Dashboard")
st.markdown("---")

# Create two columns for the first row
col1, col2 = st.columns(2)

with col1:
    st.subheader("User Growth Trend")
    # Area chart with Plotly
    fig_area = px.area(df, x='Date', y='Users',
                       template='plotly_white',
                       color_discrete_sequence=['#6C63FF'])
    fig_area.update_traces(fill='tonexty', line_width=2)
    fig_area.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title="",
        yaxis_title="Total Users"
    )
    st.plotly_chart(fig_area, use_container_width=True)

with col2:
    st.subheader("Revenue Trends")
    # Line chart with Plotly
    fig_line = px.line(df, x='Date', y='Revenue',
                       template='plotly_white',
                       color_discrete_sequence=['#00C49F'])
    fig_line.update_traces(line_width=3)
    fig_line.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title="",
        yaxis_title="Revenue ($)"
    )
    st.plotly_chart(fig_line, use_container_width=True)

# Create two columns for the second row
col3, col4 = st.columns(2)

with col3:
    st.subheader("Monthly Engagement")
    # Bar chart with Plotly
    fig_bar = px.bar(df, x='Date', y='Engagement',
                     template='plotly_white',
                     color_discrete_sequence=['#FF6B6B'])
    fig_bar.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title="",
        yaxis_title="Engagement Score"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col4:
    st.subheader("Device Distribution")
    # Donut chart with Plotly
    fig_donut = px.pie(device_df, values='Users', names='Device', hole=0.6,
                       template='plotly_white',
                       color_discrete_sequence=['#6C63FF', '#00C49F', '#FF6B6B', '#FFC154'])
    fig_donut.update_layout(
        height=400,
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20)
    )
    st.plotly_chart(fig_donut, use_container_width=True)

# Add some metrics
st.markdown("---")
metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    total_users = "{:,}".format(int(df['Users'].iloc[-1]))
    users_delta = "{:,}".format(int(df['Users'].iloc[-1] - df['Users'].iloc[-2]))
    st.metric(label="Total Users", value=total_users, delta="+"+users_delta)

with metric2:
    total_revenue = "${:,}".format(int(df['Revenue'].iloc[-1]))
    revenue_delta = "${:,}".format(int(df['Revenue'].iloc[-1] - df['Revenue'].iloc[-2]))
    st.metric(label="Total Revenue", value=total_revenue, delta="+"+revenue_delta)

with metric3:
    avg_engagement = "{:,}".format(int(df['Engagement'].mean()))
    engagement_delta = "{:,}".format(int(df['Engagement'].iloc[-1] - df['Engagement'].mean()))
    st.metric(label="Avg Engagement", value=avg_engagement, delta=engagement_delta)

with metric4:
    active_devices = "{:,}".format(int(device_df['Users'].sum()))
    st.metric(label="Active Devices", value=active_devices, delta="12%")