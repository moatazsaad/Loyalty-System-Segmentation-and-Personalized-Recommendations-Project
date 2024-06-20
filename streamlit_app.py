
import streamlit as st
import pandas as pd

# Read the clustered data and pivot table
df = pd.read_csv("Clustered_data.csv")
pivot_total = pd.read_csv("Clustered_pivot.csv")

def get_recommendations(user_id, num_recommendations):
    # Check if the user exists in the data
    if df["User_Id"].isin([int(user_id)]).any():
        # Get the cluster assigned to the user
        cluster = df.loc[df["User_Id"] == int(user_id), "Cluster"].unique()[0]

        # Filter the data for the user's cluster and calculate the sum of transaction values
        recommendations = df.loc[df["Cluster"] == cluster].groupby("Mer_Id")["Trx_Vlu"].sum().nlargest(int(num_recommendations))

        return recommendations
    else:
        return None

def main():
    # Set the title and header of the Streamlit app
    st.set_page_config(page_title="Loyalty Rewards: Personalized Recommendations", page_icon="🎁")
    st.title("🎁 Loyalty Rewards: Personalized Recommendations")
    st.header("Discover Merchants You'll Love!")

    # User input for user ID and number of recommendations
    st.sidebar.header("Input Parameters")
    user_id = st.sidebar.text_input("Enter User ID")
    num_recommendations = st.sidebar.number_input("Enter Number of Recommendations", min_value=1, max_value=20, value=5)

    # Button to trigger recommendation generation
    if st.sidebar.button("Recommend"):
        with st.spinner("Generating recommendations..."):
            recommendations = get_recommendations(user_id, num_recommendations)

        # Check if the user exists
        if recommendations is not None:
            st.success(f"Top {num_recommendations} Recommendations for User ID {user_id}")
            st.write(recommendations.reset_index().rename(columns={"Mer_Id": "Merchant ID", "Trx_Vlu": "Total Transaction Value"}))
        else:
            st.error("User not found. Please enter a valid User ID.")

    # Display pivot table for context (optional)
    with st.expander("Show Pivot Table Summary"):
        st.subheader("Clustered Pivot Table Summary")
        st.write(pivot_total)

# Run the main function
if __name__ == "__main__":
    main()
