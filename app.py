import streamlit as st
import locale

st.title("SIP CALCULATOR")

# M = P × ({[1 + i]^n – 1} / i) × (1 + i)
locale.setlocale(locale.LC_ALL, 'en_IN')

c1,c2 = st.columns(2)

with c2:
    with st.container():
        pt = st.number_input("int",label_visibility="hidden",placeholder="INR")
with c1:
    p = st.slider(label="Amount",min_value=500,max_value=1000000,value=int(pt)) 

c3,c4 = st.columns(2)

with c4:
    with st.container():
        rt = st.number_input(label="int",label_visibility="hidden",key=50,placeholder="%",min_value=1)
with c3:
    r = st.slider(label="RATE %",min_value=1,max_value=100,value=int(rt))


c5,c6 = st.columns(2)

with c6:
    with st.container():
        tt = st.number_input("int",label_visibility="hidden",key=55,placeholder="Yrs")
with c5:
    t = st.slider(label="TIME",min_value=1,max_value=50,value=int(tt)) 
    
r = r/1200
t = t*12

def ci(p,r,t):
    a = p * (((1 + r) ** t - 1) / r) * (1 + r)
    return a

final = ci(p,r,t)
final = locale.currency(final,grouping=True)

st.write(f"Final amount is: {final}")

