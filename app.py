import streamlit as st
from factorial import fact
import os

# --- HÀM HỖ TRỢ ---
def load_users():
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding="utf-8") as f:
                # Đọc từng dòng, xóa khoảng trắng thừa và bỏ dòng trống
                users = [line.strip() for line in f.readlines() if line.strip()]
            return users
        else:
            st.error("Lỗi: Không tìm thấy file user.txt!")
            return []
    except Exception as e:
        st.error(f"Lỗi khi đọc file: {e}")
        return []


# --- CÁC TRANG GIAO DIỆN ---
def login_page():
    """Giao diện trang Đăng nhập"""
    st.header("Đăng nhập hệ thống")
    
    username = st.text_input("Nhập tên người dùng:", placeholder="Ví dụ: admin")
    
    if st.button("Đăng nhập"):
        if username:
            valid_users = load_users()
            if username in valid_users:
                # Đăng nhập thành công -> Lưu vào Session State
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Đăng nhập thành công!")
                st.rerun() # Tải lại trang để chuyển sang màn hình chính
            else:
                # Sai tên -> Chuyển sang trang chào hỏi (từ chối)
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning("Vui lòng nhập tên người dùng!")

def greeting_page():
    """Trang thông báo khi người dùng không có quyền"""
    st.title("Xin chào!")
    st.write(f"Chào bạn **{st.session_state.username}**.")
    st.error("Bạn không có tên trong danh sách được cấp quyền sử dụng tính năng này.")
    
    if st.button("Quay lại đăng nhập"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()

def factorial_calculator():
    """Trang tính toán chính (Chỉ hiện khi đã đăng nhập)"""
    st.title("Factorial Calculator")
    
    # Khu vực thông tin user & Đăng xuất
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info(f"Xin chào, **{st.session_state.username}**! Chúc bạn học tốt.")
    with col2:
        if st.button("Đăng xuất"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()

    st.divider()

    # Chức năng tính toán
    st.write("Nhập một số tự nhiên để tính giai thừa ($n!$):")
    
    # Giới hạn 900 vì đệ quy Python có giới hạn độ sâu (stack depth)
    number = st.number_input("Nhập số n:", min_value=0, max_value=900, value=5, step=1)

    if st.button("Tính kết quả"):
        with st.spinner("Đang tính toán..."):
            result = fact(number)
            st.success(f"Kết quả: **{number}! = {result}**")
            
            # Hiển thị số đầy đủ nếu nó quá dài
            if len(str(result)) > 20:
                st.expander("Xem chi tiết số đầy đủ").write(str(result))

# --- HÀM MAIN (Điều hướng) ---
def main():
    # 1. Khởi tạo trạng thái (Session State) nếu chưa có
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False

    # 2. Điều hướng trang
    if st.session_state.logged_in:
        factorial_calculator()      # Đã đăng nhập -> Vào trang tính
    elif st.session_state.show_greeting:
        greeting_page()             # Sai user -> Vào trang từ chối
    else:
        login_page()                # Chưa gì cả -> Vào trang login

if __name__ == "__main__":
    main()