import numpy as np
import imageio.v3 as image

paths = {
    "kenikir" : "C:\\Users\\Lenovo\\Documents\\Ayang PCD\\PCD SESII 2\\daun kenikir.jpg",
   "pepaya" : "C:\\Users\\Lenovo\\Documents\\Ayang PCD\\PCD SESII 2\\daun pepaya.jpg",
   "singkong": "C:\\Users\\Lenovo\Documents\\Ayang PCD\\PCD SESII 2\\daun singkong.jpeg"
}

for name, path in paths.items():
    # Membaca gambar
    image_source = image.imread(path)
    
    # Pisahkan channel warna biru
    blue_ch = image_source[:,:,2]
    
    # Membuat gambar baru hanya dengan channel biru
    image_blue = np.zeros_like(image_source)
    image_blue[:,:,2] = blue_ch
    
    # Simpan gambar channel biru
    output_path = f"C:\\Users\\Lenovo\\Documents\\Ayang PCD\\hasil\\{name}_blue_channel.jpeg"
    image.imwrite(output_path, image_blue)
    
    print(f"Gambar Channel Biru untuk {name} selesai disimpan di {output_path}")