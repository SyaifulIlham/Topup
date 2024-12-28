import streamlit as st

def pajak_kendaraan_form():
    st.title("Pembayaran Pajak Kendaraan")
    plat_nomor = st.text_input("Masukkan Nomor Plat Kendaraan")
    amount = st.number_input("Jumlah Tagihan Pajak Kendaraan", min_value=0, value=1000000)
    payment_option = st.selectbox("Pilih Metode Pembayaran", ["QRIS", "Gopay", "Dana", "Shopeepay", "BCA", "Mandiri"])

    if st.button("Bayar Pajak Kendaraan", key="bayar_pajak_kendaraan"):
        st.session_state["plat_nomor"] = plat_nomor
        st.session_state["amount"] = amount
        st.session_state["payment_option"] = payment_option
        st.session_state["payment_name"] = "Pajak Kendaraan"
        
        # Menambahkan transaksi ke riwayat pembelian
        if "purchase_history" not in st.session_state:
            st.session_state.purchase_history = []
        st.session_state.purchase_history.append({
            "jenis_pembayaran": "Pajak Kendaraan",
            "nama_pengguna": plat_nomor,
            "total_harga": amount,
            "metode_pembayaran": payment_option,
            "id_transaksi": f"PK_{len(st.session_state.purchase_history) + 1}",  # ID Transaksi unik
        })
        
        st.success(f"Pembayaran Pajak Kendaraan untuk {plat_nomor} berhasil! Total: Rp {amount:,}")

def listrik_form():
    st.title("Pembayaran Tagihan Listrik")
    meteran = st.text_input("Masukkan Nomor Meteran")
    amount = st.number_input("Jumlah Tagihan Listrik", min_value=0, value=200000)
    payment_option = st.selectbox("Pilih Metode Pembayaran", ["QRIS", "Gopay", "Dana", "Shopeepay", "BCA", "Mandiri"])

    if st.button("Bayar Tagihan Listrik", key="bayar_tagihan_listrik"):
        st.session_state["meteran"] = meteran
        st.session_state["amount"] = amount
        st.session_state["payment_option"] = payment_option
        st.session_state["payment_name"] = "Tagihan Listrik"
        
        # Menambahkan transaksi ke riwayat pembelian
        if "purchase_history" not in st.session_state:
            st.session_state.purchase_history = []
        st.session_state.purchase_history.append({
            "jenis_pembayaran": "Tagihan Listrik",
            "nama_pengguna": meteran,
            "total_harga": amount,
            "metode_pembayaran": payment_option,
            "id_transaksi": f"TL_{len(st.session_state.purchase_history) + 1}",  # ID Transaksi unik
        })
        
        st.success(f"Pembayaran Listrik dengan meteran {meteran} berhasil! Total: Rp {amount:,}")

def air_form():
    st.title("Pembayaran Tagihan Air")
    meteran = st.text_input("Masukkan Nomor Meteran Air")
    amount = st.number_input("Jumlah Tagihan Air", min_value=0, value=100000)
    payment_option = st.selectbox("Pilih Metode Pembayaran", ["QRIS", "Gopay", "Dana", "Shopeepay", "BCA", "Mandiri"])

    if st.button("Bayar Tagihan Air", key="bayar_tagihan_air"):
        st.session_state["meteran"] = meteran
        st.session_state["amount"] = amount
        st.session_state["payment_option"] = payment_option
        st.session_state["payment_name"] = "Tagihan Air"
        
        # Menambahkan transaksi ke riwayat pembelian
        if "purchase_history" not in st.session_state:
            st.session_state.purchase_history = []
        st.session_state.purchase_history.append({
            "jenis_pembayaran": "Tagihan Air",
            "nama_pengguna": meteran,
            "total_harga": amount,
            "metode_pembayaran": payment_option,
            "id_transaksi": f"TA_{len(st.session_state.purchase_history) + 1}",  # ID Transaksi unik
        })
        
        st.success(f"Pembayaran Air dengan meteran {meteran} berhasil! Total: Rp {amount:,}")

def internet_form():
    st.title("Pembayaran Tagihan Internet")
    provider = st.text_input("Masukkan Nama Provider Internet")
    amount = st.number_input("Jumlah Tagihan Internet", min_value=0, value=300000)
    payment_option = st.selectbox("Pilih Metode Pembayaran", ["QRIS", "Gopay", "Dana", "Shopeepay", "BCA", "Mandiri"])

    if st.button("Bayar Tagihan Internet", key="bayar_tagihan_internet"):
        st.session_state["provider"] = provider
        st.session_state["amount"] = amount
        st.session_state["payment_option"] = payment_option
        st.session_state["payment_name"] = "Tagihan Internet"
        
        # Menambahkan transaksi ke riwayat pembelian
        if "purchase_history" not in st.session_state:
            st.session_state.purchase_history = []
        st.session_state.purchase_history.append({
            "jenis_pembayaran": "Tagihan Internet",
            "nama_pengguna": provider,
            "total_harga": amount,
            "metode_pembayaran": payment_option,
            "id_transaksi": f"TI_{len(st.session_state.purchase_history) + 1}",  # ID Transaksi unik
        })
        
        st.success(f"Pembayaran Internet dengan provider {provider} berhasil! Total: Rp {amount:,}")
