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
    
    # Konversi ke grayscale menggunakan rumus luminance
    grayscale_image = np.dot(image_source[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
    
    # Simpan gambar grayscale
    output_path = f"C:\\Users\\Lenovo\\Documents\\Ayang PCD\\hasil\\{name}_grayscale.jpeg"
    image.imwrite(output_path, grayscale_image)
    
    print(f"Gambar Grayscale untuk {name} selesai disimpan di {output_path}")