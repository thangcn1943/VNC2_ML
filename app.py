import streamlit as st
import preprocess_data
import pickle
import os
import time
import numpy as np


name_result = {
    'Am nhac': 'Âm nhạc',
    'Am thuc': 'Ẩm thực',
    'Bat dong san': 'Bất động sản',
    'Bong da': 'Thể thao',
    'Chung khoan': 'Chứng khoán',
    'Cum ga': 'Cúm gà',
    'Cuoc song do day': 'Cuộc sống đó đây',
    'Du hoc': 'Du học',
    'Du lich': 'Du lịch',
    'Duong vao WTO': 'Đường vào WTO',
    'Gia dinh': 'Gia đình',
    'Giai tri tin hoc': 'Giải trí tin học',
    'Giao duc': 'Giáo dục',
    'Gioi tinh': 'Giới tính',
    'Hackers va Virus': 'Hackers và Virus',
    'Hinh su': 'Hình sự',
    'Khong gian song': 'Không gian sống',
    'Kinh doanh quoc te': 'Kinh doanh quốc tế',
    'Kinh te': 'Kinh tế',
    'Lam dep': 'Làm đẹp',
    'Loi song': 'Lối sống',
    'Mua sam': 'Mua sắm',
    'My thuat': 'Mỹ thuật',
    'San khau dien anh': 'Sân khấu điện ảnh',
    'San pham tin hoc moi': 'Sản phẩm tin học mới',
    'Suc khoe': 'Sức khỏe',
    'Tennis': 'Thể thao',
    'The gioi tre': 'Thế giới trẻ',
    'Thoi trang': 'Thời trang',
    'Xe co': 'Xe cộ',
}

st.write("VietNamese Newspaper Classification")
#knn_model = pickle.load(open('data/saved/knn_model.sav','rb'))
lreg_model = pickle.load(open('data/saved/lreg_model.sav','rb'))
#mnb_model = pickle.load(open('data/saved/mnb_model.sav','rb'))
feature_extractor = pickle.load(open('data/saved/feature_extractor.sav', 'rb'))

news = st.text_area("Nhap du lieu moi vao day")
if news:

    # Tiền xử lý và loại bỏ stopwords
    start = time.time()
    data = preprocess_data.preprocess(news)
    data = preprocess_data.remove_stopwords(data)
    preprocess_time = time.time() - start

        # Dự đoán
    start = time.time()
    np_data = np.array([data])
    feature = feature_extractor.transform(np_data)
    #pred = knn_modelmodel.predict(feature)
    pred = lreg_model.predict(feature)
    result = name_result[pred[0]]
    predict_time = time.time() - start

    total = round(predict_time + preprocess_time, 2)
        # Hiện kết quả
    st.text('Kết quả: ' + result)
    st.text('Time: ' + str(total) + 's')
    #st.text('Data preprocessed: ' + data)
