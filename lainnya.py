import streamlit as st
from form_beli.form_kebutuhan import pajak_kendaraan_form, listrik_form, air_form, internet_form

class KebutuhanBulanan:
    def __init__(self):
        self.image_path = "img/CS.PNG"
        self.payments = [
            {"name": "Tagihan Pajak Kendaraan", "icon": "https://cdn-icons-png.flaticon.com/512/1995/1995575.png"},
            {"name": "Tagihan Listrik", "icon": "https://karir.nativeindonesia.com/wp-content/uploads/2024/11/Logo_PLN.png"},
            {"name": "Tagihan Air", "icon": "https://cdn-icons-png.flaticon.com/512/126/126601.png"},
            {"name": "Tagihan Internet", "icon": "https://cdn-icons-png.flaticon.com/512/3062/3062634.png"}
        ]
        
    def run(self):
        self.show_header()
        st.title("Pembayaran Kebutuhan Bulanan")
        self.display_payment_choices()  # Call display_payment_choices here
        # Check if form is open and display accordingly
        self.show_payment_form()

    def show_header(self):
        st.image(self.image_path, use_container_width=True)

    def display_payment_choices(self):
        st.markdown("### Pilih Pembayaran:")
        for idx, payment in enumerate(self.payments):
            self.show_payment_button(payment, idx)

    def show_payment_button(self, payment, idx):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.image(payment["icon"], width=100, use_container_width=True)
        with col2:
            st.markdown(f"#### {payment['name']}")
            st.markdown("##### ✨ Proses Pembayaran Cepat & Mudah!")
        with col3:
            # Update session state when a button is clicked
            if st.button(f"Bayar {payment['name']}", key=f"bayar_{idx}"):
                st.session_state.selected_payment = payment["name"]  # Store selected payment
                st.session_state.payment_form_open = True  # Mark the form as open

    def show_payment_form(self):
        if "selected_payment" in st.session_state and st.session_state.selected_payment:
            payment_name = st.session_state.selected_payment
            st.markdown(f"### Form Pembayaran untuk {payment_name}")

            if payment_name == "Tagihan Pajak Kendaraan":
                data = pajak_kendaraan_form()
            elif payment_name == "Tagihan Listrik":
                data = listrik_form()
            elif payment_name == "Tagihan Air":
                data = air_form()
            elif payment_name == "Tagihan Internet":
                data = internet_form()
            else:
                data = None

            if data:
                if "purchase_history" not in st.session_state:
                    st.session_state.purchase_history = []
                st.session_state.purchase_history.append(
                    {
                        "jenis": "kebutuhan",
                        **data,
                    }
                )
            st.success("Pembayaran berhasil disimpan ke riwayat!")

if "selected_payment" not in st.session_state:
    st.session_state.selected_payment = None
if "payment_form_open" not in st.session_state:
    st.session_state.payment_form_open = False

app = KebutuhanBulanan()
app.run()
