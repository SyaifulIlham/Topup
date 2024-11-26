import streamlit as st

def detail_page():
    st.title("Detail Transaksi")
    st.write("Berikut adalah detail transaksi Anda:")
    st.write(f"**UID**: {st.session_state['uid']}")
    st.write(f"**Metode Pembayaran**: {st.session_state['payment_method']}")
    st.write(f"**Jumlah Diamond**: {st.session_state['diamond_count']}")
    st.write(f"**Harga Diamond**: {st.session_state['diamond_price']}")
    st.write(f"**username**: {st.session_state['username']}")
    
    st.image("790d9db1-149f-4aca-a739-b3a489f7e33b.jpg",width=200)
    
    if st.button("Batal"):
        st.session_state["page"] = "form"