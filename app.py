import streamlit as st
from PIL import Image
import numpy as np
import io

# =============================
# Konfigurasi Halaman
# =============================
st.set_page_config(
    page_title="Solidaritas Indonesia Filter",
    page_icon="🇮🇩",
    layout="centered"
)

# =============================
# Judul
# =============================
st.title("🇮🇩 Solidaritas Indonesia Filter")
st.write("Ubah fotomu jadi gaya **hijau & pink** yang sedang tren di Indonesia sebagai bentuk solidaritas.")

# =============================
# Upload Foto
# =============================
uploaded_file = st.file_uploader("📷 Upload Foto", type=["jpg", "jpeg", "png"])

# =============================
# Proses Foto
# =============================
if uploaded_file is not None:
    # Buka gambar & konversi grayscale
    img = Image.open(uploaded_file).convert("L")
    img_array = np.array(img)

    # Warna duotone (sesuai gambar tren)
    dark_color = np.array([24, 71, 36])     # Hijau gelap
    light_color = np.array([236, 93, 171])  # Pink magenta

    # Normalisasi pixel (0–255 -> 0–1)
    norm = img_array / 255.0

    # Interpolasi linear hijau → pink
    colored = (dark_color[None, None, :] * (1 - norm[..., None]) +
               light_color[None, None, :] * norm[..., None]).astype(np.uint8)

    result = Image.fromarray(colored)

    # Tampilkan hasil
    st.image(result, caption="✨ Hasil Filter Solidaritas", use_container_width=True)

    # Simpan ke buffer untuk download
    buf = io.BytesIO()
    result.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Tombol download
    st.download_button(
        label="⬇️ Download Foto",
        data=byte_im,
        file_name="solidaritas.png",
        mime="image/png"
    )
