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
    
    # Pisahkan channel warna hijau
    green_ch = image_source[:,:,1]
    
    # Membuat gambar baru hanya dengan channel hijau
    image_green = np.zeros_like(image_source)
    image_green[:,:,1] = green_ch
    
    # Simpan gambar channel hijau
    output_path = f"C:\\Users\\Lenovo\\Documents\\Ayang PCD\\hasil\\{name}_green_channel.jpeg"
    image.imwrite(output_path, image_green)
    
    print(f"Gambar Channel Hijau untuk {name} selesai disimpan di {output_path}")