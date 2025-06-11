import streamlit as st

# Inline discount logic
def calculate_discounted_price(base_price, promo_code):
    valid_codes = {
        "BPR1": 0.10
    }

    discount_rate = valid_codes.get(promo_code.upper(), 0)
    if discount_rate > 0:
        discounted_price = base_price * (1 - discount_rate)
        return round(discounted_price, 2), True
    else:
        return base_price, False

# UI begins
st.set_page_config(page_title="Recruiting Assistant", layout="centered")
st.title("🚀 Welcome to the Beyond Performance Recruiting Experience")

st.markdown("Begin your journey beyond performance. Choose your subscription level below.")

plans = {
    "Monthly": 30.00,
    "Yearly": 300.00
}

plan = st.selectbox("Select Your Subscription Plan:", list(plans.keys()))
base_price = plans[plan]

promo_code = st.text_input("Enter Promo Code (if any):").strip()
final_price, discount_applied = calculate_discounted_price(base_price, promo_code)

st.markdown("---")
st.subheader("💳 Payment Summary")
st.write(f"**Plan Chosen:** {plan}")
st.write(f"**Original Price:** ${base_price:.2f}")
if discount_applied:
    st.success(f"Promo code '{promo_code}' applied — 10% off!")
    st.write(f"**Discounted Price:** ${final_price:.2f}")
else:
    st.write(f"**Final Price:** ${final_price:.2f}")

if st.button("👉 Begin Beyond Performance Experience"):
    st.success("✅ You're all set! Let's take your recruiting to the next level.")
    st.balloons()
