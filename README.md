
# 📱 Mobile Sales Analytics Dashboard

## 🚀 Project Workflow

1. **Data Collection & Cleaning**  
	- Source: `mobile_sales_dataset.csv`  
	- Removed duplicates and NaN values for a clean dataset (2,806 records, 17 brands)
2. **Exploratory Data Analysis (EDA)**  
	- Brand distribution, model counts, top mobiles, color trends, price, ratings, discounts
	- Interactive charts generated with Plotly (`generate_charts.py`)
3. **Insights Dashboard**  
	- All charts and insights are available in the `charts/` folder and visualized in `index.html`
4. **Price Prediction**  
	- ML models: Linear Regression, KNN, Polynomial Regression, Decision Tree, Random Forest, AdaBoost, Gradient Boosting, XGBoost  
	- Performance metrics: RMSE, R², etc. (see `price_prediction.ipynb`)
5. **Reporting**  
	- Key findings summarized in `Exploratory_Data_Analysis.pptx` and `mobile_sales_report.docx`

---

## 🌟 Key Insights

<table><tr>
<td>📊 <b>Dataset Overview</b><br>2,806 clean records, 17 brands</td>
<td>🏢 <b>Brand Leadership</b><br>Samsung leads in model count, Realme & Apple follow</td>
<td>💰 <b>Revenue Champion</b><br>Apple generates highest revenue (₹19.6M)</td>
<td>⭐ <b>Quality Ratings</b><br>Apple tops with 4.6, POCO & Nokia also excel</td>
</tr></table>

---

## 📈 Visualizations & Charts

- 🥧 **Brand-wise Distribution**: Samsung, Realme, Apple dominate market share
- 📈 **Number of Models by Brands**: Samsung produces most models
- 🎯 **Top Brands & Mobiles**: Dual donut chart for brand and top-selling models
- 🏆 **Top 10 Most Sold Mobiles**: Apple models dominate top spots
- 🍎 **Apple Model Distribution**: iPhone 11, 13 Pro Max are best sellers
- 🎨 **Top 10 Colors**: Black is most preferred color
- 💵 **Mean Selling Price by Brand**: Apple highest, followed by Google Pixel, IQOO
- ⭐ **Mean Ratings by Brand**: Brands above 4.0 are top performers
- 💸 **Mean Discount by Brand**: Discount trends across brands
- 🏷️ **Top Discount Mobiles**: Highest discounts highlighted
- 🏦 **Total Revenue by Brand**: Apple leads, followed by Samsung

All charts are interactive and available in the `charts/` folder. View the dashboard in `index.html` for a beautiful summary.

---

## 🤖 ML Price Prediction

Tested multiple ML models for price prediction:

| Model                | RMSE      | R² Score |
|----------------------|-----------|----------|
| Linear Regression    | 13,795    | 0.68     |
| KNN                  | 10,000+   | 0.80+    |
| Polynomial Regression| ~10,000   | 0.80+    |
| Decision Tree        | 7,714     | 0.90     |
| Random Forest        | 5,800     | 0.94     |
| AdaBoost             | 17,912    | 0.46     |
| Gradient Boosting    | 6,998     | 0.91     |
| XGBoost              | 5,503     | 0.95     |

Best performance: **XGBoost** and **Random Forest** (highest R², lowest RMSE)

---

## 📂 Project Structure

```
├── mobile_sales_dataset.csv         # Raw dataset
├── generate_charts.py              # Chart generation script
├── price_prediction.ipynb          # ML model notebook
├── charts/                         # Interactive HTML charts
├── index.html                      # Dashboard
├── README.md                       # This file
├── ...                             # Other assets & reports
```

---

## 🛠️ Tech Stack

- Python (Pandas, NumPy, Scikit-learn, Plotly)
- Jupyter Notebook
- HTML/CSS (Dashboard)

---

## 📬 Contact & Credits

Project by JoySarthak.  
For questions, reach out via GitHub.

---

<p align="center"><b>Made with ❤️ and Plotly for beautiful, interactive analytics!</b></p>
