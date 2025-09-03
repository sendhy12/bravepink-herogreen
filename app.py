import streamlit as st
from PIL import Image, ImageOps
import numpy as np

# =============================
# Fungsi untuk efek Brave Pink – Hero Green
# =============================
def brave_pink_hero_green(img):
    # Convert ke grayscale
    gray = ImageOps.grayscale(img)
    arr = np.array(gray)

    # Normalisasi (0 - 1)
    norm = arr / 255.0

    # Warna Brave Pink (magenta) dan Hero Green (neon hijau)
    pink = np.array([255, 105, 180])   # Hot Pink
    green = np.array([0, 255, 128])    # Neon Green

    # Linear interpolation: 0 → pink, 1 → green
    duotone = (1 - norm[..., None]) * pink + norm[..., None] * green
    duotone = duotone.astype(np.uint8)

    return Image.fromarray(duotone)

# =============================
# Streamlit UI
# =============================
st.set_page_config(page_title="Brave Pink – Hero Green Generator", layout="centered")

st.title("🩷💚 Brave Pink – Hero Green Generator")
st.write("Ubah fotomu ke gaya solidaritas **Brave Pink – Hero Green** 🇮🇩")

# Upload foto
uploaded_file = st.file_uploader("Upload foto", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.subheader("Foto Asli")
    st.image(img, use_container_width=True)

    # Proses efek
    result = brave_pink_hero_green(img)

    st.subheader("Foto Brave Pink – Hero Green")
    st.image(result, use_container_width=True)

    # Tombol download
    result.save("brave_pink_hero_green.png")
    with open("brave_pink_hero_green.png", "rb") as f:
        st.download_button("⬇️ Download Hasil", f, file_name="brave_pink_hero_green.png", mime="image/png")
