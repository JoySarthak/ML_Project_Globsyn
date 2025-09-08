import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio

# Load the dataset
df = pd.read_csv('mobile_sales_dataset.csv')

# Clean the data
df['Mobile'] = df['Mobile'].str.strip()
df.drop_duplicates(keep='first', inplace=True)
df = df.dropna()

# Create charts directory
import os
if not os.path.exists('charts'):
    os.makedirs('charts')

print("Generating colorful charts...")

# 1. Brand-wise Distribution (Pie Chart)
print("Creating brand distribution chart...")
brands = df['Brands'].value_counts()
df_brands = brands.reset_index()
df_brands.columns = ['Brands','Count']

# Filter main brands (threshold 110)
threshold = 110
df_main = df_brands[df_brands['Count'] >= threshold]
df_others = df_brands[df_brands['Count'] < threshold]
others_count = df_others['Count'].sum()
df_main = pd.concat([df_main, pd.DataFrame({'Brands': ['Others'], 'Count': [others_count]})], ignore_index=True)

# Custom colors for pie chart (similar to GnBu palette)
colors = ['#f7fcf0','#e0f3db','#ccebc5','#a8ddb5','#7bccc4','#4eb3d3','#2b8cbe','#08589e']

fig1 = go.Figure(data=[go.Pie(
    labels=df_main['Brands'], 
    values=df_main['Count'],
    hole=0,
    textinfo='label+percent',
    textposition='auto',
    marker=dict(colors=colors, line=dict(color='#000000', width=2)),
    pull=[0.1, 0.07, 0, 0, 0, 0, 0, 0.05]  # explode effect
)])

fig1.update_layout(
    title={
        'text': "Brand-wise Distribution",
        'y':0.95,
        'x':0.02,
        'xanchor': 'left',
        'yanchor': 'top',
        'font': {'family': 'serif', 'color': 'Blue', 'size': 16}
    },
    showlegend=True,
    legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02),
    width=900,
    height=600
)

fig1.write_html("charts/brand_distribution.html")

# 2. Number of Models by Brands
print("Creating models by brand chart...")
models_of_company = df.groupby('Brands')['Models'].nunique().sort_values(ascending=False)

fig2 = go.Figure()

# Bar chart
fig2.add_trace(go.Bar(
    x=models_of_company.index,
    y=models_of_company.values,
    marker_color=px.colors.sequential.Viridis[:len(models_of_company)],
    name='Number of Models'
))

# Add trend line
fig2.add_trace(go.Scatter(
    x=models_of_company.index,
    y=models_of_company.values,
    mode='lines+markers',
    line=dict(color='blue', width=2),
    marker=dict(color='blue', size=8),
    name='Trend Line'
))

fig2.update_layout(
    title={
        'text': "Number of Models By Brands",
        'y':0.95,
        'x':0.02,
        'xanchor': 'left',
        'yanchor': 'top',
        'font': {'family': 'serif', 'color': 'Blue', 'size': 16}
    },
    xaxis_title='Company',
    yaxis_title='Number of Models',
    xaxis=dict(tickangle=90),
    showlegend=True,
    width=1200,
    height=700
)

fig2.write_html("charts/models_by_brand.html")

# 3. Top 5 Brands and Their Most Sold Mobiles (Donut Chart)
print("Creating top brands and mobiles chart...")
y = df['Brands'].value_counts().head(5)
c = df['Brands'].value_counts().head(5).index
df_top_brands = df[df['Brands'].isin(c)]
ld = df_top_brands.groupby('Brands')['Mobile'].value_counts().reset_index()
idx = ld.groupby('Brands')['count'].idxmax()
max_df = ld.loc[idx]

# Create subplot with donut charts
fig3 = make_subplots(
    rows=1, cols=1,
    specs=[[{'type': 'domain'}]],
    subplot_titles=['Top Performing Brands and Their Top Mobiles']
)

# Outer donut (top mobiles)
fig3.add_trace(go.Pie(
    labels=max_df['Mobile'],
    values=max_df['count'],
    hole=0.6,
    domain=dict(x=[0, 1], y=[0, 1]),
    textinfo='percent',
    textposition='auto',
    marker=dict(colors=px.colors.sequential.Blues_r[:len(max_df)]),
    name="Top Mobiles"
), row=1, col=1)

