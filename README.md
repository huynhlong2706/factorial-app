# 🧮 Factorial Calculator App

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Deployed](https://img.shields.io/badge/Deployed-Streamlit_Cloud-success?style=for-the-badge)

**Project 2 - AIO2025 Module 1 (Mục 4.3)**

*Ứng dụng Web tính giai thừa của một số tự nhiên, được tích hợp hệ thống xác thực người dùng cơ bản bằng tính năng Session State của Streamlit.*

[Live Demo](#-live-demo) • [Tính năng](#-tính-năng-nổi-bật) • [Cài đặt](#️-cài-đặt--chạy-trên-máy-cá-nhân)

---

## 🚀 Live Demo

Trải nghiệm ứng dụng thực tế tại đây: 

👉 **[Factorial Calculator App](https://factorial-app-3zsgsccqwxjxyqszk5mzlr.streamlit.app/)**

> 💡 **Gợi ý:** Sử dụng tài khoản `admin` hoặc các tên có trong file `user.txt` để đăng nhập

---

## ✨ Tính năng Nổi bật

### 🔐 Xác thực Người dùng (Authentication)
- Hệ thống đăng nhập dựa trên danh sách user trong `user.txt`
- Sử dụng `st.session_state` để quản lý phiên đăng nhập
- Chỉ user hợp lệ mới được truy cập chức năng tính toán

### 🧮 Thuật toán Đệ quy
- Tính toán giai thừa $n!$ chính xác
- Logic được tách riêng biệt trong module `factorial.py`
- Xử lý hiệu quả với số nguyên lớn

### 📦 Cấu trúc Module hóa
- Tách biệt code giao diện (`app.py`) và xử lý logic (`factorial.py`)
- Dễ dàng bảo trì và mở rộng tính năng

---

## ⚙️ Cài đặt & Chạy trên máy cá nhân

### 📋 Yêu cầu hệ thống
- Python 3.10 trở lên
- pip (Python package manager)
- Git

### 🚀 Các bước thực hiện

#### 1️⃣ Clone dự án về máy
```bash
git clone https://github.com/huynhlong2706/factorial-app.git
cd factorial-app
```

#### 2️⃣ Tạo môi trường ảo (Virtual Environment)

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**MacOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Cài đặt thư viện
```bash
pip install -r requirements.txt
```

#### 4️⃣ Chạy ứng dụng
```bash
streamlit run app.py
```

> 🌐 Ứng dụng sẽ tự động mở tại: **http://localhost:8501**

---

## 📂 Cấu trúc Thư mục
```
factorial-app/
│
├── 📄 app.py                  # Giao diện và luồng điều hướng Streamlit
├── 📄 factorial.py            # Module chứa hàm tính giai thừa
├── 👥 user.txt                # Danh sách tài khoản được phép đăng nhập
├── 📄 requirements.txt        # Dependencies
└── 📖 README.md               # Tài liệu dự án
```

---

## 🔧 Cách sử dụng

### 1. Đăng nhập
- Nhập username có trong file `user.txt`
- Click nút **Login**

### 2. Tính giai thừa
- Nhập số nguyên dương $n$
- Ứng dụng sẽ tính và hiển thị kết quả $n!$

### 3. Đăng xuất
- Click nút **Logout** để thoát phiên làm việc

---

## 🤝 Đóng góp

Mọi đóng góp đều được hoan nghênh! 

### Quy trình đóng góp:

1. 🍴 Fork dự án
2. 🌿 Tạo nhánh tính năng: `git checkout -b feature/AmazingFeature`
3. 💾 Commit thay đổi: `git commit -m 'Add some AmazingFeature'`
4. 📤 Push lên nhánh: `git push origin feature/AmazingFeature`
5. 🔃 Tạo Pull Request

---

## 📞 Liên hệ

**Tác giả:** Bùi Huỳnh Long

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:bhlong2706@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/huynhlong2706)

---

**Dự án được thực hiện trong khuôn khổ khóa học AI Engineer - AIO2025**

⭐ Nếu thấy dự án hữu ích, hãy cho một star nhé!