Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
>>> import streamlit as st
... 
... # -----------------------------
... # E-commerce AI Agent Class
... # -----------------------------
... class EcommerceAgent:
...     def __init__(self):
...         self.product_db = []
...         self.purchase_channels = {}
...         self.market_insights = {}
...         self.profit_data = {}
... 
...     def find_high_volume_products(self, platform="amazon", category="kitchen"):
...         if platform == "amazon" and category == "kitchen":
...             products = [
...                 {"name": "Smart Air Fryer", "category": "kitchen", "monthly_sales": 3200},
...                 {"name": "Countertop Ice Maker", "category": "kitchen", "monthly_sales": 2100},
...                 {"name": "Electric Kettle with Temp Control", "category": "kitchen", "monthly_sales": 1900}
...             ]
...         elif platform == "amazon" and category == "beauty":
...             products = [
...                 {"name": "Revlon One-Step Hair Dryer", "category": "beauty", "monthly_sales": 5000},
...                 {"name": "Ceramic Curling Wand", "category": "beauty", "monthly_sales": 1500},
...                 {"name": "Facial Steamer", "category": "beauty", "monthly_sales": 1400}
...             ]
...         elif platform == "walmart" and category == "kitchen":
...             products = [
...                 {"name": "Touchscreen Air Fryer", "category": "kitchen", "monthly_sales": 2800},
...                 {"name": "Bullet Ice Maker", "category": "kitchen", "monthly_sales": 2200},
                {"name": "Compact Bread Machine", "category": "kitchen", "monthly_sales": 1600}
            ]
        elif platform == "walmart" and category == "beauty":
            products = [
                {"name": "Ionic Hair Dryer", "category": "beauty", "monthly_sales": 2100},
                {"name": "Mini Flat Iron", "category": "beauty", "monthly_sales": 1200},
                {"name": "Hair Volumizer Brush", "category": "beauty", "monthly_sales": 1100}
            ]
        else:
            products = []
        return products

    def find_purchase_sources(self, product_name):
        sources = [
            {"supplier": "Alibaba", "moq": 100, "unit_price": 20.0},
            {"supplier": "Global Sources", "moq": 200, "unit_price": 18.5},
            {"supplier": "US Distributor", "moq": 50, "unit_price": 23.0},
        ]
        self.purchase_channels[product_name] = sources
        return sources

    def estimate_profit(self, product_name, retail_price, cost, fees_percent=0.15, shipping_cost=5.0):
        fees = retail_price * fees_percent
        profit = retail_price - cost - fees - shipping_cost
        margin = (profit / retail_price) * 100 if retail_price > 0 else 0
        self.profit_data[product_name] = {
            "retail_price": retail_price,
            "cost": cost,
            "fees": fees,
            "shipping": shipping_cost,
            "profit": profit,
            "margin_percent": round(margin, 2)
        }
        return self.profit_data[product_name]

    def estimate_monthly_profit(self, product_name, monthly_sales):
        if product_name in self.profit_data:
            unit_profit = self.profit_data[product_name]["profit"]
            return round(unit_profit * monthly_sales, 2)
        return 0.0

# -----------------------------
# Streamlit App Starts Here
# -----------------------------
agent = EcommerceAgent()

st.set_page_config(page_title="Ecommerce AI Assistant", layout="wide")
st.title("🤖 E-commerce AI Assistant for Kitchen & Beauty Electronics")

col1, col2 = st.columns(2)
with col1:
    platform = st.selectbox("Select Platform", ["amazon", "walmart"])
with col2:
    category = st.selectbox("Select Category", ["kitchen", "beauty"])

products = agent.find_high_volume_products(platform=platform, category=category)

st.subheader(f"📈 Best Sellers ({category.title()}) on {platform.title()} - Sales > 1000/month")
product_names = [p["name"] for p in products]
selected_product = st.selectbox("Choose a product for analysis:", product_names)

if selected_product:
    product_data = next((p for p in products if p["name"] == selected_product), None)
    monthly_sales = product_data["monthly_sales"] if product_data else 1000

    st.markdown("### 🛒 Purchase Sources")
    sources = agent.find_purchase_sources(selected_product)
    st.table(sources)

    st.markdown("### 💰 Profit Estimate")
    retail_price = st.number_input("Retail Price", value=59.99)
    cost = sources[0]["unit_price"] if sources else 20.0
    profit_info = agent.estimate_profit(selected_product, retail_price, cost)
    st.json(profit_info)

    total_monthly_profit = agent.estimate_monthly_profit(selected_product, monthly_sales)
    st.success(f"📦 Est. Monthly Sales: {monthly_sales} units — 💵 Monthly Profit: ${total_monthly_profit}")
