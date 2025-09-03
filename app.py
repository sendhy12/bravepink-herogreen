import streamlit as st
from PIL import Image
import numpy as np

st.title("🇮🇩 Solidaritas Indonesia Filter")
st.write("Ubah fotomu jadi gaya warna hijau & pink sebagai bentuk solidaritas.")

uploaded_file = st.file_uploader("Upload Foto", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("L")  # ubah grayscale
    img_array = np.array(img)

    # definisi warna duotone (dari gambar contoh)
    dark_color = np.array([24, 71, 36])   # hijau gelap
    light_color = np.array([236, 93, 171]) # pink magenta

    # normalisasi pixel grayscale (0-255 -> 0-1)
    norm = img_array / 255.0
    # interpolasi linear antara hijau dan pink
    colored = (dark_color[None, None, :] * (1 - norm[..., None]) +
               light_color[None, None, :] * norm[..., None]).astype(np.uint8)

    result = Image.fromarray(colored)

    st.image(result, caption="Hasil Filter Solidaritas", use_column_width=True)

    # tombol download
    st.download_button(
        "Download Foto",
        data=result.tobytes(),
        file_name="solidaritas.png",
        mime="image/png"
    )
