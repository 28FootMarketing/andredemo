import streamlit as st

# ✅ Discount logic included directly here
def calculate_discounted_price(base_price, promo_code):
    valid_codes = {
        "BPR1": 0.10  # 10% discount
    }

    discount_rate = valid_codes.get(promo_code.upper(), 0)
    if discount_rate > 0:
        discounted_price = base_price * (1 - discount_rate)
        return round(discounted_price, 2), True
    else:
        return base_price, False

# ✅ Streamlit App UI
st.set_page_config(page_title="Recruiting Assistant", layout="centered")
st.title("🚀 Welcome to the Beyond Performance Recruiting Experience")

st.markdown("Begin your journey beyond performance. Fill out your information and choose your subscription plan below.")

# Athlete Information
st.subheader("👤 Athlete Info")
full_name = st.text_input("Full Name")
email = st.text_input("Email Address")
sport = st.selectbox("Primary Sport", [
    "Football", "Basketball", "Baseball", "Softball", "Soccer", "Track & Field", "Wrestling",
    "Volleyball", "Tennis", "Golf", "Swimming", "Lacrosse", "Field Hockey", "Gymnastics",
    "Cheerleading", "Esports", "Girls Flag Football", "Other"
])
graduation_year = st.selectbox("Graduation Year", [2025, 2026, 2027, 2028, 2029])

st.markdown("---")

# Subscription Plan
st.subheader("📦 Subscription Plan")
plans = {
    "Monthly": 30.00,
    "Yearly": 300.00
}
plan = st.selectbox("Select Your Plan:", list(plans.keys()))
base_price = plans[plan]

# Promo Code
promo_code = st.text_input("Enter Promo Code (if any):").strip()
final_price, discount_applied = calculate_discounted_price(base_price, promo_code)

# Payment Summary
st.markdown("---")
st.subheader("💳 Payment Summary")
st.write(f"**Plan Chosen:** {plan}")
st.write(f"**Original Price:** ${base_price:.2f}")
if discount_applied:
    st.success(f"Promo code '{promo_code}' applied — 10% off!")
    st.write(f"**Discounted Price:** ${final_price:.2f}")
else:
    st.write(f"**Final Price:** ${final_price:.2f}")

# Confirmation
if st.button("👉 Begin Beyond Performance Experience"):
    if full_name and email:
        st.success(f"✅ Thanks {full_name.split()[0]}, you're all set! Check your inbox at {email}.")
        st.balloons()
    else:
        st.error("Please complete all required fields (Full Name and Email).")
