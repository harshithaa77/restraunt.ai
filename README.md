# RestaurantAI – AI-Powered Restaurant Menu Management System

RestaurantAI is a production-ready, highly interactive multi-page web application built with Python and Streamlit. Designed for modern dining spaces, it combines customer food ordering capabilities with full administrator inventory and state-of-the-art metrics tracking, powered by a local, thread-safe JSON database.

---

## Features

- **Dynamic Homepage**: Features visually striking hero banners, customer metrics, food categories, and immediate search routing.
- **Interactive Menu Catalog**: Offers detailed food cards featuring item images, categories, vegetarian indicators, star ratings, and real-time stock toggles. Includes filtration options for searches, price-sliders, dietary filters, and star bounds, with multiple sort algorithms.
- **Reactive Shopping Cart**: Displays orders dynamically with quantity increment/decrement controls, live subtotal calculations, automated 5% GST computation, and order placement.
- **Embedded Security & Authentication**: Implements secure user signups, sign-ins, and role-based access control. Pre-seeds default credentials for both guest customers and store managers.
- **Order Progression tracking**: Lists historical user receipts and active order cooking phases with status progression indicators. Allows instant downloads of formatted plain-text receipts.
- **Manager Administration Console**: 
  - **Dynamic Analytics**: Plotly visualization of revenues and item-specific sales totals.
  - **Live Order Status Controllers**: Ability to transition order phases from *Preparing* ➔ *Cooking* ➔ *Ready* ➔ *Delivered*.
  - **Inventory Management**: Forms to Add, Edit, Delete, or toggle availability of menu items, with direct support for custom food image uploads.
- **Responsive Layout**: Dark theme customization styling that is responsive and mobile-friendly.

---

## Folder Structure

```text
RestaurantAI/
│
├── app.py                  # Entry point for the multi-page application navigation
├── config.py               # Handles environment variables loading and project constants
│
├── pages/                  # Streamlit Multi-page files
│   ├── Home.py
│   ├── Menu.py
│   ├── Cart.py
│   ├── Orders.py
│   ├── Admin.py
│   └── About.py
│
├── utils/                  # Core modules
│   ├── database.py         # Thread-safe JSON load/save operations with locks
│   ├── authentication.py   # Secure password hashing and authentication sessions
│   ├── menu_manager.py     # Menu retrieval, CRUD, filtering and sorting
│   ├── order_manager.py    # Order validation, processing, and analytics
│   └── helpers.py          # Custom CSS injector, image loaders, receipt generators
│
├── assets/                 # Dynamic assets
│   ├── logo.png            # Generated application logo
│   ├── banner.png          # Wide hero image banner
│   ├── pizza.png           # Margherita pizza card image
│   ├── burger.png          # Gourmet burger card image
│   ├── dessert.png         # Lava cake dessert card image
│   ├── chinese.png         # Chinese noodles card image
│   └── style.css           # Custom CSS styling tokens and animation triggers
│
├── data/                   # Database store
│   ├── menu.json           # Stores menu items catalog
│   ├── orders.json         # Tracks orders database
│   └── users.json          # Keeps credentials database
│
├── .env                    # Local environment variables
├── .env.example            # Environment variables template
├── requirements.txt        # Package dependencies list
├── .gitignore              # Standard git exclusion patterns
└── README.md               # User documentation
```

---

## Installation & Setup

### Prerequisites

Ensure you have Python 3.9+ installed on your computer.

### Step 1: Clone or Copy the Project
Verify all directory structures align with the layout above.

### Step 2: Install Dependencies

Open a terminal in the project root directory and run:

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

1. Copy `.env.example` to create a new file named `.env`:
   ```bash
   cp .env.example .env
   ```
2. Populate the `.env` file with appropriate API key configurations. (The system contains standard defaults and works automatically with dummy values locally).

---

## Running the Project Locally

To run the Streamlit application, execute:

```bash
streamlit run app.py
```

This will automatically launch the web interface in your default browser at `http://localhost:8501`.

### Pre-seeded Credentials
- **Admin Access**:
  - **Username**: `admin`
  - **Password**: `admin123`
- **Customer Access**:
  - Register instantly inside the checkout panel on the **Cart** page.

---

## Deployment to Streamlit Community Cloud

This project is configured and ready for production deployment on **Streamlit Community Cloud**:

1. Push the code repository to GitHub (ensure `.env` is ignored by `.gitignore`).
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **New App**, select your repository, branch, and set `app.py` as the **Main file path**.
4. In **Advanced Settings**, paste the environment variables from your `.env` file under **Secrets** (e.g., `SECRET_KEY="your_value"`).
5. Click **Deploy!**

---

## Screenshots

*Place screenshot links or preview graphics here in production deployments.*

---

## License

This project is licensed under the MIT License.
