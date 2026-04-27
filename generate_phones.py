import json
import re

brands_data = {
    "Apple": [
        ("iPhone 17 Pro Max", "Brand New", "256GB", 3800000, "apple-iphone-17-pro-max.jpg"),
        ("iPhone 17 Pro", "Brand New", "256GB", 3400000, "apple-iphone-17-pro.jpg"),
        ("iPhone 17 Plus", "Brand New", "256GB", 2800000, "apple-iphone-17-plus.jpg"),
        ("iPhone 17", "Brand New", "128GB", 2400000, "apple-iphone-17.jpg"),
        ("iPhone 16 Pro Max", "UK Used", "256GB", 2500000, "apple-iphone-16-pro-max.jpg"),
        ("iPhone 16 Pro", "UK Used", "128GB", 2100000, "apple-iphone-16-pro.jpg"),
        ("iPhone 16 Plus", "UK Used", "128GB", 1800000, "apple-iphone-16-plus.jpg"),
        ("iPhone 16", "UK Used", "128GB", 1500000, "apple-iphone-16.jpg"),
        ("iPhone 15 Pro Max", "UK Used", "256GB", 1450000, "apple-iphone-15-pro-max.jpg"),
        ("iPhone 15 Pro", "UK Used", "128GB", 1250000, "apple-iphone-15-pro.jpg"),
        ("iPhone 15 Plus", "UK Used", "128GB", 1000000, "apple-iphone-15-plus.jpg"),
        ("iPhone 15", "UK Used", "128GB", 900000, "apple-iphone-15.jpg"),
        ("iPhone 14 Pro Max", "UK Used", "256GB", 1100000, "apple-iphone-14-pro-max.jpg"),
        ("iPhone 14 Pro", "UK Used", "128GB", 900000, "apple-iphone-14-pro.jpg"),
        ("iPhone 13", "UK Used", "128GB", 500000, "apple-iphone-13.jpg")
    ],
    "Samsung": [
        ("Galaxy S26 Ultra", "Brand New", "256GB", 3400000, "samsung-galaxy-s26-ultra.jpg"),
        ("Galaxy S26+", "Brand New", "256GB", 2800000, "samsung-galaxy-s26-plus.jpg"),
        ("Galaxy S26", "Brand New", "128GB", 2100000, "samsung-galaxy-s26.jpg"),
        ("Galaxy Z Fold 7", "Brand New", "512GB", 3600000, "samsung-galaxy-z-fold7.jpg"),
        ("Galaxy Z Flip 7", "Brand New", "256GB", 2400000, "samsung-galaxy-z-flip7.jpg"),
        ("Galaxy S25 Ultra", "UK Used", "256GB", 2200000, "samsung-galaxy-s25-ultra.jpg"),
        ("Galaxy S25+", "UK Used", "256GB", 1700000, "samsung-galaxy-s25-plus.jpg"),
        ("Galaxy S25", "UK Used", "128GB", 1300000, "samsung-galaxy-s25.jpg"),
        ("Galaxy A56 5G", "Brand New", "128GB", 700000, "samsung-galaxy-a56.jpg"),
        ("Galaxy A36 5G", "Brand New", "128GB", 550000, "samsung-galaxy-a36.jpg"),
        ("Galaxy S24 Ultra", "UK Used", "256GB", 1450000, "samsung-galaxy-s23-ultra-5g.jpg"),
        ("Galaxy S24", "UK Used", "128GB", 1100000, "samsung-galaxy-s24.jpg"),
        ("Galaxy A55 5G", "Brand New", "128GB", 580000, "samsung-galaxy-a55.jpg"),
        ("Galaxy A35 5G", "Brand New", "128GB", 480000, "samsung-galaxy-a35.jpg"),
        ("Galaxy A15", "Brand New", "128GB", 215000, "samsung-galaxy-a15.jpg")
    ],
    "Tecno": [
        ("Phantom Ultimate 2", "Brand New", "512GB", 1800000, "tecno-phantom-ultimate.jpg"),
        ("Phantom V Fold 3", "Brand New", "512GB", 1600000, "tecno-phantom-v-fold2.jpg"),
        ("Camon 40 Premier", "Brand New", "512GB", 1100000, "tecno-camon-40-premier.jpg"),
        ("Camon 40 Pro", "Brand New", "256GB", 800000, "tecno-camon-40-pro.jpg"),
        ("Camon 40", "Brand New", "256GB", 600000, "tecno-camon-40.jpg"),
        ("Spark 40 Pro", "Brand New", "256GB", 350000, "tecno-spark-40-pro.jpg"),
        ("Spark 40", "Brand New", "128GB", 250000, "tecno-spark-40.jpg"),
        ("Pova 7 Pro", "Brand New", "256GB", 450000, "tecno-pova-7-pro.jpg"),
        ("Phantom X2 Pro", "Brand New", "256GB", 750000, "tecno-phantom-x2-pro.jpg"),
        ("Camon 30 Premier", "Brand New", "512GB", 615000, "tecno-camon-30-premier.jpg"),
        ("Camon 30 Pro", "Brand New", "256GB", 480000, "tecno-camon-30-pro.jpg"),
        ("Spark 30 Pro", "Brand New", "256GB", 280000, "tecno-spark-30-pro.jpg"),
        ("Spark 30C", "Brand New", "128GB", 145000, "tecno-spark-20c.jpg"),
        ("Pova 6 Pro", "Brand New", "256GB", 320000, "tecno-pova-6-pro.jpg"),
        ("Pop 12", "Brand New", "64GB", 120000, "tecno-pop-11.jpg")
    ],
    "Infinix": [
        ("Zero 50 Ultra", "Brand New", "512GB", 1300000, "infinix-zero-50-ultra.jpg"),
        ("Zero 50 Pro", "Brand New", "256GB", 900000, "infinix-zero-50-pro.jpg"),
        ("Note 60 Pro+", "Brand New", "256GB", 650000, "infinix-note-60-pro-plus.jpg"),
        ("Note 60 Pro", "Brand New", "256GB", 500000, "infinix-note-60-pro.jpg"),
        ("Note 60", "Brand New", "256GB", 400000, "infinix-note-60.jpg"),
        ("Hot 60 Pro", "Brand New", "256GB", 300000, "infinix-hot-60-pro.jpg"),
        ("Hot 60", "Brand New", "128GB", 220000, "infinix-hot-60.jpg"),
        ("Smart 10", "Brand New", "128GB", 150000, "infinix-smart-10.jpg"),
        ("Zero 40 Pro", "Brand New", "256GB", 600000, "infinix-zero-40-pro.jpg"),
        ("Note 50 Pro+", "Brand New", "256GB", 520000, "infinix-note-40-pro-plus.jpg"),
        ("Note 50 Pro", "Brand New", "256GB", 380000, "infinix-note-30-pro.jpg"),
        ("Note 50", "Brand New", "128GB", 280000, "infinix-note-40.jpg"),
        ("Hot 50 Pro", "Brand New", "128GB", 230000, "infinix-hot-50-pro.jpg"),
        ("Hot 50", "Brand New", "128GB", 180000, "infinix-hot-50.jpg"),
        ("Smart 8", "Brand New", "64GB", 118000, "infinix-smart-8.jpg")
    ],
    "Xiaomi": [
        ("Xiaomi 16 Ultra", "Brand New", "512GB", 2100000, "xiaomi-16-ultra.jpg"),
        ("Xiaomi 16 Pro", "Brand New", "256GB", 1600000, "xiaomi-16-pro.jpg"),
        ("Xiaomi 16", "Brand New", "256GB", 1200000, "xiaomi-16.jpg"),
        ("Redmi Note 15 Pro+", "Brand New", "256GB", 550000, "xiaomi-redmi-note-15-pro-plus.jpg"),
        ("Redmi Note 15 Pro", "Brand New", "256GB", 450000, "xiaomi-redmi-note-15-pro.jpg"),
        ("Redmi Note 15", "Brand New", "128GB", 300000, "xiaomi-redmi-note-15.jpg"),
        ("Poco F7 Pro", "Brand New", "512GB", 800000, "xiaomi-poco-f7-pro.jpg"),
        ("Poco F7", "Brand New", "256GB", 600000, "xiaomi-poco-f7.jpg"),
        ("Poco X7 Pro", "Brand New", "256GB", 450000, "xiaomi-poco-x7-pro.jpg"),
        ("Xiaomi 15 Ultra", "UK Used", "512GB", 1400000, "xiaomi-15-ultra.jpg"),
        ("Xiaomi 15 Pro", "UK Used", "256GB", 1100000, "xiaomi-15-pro.jpg"),
        ("Xiaomi 15", "UK Used", "256GB", 900000, "xiaomi-15.jpg"),
        ("Redmi Note 13 Pro", "Brand New", "256GB", 350000, "xiaomi-redmi-note-13-pro-4g.jpg"),
        ("Redmi 14C", "Brand New", "128GB", 160000, "xiaomi-redmi-14c.jpg"),
        ("Redmi 13C", "Brand New", "128GB", 155000, "xiaomi-redmi-13c.jpg")
    ],
    "Google Pixel": [
        ("Pixel 10 Pro XL", "Brand New", "512GB", 2500000, "google-pixel-10-pro-xl.jpg"),
        ("Pixel 10 Pro", "Brand New", "256GB", 2100000, "google-pixel-10-pro.jpg"),
        ("Pixel 10", "Brand New", "128GB", 1600000, "google-pixel-10.jpg"),
        ("Pixel 10a", "Brand New", "128GB", 900000, "google-pixel-10a.jpg"),
        ("Pixel 9 Pro Fold", "Brand New", "512GB", 3200000, "google-pixel-9-pro-fold.jpg"),
        ("Pixel 9 Pro XL", "UK Used", "256GB", 1600000, "google-pixel-9-pro-xl.jpg"),
        ("Pixel 9 Pro", "UK Used", "256GB", 1300000, "google-pixel-9-pro.jpg"),
        ("Pixel 9", "UK Used", "128GB", 1000000, "google-pixel-9.jpg"),
        ("Pixel 8a", "Brand New", "128GB", 600000, "google-pixel-8a.jpg"),
        ("Pixel 8 Pro", "UK Used", "256GB", 850000, "google-pixel-8-pro.jpg"),
        ("Pixel 8", "UK Used", "128GB", 650000, "google-pixel-8.jpg"),
        ("Pixel Fold 2", "UK Used", "256GB", 1500000, "google-pixel-fold-2.jpg"),
        ("Pixel 7 Pro", "UK Used", "128GB", 500000, "google-pixel-7-pro.jpg"),
        ("Pixel 7", "UK Used", "128GB", 400000, "google-pixel-7.jpg"),
        ("Pixel 7a", "UK Used", "128GB", 320000, "google-pixel-7a.jpg")
    ],
    "Oppo": [
        ("Find X8 Ultra", "Brand New", "512GB", 2200000, "oppo-find-x8-ultra.jpg"),
        ("Find X8 Pro", "Brand New", "256GB", 1700000, "oppo-find-x8-pro.jpg"),
        ("Find X8", "Brand New", "256GB", 1300000, "oppo-find-x8.jpg"),
        ("Reno 13 Pro+", "Brand New", "256GB", 900000, "oppo-reno13-pro-plus.jpg"),
        ("Reno 13 Pro", "Brand New", "256GB", 700000, "oppo-reno13-pro.jpg"),
        ("Reno 13", "Brand New", "256GB", 500000, "oppo-reno13.jpg"),
        ("Find N4 Fold", "Brand New", "512GB", 2400000, "oppo-find-n4.jpg"),
        ("Find N4 Flip", "Brand New", "256GB", 1400000, "oppo-find-n4-flip.jpg"),
        ("Find X7 Ultra", "UK Used", "256GB", 1400000, "oppo-find-x7-ultra.jpg"),
        ("Find X7", "UK Used", "256GB", 900000, "oppo-find-x7.jpg"),
        ("Reno 12 Pro", "Brand New", "256GB", 600000, "oppo-reno12-pro.jpg"),
        ("Reno 12", "Brand New", "256GB", 400000, "oppo-reno12.jpg"),
        ("Reno 11", "UK Used", "256GB", 300000, "oppo-reno11.jpg"),
        ("Find X5 Pro", "UK Used", "256GB", 550000, "oppo-find-x5-pro.jpg"),
        ("A79", "Brand New", "128GB", 280000, "oppo-a79.jpg")
    ],
    "Huawei": [
        ("Mate 70 Pro+", "Brand New", "512GB", 2600000, "huawei-mate-70-pro-plus.jpg"),
        ("Mate 70 Pro", "Brand New", "256GB", 2000000, "huawei-mate-70-pro.jpg"),
        ("Mate 70", "Brand New", "256GB", 1500000, "huawei-mate-70.jpg"),
        ("Pura 80 Ultra", "Brand New", "512GB", 2700000, "huawei-pura-80-ultra.jpg"),
        ("Pura 80 Pro", "Brand New", "256GB", 2100000, "huawei-pura-80-pro.jpg"),
        ("Pura 80", "Brand New", "256GB", 1600000, "huawei-pura-80.jpg"),
        ("Nova 13 Pro", "Brand New", "256GB", 800000, "huawei-nova-13-pro.jpg"),
        ("Nova 13", "Brand New", "128GB", 500000, "huawei-nova-13.jpg"),
        ("Mate X4 Fold", "Brand New", "1TB", 3800000, "huawei-mate-x4.jpg"),
        ("Mate 60 Pro", "UK Used", "256GB", 1300000, "huawei-mate-60-pro.jpg"),
        ("Pura 70 Ultra", "UK Used", "512GB", 1600000, "huawei-pura-70-ultra.jpg"),
        ("Pura 70 Pro", "UK Used", "256GB", 1200000, "huawei-pura-70-pro.jpg"),
        ("Nova 12 Pro", "Brand New", "256GB", 600000, "huawei-nova-12-pro.jpg"),
        ("Nova 12", "Brand New", "128GB", 400000, "huawei-nova-12.jpg"),
        ("Mate 50 Pro", "Brand New", "256GB", 820000, "huawei-mate-50-pro.jpg")
    ]
}

lines = []
id_counter = 1
for brand, models in brands_data.items():
    for (model, cond, storage, price, img) in models:
        lines.append(f"            {{ id: {id_counter}, brand: '{brand}', model: '{model}', cond: '{cond}', storage: ['{storage}'], price: {price}, img: 'https://fdn2.gsmarena.com/vv/bigpic/{img}' }}")
        id_counter += 1

array_content = "        const products = [\n" + ",\n".join(lines) + "\n        ];"

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the const products = [ ... ]; block
start_marker = "const products = ["
end_marker = "        ];\n\n        const bundles"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker) + len("        ];")

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + array_content + content[end_idx:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Replaced successfully!")
else:
    print("Could not find blocks")
