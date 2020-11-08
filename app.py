import streamlit as st
import time

def main():
    st.title("My First App of Streamlite")
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'Iteration {i+1}')
      bar.progress(i + 1)
      time.sleep(0.1)
    '...and now we\'re done!'

if __name__=='__main__':
    main()

