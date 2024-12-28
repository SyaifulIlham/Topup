import streamlit as st

def mobile_legend_form():
    st.title("Ayo Top-up Mobile Legends")
    
    diamond_prices = {
        "10 Diamonds": 5000,
        "50 Diamonds": 75000,
        "75 Diamonds": 80000,
        "100 Diamonds": 120000,
        "150 Diamonds": 150000,
        "200 Diamonds": 200000,
        "300 Diamonds": 220000,
        "500 Diamonds": 250000,
        "750 Diamonds": 300000,
        "1000 Diamonds": 400000,
        "1500 Diamonds": 550000,
    }
    process_form("Mobile Legends", diamond_prices)

def free_fire_form():
    st.title("Ayo Top-up Free Fire")
    diamond_prices = {
        "100 Diamonds": 100000,
        "310 Diamonds": 200000,
        "520 Diamonds": 450000,
        "1000 Diamonds": 500000,
        "2000 Diamonds": 120000,
        "3000 Diamonds": 400000,
    }
    process_form("Free Fire", diamond_prices)

def pubg_form():
    st.title("Ayo Top-up PUBG Mobile")
    diamond_prices = {
        "60 UC": 10000,
        "180 UC": 50000,
        "600 UC": 120000,
        "1200 UC": 30000,
        "1800 UC": 65000,
    }
    process_form("PUBG Mobile", diamond_prices)

def valorant_form():
    st.title("Ayo Top-up Valorant")
    diamond_prices = {
        "525 VP": "mahal",
        "1150 VP": "mahal",
        "2300 VP": 200000,
        "4600 VP": 300000,
        "6500 VP": 1200000,
    }
    process_form("Valorant", diamond_prices)

def genshin_form():
    st.title("Ayo Top-up Genshin Impact")
    diamond_prices = {
        "60 Crystals": 50000,
        "300 Crystals": 100000,
        "980 Crystals": 120000,
        "1980 Crystals": 300000,
        "3280 Crystals": 650000,
    }
    process_form("Genshin Impact", diamond_prices)

def process_form(game_name, prices):
    
    name = st.text_input(f"Masukkan UID ({game_name})")
    username = st.text_input(f"Masukkan Username ({game_name})")

    
    payment_option = st.selectbox(
        "Pilih Metode Pembayaran",
        ("QRIS", "Gopay", "Dana", "Shopeepay", "BCA", "Mandiri"),
        index=0,
    )

    
    item = st.selectbox(
        "Pilih Jumlah Top-Up",
        ["Pilih Jumlah"] + list(prices.keys()),
        index=0,
    )

    
    jml_bl = st.number_input("Jumlah Beli", min_value=1, value=1)

    if item != "Pilih Jumlah":
        st.write(f"Harga Total: Rp {prices[item] * jml_bl:,}")

    if st.button(f"Submit Top-Up {game_name}"):
        if not username.strip():
            st.warning("Tolong isi username dahulu")
        elif item == "Pilih Jumlah":
            st.warning("Silakan pilih jumlah terlebih dahulu!")
        else:
            
            st.session_state["uid"] = name
            st.session_state["payment_method"] = payment_option
            st.session_state["item"] = item
            st.session_state["total_price"] = prices[item] * jml_bl
            st.session_state["username"] = username

            
            if "purchase_history" not in st.session_state:
                st.session_state["purchase_history"] = []
            st.session_state["purchase_history"].append({
                "game": game_name,
                "uid": name,
                "username": username,
                "item": item,
                "jumlah": jml_bl,
                "total_harga": prices[item] * jml_bl,
                "metode_pembayaran": payment_option,
            })

            
            st.write(
                f"UID: {name}, Username: {username}, Item: {item}, Harga Total: Rp {prices[item] * jml_bl:,}"
            )
            st.success(f"Top-up {game_name} berhasil!")

