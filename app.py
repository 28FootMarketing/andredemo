import streamlit as st
from utils.pricing import calculate_discounted_price

# ✅ Basic Setup
st.set_page_config(page_title="Recruiting Assistant", layout="centered")
st.title("🚀 Welcome to the Beyond Performance Recruiting Experience")

st.markdown("Begin your journey beyond performance. Choose your subscription level below.")

# ✅ Subscription Options
plans = {
    "Monthly": 30.00,
    "Yearly": 300.00
}

# User selects a plan
plan = st.selectbox("Select Your Subscription Plan:", list(plans.keys()))
base_price = plans[plan]

# Promo Code Input
promo_code = st.text_input("Enter Promo Code (if any):").strip()

# Calculate discounted price
final_price, discount_applied = calculate_discounted_price(base_price, promo_code)

# Display Pricing Summary
st.markdown("---")
st.subheader("💳 Payment Summary")
st.write(f"**Plan Chosen:** {plan}")
st.write(f"**Original Price:** ${base_price:.2f}")
if discount_applied:
    st.success(f"Promo code '{promo_code}' applied — 10% off!")
    st.write(f"**Discounted Price:** ${final_price:.2f}")
else:
    st.write(f"**Final Price:** ${final_price:.2f}")

# Continue Button
if st.button("👉 Begin Beyond Performance Experience"):
    st.success("✅ You're all set! Let's take your recruiting to the next level.")
    st.balloons()
