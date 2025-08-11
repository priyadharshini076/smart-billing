import streamlit as st
import requests

st.set_page_config(page_title="SmartBillCare", layout="centered")

st.title("🧾 SmartBillCare - Patient Billing Assistant")

# Input field for Patient ID
patient_id = st.text_input("Enter your Patient ID (e.g., P001):")

if st.button("Get Bill Details"):
    if not patient_id:
        st.warning("Please enter a Patient ID.")
    else:
        try:
            # Call the FastAPI backend
            url = f"http://127.0.0.1:8000/billing/{patient_id}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                
                if "error" in data:
                    st.error(data["error"])
                else:
                    st.success("Billing details retrieved successfully!")
                    st.write(f"**Name:** {data['name']}")
                    st.write(f"**Total Bill:** ₹{data['bill_total']}")
                    st.write(f"**Due Date:** {data['due_date']}")
                    
                    st.write("### Breakdown:")
                    breakdown = data["breakdown"]
                    for item, cost in breakdown.items():
                        st.write(f"- {item}: ₹{cost}")
            else:
                st.error("Something went wrong with the server.")

        except requests.exceptions.ConnectionError:
            st.error("⚠️ Cannot connect to backend. Is the FastAPI server running?")