# Inner pie (top brands)
fig3.add_trace(go.Pie(
    labels=y.index,
    values=y.values,
    hole=0.3,
    domain=dict(x=[0.25, 0.75], y=[0.25, 0.75]),
    textinfo='percent',
    textposition='auto',
    marker=dict(colors=px.colors.sequential.Greens_r[:len(y)]),
    name="Top Brands"
), row=1, col=1)

fig3.update_layout(
    title={
        'text': "Top Performing Brands and Their Top Mobiles",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'family': 'serif', 'color': 'Purple', 'size': 16}
    },
    showlegend=True,
    width=1000,
    height=600
)

fig3.write_html("charts/top_brands_mobiles.html")

# 4. Top 10 Most Sold Mobile Phones
print("Creating top 10 mobiles chart...")
T10_M = df['Mobile'].value_counts().head(10)

fig4 = go.Figure(data=[
    go.Bar(
        x=T10_M.index,
        y=T10_M.values,
        marker_color=px.colors.sequential.Viridis[:len(T10_M)],
        text=T10_M.values,
        textposition='outside'
    )
])

fig4.update_layout(
    title={
        'text': "Top 10 Most Sold Phones",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'color': 'Blue', 'size': 16}
    },
    xaxis_title='Mobile Phone',
    yaxis_title='Count',
    xaxis=dict(tickangle=45),
    width=1000,
    height=800
)

fig4.write_html("charts/top_10_mobiles.html")

# 5. Apple Model Distribution
print("Creating Apple model distribution...")
df_Apple = df[df['Brands']=="Apple"]
c_a = df_Apple['Models'].value_counts()

fig5 = go.Figure(data=[
    go.Bar(
        x=c_a.values,
        y=c_a.index,
        orientation='h',
        marker_color=px.colors.sequential.Blues[:len(c_a)],
        text=c_a.values,
        textposition='outside'
    )
])

fig5.update_layout(
    title="Distribution of Apple Models",
    xaxis_title='Count',
    yaxis_title='Apple Models',
    width=1200,
    height=800
)

fig5.write_html("charts/apple_models.html")

# 6. Top 10 Colors
print("Creating color distribution chart...")
color_count = df['Colors'].value_counts().head(10)

# Custom color mapping
color_mapping = {
    "Black": "#000000", "Gold": "#FFD700", "White": "#F8F6F0", "Blue": "#0000FF",
    "Silver": "#BCC6CC", "Red": "#FF0000", "Grey": "#808080", "Midnight Black": "#00040D",
    "Space Grey": "#717378", "Rose Gold": "#B76E79"
}

actual_colors = [color_mapping.get(color, "#888888") for color in color_count.index]

fig6 = go.Figure(data=[
    go.Bar(
        x=color_count.index,
        y=color_count.values,
        marker_color=actual_colors,
        text=color_count.values,
        textposition='outside'
    )
])

fig6.update_layout(
    title="Top 10 Colors",
    xaxis_title='Colors',
    yaxis_title='Count',
    xaxis=dict(tickangle=45),
    width=1000,
    height=700
)

fig6.write_html("charts/top_colors.html")

# 7. Mean Selling Price by Brands
print("Creating mean selling price chart...")
Mean_agg_saleprice = df.groupby('Brands')['Selling Price'].mean().sort_values(ascending=False)

fig7 = go.Figure(data=[
    go.Bar(
        x=Mean_agg_saleprice.values,
        y=Mean_agg_saleprice.index,
        orientation='h',
        marker=dict(
            color=Mean_agg_saleprice.values,
            colorscale='Blues',
            showscale=True,
            colorbar=dict(title="Mean Selling Price")
        ),
        text=[f'{x:.0f}' for x in Mean_agg_saleprice.values],
        textposition='outside'
    )
])

fig7.update_layout(
    title="Mean Selling Price of Each Brand",
    xaxis_title='Mean Selling Price (₹)',
    yaxis_title='Brands',
    width=1200,
    height=800
)

fig7.write_html("charts/mean_selling_price.html")

# 8. Mean Ratings by Brands  
print("Creating mean ratings chart...")
brand_rating = df[["Brands","Rating"]]
Mean_agg_rating = brand_rating.groupby('Brands')['Rating'].mean().sort_values(ascending=False)
cutoff_value = 4.0

fig8 = go.Figure()

