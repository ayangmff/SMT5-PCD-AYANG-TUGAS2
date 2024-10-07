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
    
    # Pisahkan channel warna merah
    red_ch = image_source[:,:,0]
    
    # Membuat gambar baru hanya dengan channel merah
    image_red = np.zeros_like(image_source)
    image_red[:,:,0] = red_ch
    
    # Simpan gambar channel merah"
    output_path = f"C:\\Users\\Lenovo\\Documents\\Ayang PCD\\hasil\\{name}_red_channel.jpeg"
    image.imwrite(output_path, image_red)
    
    print(f"Gambar Channel Merah untuk {name} selesai disimpan di {output_path}")