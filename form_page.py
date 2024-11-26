import streamlit as st

def form_page():
    st.title("Ayo Top-up")
    st.write("Form Pemesanan Top Up Game")

    # Kamus harga diamond
    diamond_prices = {
        "10 Diamonds": 1000,
        "50 Diamonds": 5000,
        "75 Diamonds": 12000,
        "100 Diamonds": 30000,
        "150 Diamonds": 65000,
        "200 Diamonds": 80000,
        "300 Diamonds": 120000,
        "500 Diamonds": 150000,
        "750 Diamonds": 200000,
        "1000 Diamonds": 350000,
        "1500 Diamonds": 400000,
    }

    # Input dan Output
    name = st.text_input("Masukkan UID")
    option = st.selectbox(
        "Pilih Metode Pembayaran",
        ("QRIS", "Gopay", "Dana", "Shopeepay", "BCA", "Mandiri"),
        index=0,
    )
    
    # Pilihan jumlah diamond
    diamond = st.selectbox(
        "Pilih Jumlah Diamond",
        ["Pilih Jumlah Diamond"] + list(diamond_prices.keys()),  # Tambahkan pilihan default
        index=0,
    )

    if diamond != "Pilih Jumlah Diamond":
        st.write(f"Harga Diamond: Rp {diamond_prices[diamond]:,}")
        
    username = st.text_input("masukan username anda")

    
    if st.button("Submit"):
        if diamond == "Pilih Jumlah Diamond":
            st.warning("Silakan pilih jumlah diamond terlebih dahulu!")
        else:
            st.session_state["uid"] = name
            st.session_state["payment_method"] = option
            st.session_state["diamond_count"] = diamond
            st.session_state["diamond_price"] = diamond_prices[diamond]
            st.session_state["username"] = username
            st.session_state["page"] = "detail"
