import pandas as pd
# a. Đọc dữ liệu từ Excel
df_san_pham = pd.read_excel('DuLieuThucHanh2_V1.xlsx',sheet_name = 'San Pham')
df_nhan_vien = pd.read_excel('DuLieuThucHanh2_V1.xlsx',sheet_name = 'Nhan Vien')
df_hoa_don = pd.read_excel('DuLieuThucHanh2_V1.xlsx',sheet_name = 'Hoa Don')
df_thong_tin = pd.read_excel('DuLieuThucHanh2_V1.xlsx',sheet_name = 'Thong Tin Hoa Don')
# Hiển thị DataFrames
print(df_san_pham)
print(df_nhan_vien)
print(df_hoa_don)
print(df_thong_tin)
# b. Tạo DataFrame mới với số lượng sản phẩm đã bán
df_ban_hang = df_thong_tin.groupby('ID San Pham')['So Luong'].sum().reset_index()
df_ban_hang = df_ban_hang.merge(df_san_pham[['ID San Pham', 'Ten']], on='ID San Pham')
print(df_ban_hang)
# Sản phẩm bán chạy nhất
best_selling = df_ban_hang[df_ban_hang['So Luong'] == df_ban_hang['So Luong'].max()]
print(best_selling)