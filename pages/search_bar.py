import streamlit as st

# text를 입력하는 검색창을 하나 만듭니다.
# ani_list에 있는 글자가 일부라도 들어가면
# img_list에 있는 해당 그림이 출력되는 검색창을 하나 만들어주세요

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']


a = st.text_input("검색창")

if a != '':
    if a in '짱구는못말려':
        st.image(img_list[0])

    elif a in '몬스터':
        st.image(img_list[1])

    elif a in '릭앤모티':
        st.image(img_list[2])
    else:
        st.text("찾으시는 사진이 없습니다.")