fig8.add_trace(go.Bar(
    x=Mean_agg_rating.values,
    y=Mean_agg_rating.index,
    orientation='h',
    marker=dict(
        color=Mean_agg_rating.values,
        colorscale='RdYlBu_r',
        showscale=True,
        colorbar=dict(title="Mean Rating")
    ),
    text=[f'{x:.2f}' for x in Mean_agg_rating.values],
    textposition='outside'
))

# Add cutoff line
fig8.add_shape(
    type="line",
    x0=cutoff_value, x1=cutoff_value,
    y0=-0.5, y1=len(Mean_agg_rating)-0.5,
    line=dict(color="black", width=2, dash="dash")
)

fig8.add_annotation(
    x=cutoff_value,
    y=len(Mean_agg_rating)-1,
    text=f"Cutoff: {cutoff_value:.2f}",
    showarrow=False,
    xanchor="left"
)

fig8.update_layout(
    title="Mean Ratings of Each Brand",
    xaxis_title='Mean Rating',
    yaxis_title='Brands',
    width=1200,
    height=800
)

fig8.write_html("charts/mean_ratings.html")

# 9. Mean Discount by Brands
print("Creating mean discount chart...")
Mean_agg_discount = df.groupby('Brands')['Discount'].mean().sort_values(ascending=False)
cutoff_value_discount = Mean_agg_discount.mean()

fig9 = go.Figure()

fig9.add_trace(go.Bar(
    x=Mean_agg_discount.values,
    y=Mean_agg_discount.index,
    orientation='h',
    marker=dict(
        color=Mean_agg_discount.values,
        colorscale='Viridis',
        showscale=True,
        colorbar=dict(title="Mean Discount")
    ),
    text=[f'{x:.0f}' for x in Mean_agg_discount.values],
    textposition='outside'
))

# Add cutoff line
fig9.add_shape(
    type="line",
    x0=cutoff_value_discount, x1=cutoff_value_discount,
    y0=-0.5, y1=len(Mean_agg_discount)-0.5,
    line=dict(color="black", width=2, dash="dash")
)

fig9.update_layout(
    title="Mean Discount of Each Brand",
    xaxis_title='Mean Discount (₹)',
    yaxis_title='Brands',
    width=1200,
    height=800
)

fig9.write_html("charts/mean_discount.html")

# 10. Top 5 Mobiles with Most Discount
print("Creating top discount mobiles chart...")
top_5_mobiles = df.sort_values("Discount", ascending=False).head(7)
top_5_mobiles = top_5_mobiles[['Mobile','Original Price','Discount']]
top_5_mobiles = top_5_mobiles.drop_duplicates().sort_values('Original Price', ascending=False)

fig10 = go.Figure()

fig10.add_trace(go.Bar(
    name='Original Price',
    x=top_5_mobiles['Mobile'],
    y=top_5_mobiles['Original Price'],
    marker_color='crimson'
))

fig10.add_trace(go.Bar(
    name='Discount',
    x=top_5_mobiles['Mobile'],
    y=top_5_mobiles['Discount'],
    marker_color='purple'
))

fig10.update_layout(
    title='Top 5 Mobiles by Discount',
    xaxis_title='Mobile',
    yaxis_title='Price (₹)',
    xaxis=dict(tickangle=45),
    barmode='group',
    width=1000,
    height=800
)

fig10.write_html("charts/top_discount_mobiles.html")

# 11. Total Revenue by Brand
print("Creating revenue chart...")
Agg_sp = df.groupby('Brands')['Selling Price'].value_counts().reset_index()
Agg_sp['Aggregate_SP'] = Agg_sp['Selling Price'] * Agg_sp['count']
revenue = Agg_sp.groupby('Brands')['Aggregate_SP'].sum().sort_values(ascending=False)

fig11 = go.Figure(data=[
    go.Bar(
        x=revenue.index,
        y=revenue.values,
        marker_color=px.colors.sequential.Plasma[:len(revenue)],
        text=[f'{x:,.0f}' for x in revenue.values],
        textposition='outside'
    )
])

fig11.update_layout(
    title="Total Revenue Generated by Each Brand",
    xaxis_title='Brands',
    yaxis_title='Revenue (₹)',
    xaxis=dict(tickangle=45),
    width=1200,
    height=800
)

fig11.write_html("charts/total_revenue.html")

print("All charts generated successfully!")