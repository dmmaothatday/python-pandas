import pandas as pd

# a.
# Đọc dữ liệu từ Excel
df_san_pham = pd.read_excel('DuLieuThucHanh2_V1.xlsx', sheet_name='San Pham')
df_nhan_vien = pd.read_excel('DuLieuThucHanh2_V1.xlsx', sheet_name='Nhan Vien')
df_hoa_don = pd.read_excel('DuLieuThucHanh2_V1.xlsx', sheet_name='Hoa Don')
df_thong_tin = pd.read_excel('DuLieuThucHanh2_V1.xlsx', sheet_name='Thong Tin Hoa Don')
# Hiển thị DataFrames
print("")
print("--- Sản phẩm:")
print(df_san_pham)
print("")
print("--- Nhân viên:")
print(df_nhan_vien)
print("")
print("--- Hóa đơn:")
print(df_hoa_don)
print("")
print("--- Thông tin hóa đơn:")
print(df_thong_tin)
print("")

# b.
# Tạo DataFrame mới với số lượng sản phẩm đã bán
df_ban_hang = df_thong_tin.groupby('ID San Pham')['So Luong'].sum().reset_index()
df_ban_hang = df_ban_hang.merge(df_san_pham[['ID San Pham', 'Ten']], on='ID San Pham')
print("--- Số lượng sản phẩm đã bán:")
print(df_ban_hang)
print("")
# Sản phẩm bán chạy nhất
best_selling = df_ban_hang[df_ban_hang['So Luong'] == df_ban_hang['So Luong'].max()]
print("--- Sản phẩm bán chạy nhất:")
print(best_selling)
print("")

# c.
# Tính tổng doanh thu cửa hàng
df_doanh_thu = df_thong_tin.merge(df_san_pham[['ID San Pham', 'Gia']])
df_doanh_thu['Thanh Tien'] = df_doanh_thu['So Luong'] * df_doanh_thu['Gia']
df_doanh_thu = df_doanh_thu.groupby('ID Hoa Don')['Thanh Tien'].sum().reset_index()
tong_tien_tat_ca = df_doanh_thu['Thanh Tien'].sum()
dong_moi = pd.DataFrame({'ID Hoa Don': ['Tong Tien'], 'Thanh Tien': [tong_tien_tat_ca]})
df_doanh_thu = pd.concat([df_doanh_thu, dong_moi])
print("--- Tổng doanh thu cửa hàng:")
print(df_doanh_thu)
print("")

# d.
# Update lại số lượng sản phẩm ở df_san_pham sau khi trừ hết số lượng đã bán trong các hóa đơn
df_san_pham['So Luong'] = df_san_pham['So Luong'] - df_ban_hang['So Luong']
print("--- Số lượng sản phẩm sau khi trừ hết số lượng đã bán:")
print(df_san_pham)
print("")