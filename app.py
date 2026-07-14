import streamlit as st
from utils.authentication import init_auth_session, is_admin, is_authenticated
from utils.helpers import inject_custom_css

# 1. Page Configuration
st.set_page_config(
    page_title="RestaurantAI - AI Menu & Order Hub",
    page_icon="🍴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Initialize Session State
init_auth_session()
if "cart" not in st.session_state:
    st.session_state["cart"] = {}

# 3. Inject Elegant Theme Styles
inject_custom_css()

# 4. Define Pages
home_page = st.Page("pages/Home.py", title="Home", icon="🏠", default=True)
menu_page = st.Page("pages/Menu.py", title="Menu", icon="🍔")
cart_page = st.Page("pages/Cart.py", title="Cart", icon="🛒")
orders_page = st.Page("pages/Orders.py", title="Orders", icon="📦")
admin_page = st.Page("pages/Admin.py", title="Admin Panel", icon="🛠️")
about_page = st.Page("pages/About.py", title="About Us", icon="ℹ️")

# 5. Build Sidebar Navigation Groups
nav_structure = {
    "Discover": [home_page, menu_page, about_page],
    "Your Session": [cart_page, orders_page],
    "Administration": [admin_page]
}

# 6. Run Multi-Page Shell
pg = st.navigation(nav_structure)
pg.run()

# 7. Sidebar Footer Information
st.sidebar.markdown("---")
if is_authenticated():
    st.sidebar.success(f"Logged in: **{st.session_state['user_name']}** ({st.session_state['user_role'].capitalize()})")
    if st.sidebar.button("Logout", key="logout_sidebar_btn"):
        from utils.authentication import logout_user
        logout_user()
        st.toast("Logged out successfully!")
        st.rerun()
else:
    st.sidebar.info("👋 Welcome Guest! Sign in under **Cart** or **Admin** to place orders & manage items.")
st.sidebar.caption("© 2026 RestaurantAI. Powered by Streamlit.")
