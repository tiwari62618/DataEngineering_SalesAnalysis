def load_data(
        df,
        product_sales,
        city_sales,
        summary
):

    print("Loading processed data...")

    #Save cleaned sales data
    df.to_csv(
        "data/processed/cleaned_sales.csv",
        index=False
    )

    #Create summary
    with open(
        "data/processed/sales_summary.csv",
        "w"
    )as file:
        file.write("Metric,Value\n")
        file.write(f"Total Sales,{summary['total_sales']}\n")
        file.write(f"Best Product,{summary['best_product']}\n")
        file.write(f"Best City,{summary['best_city']}\n")

    print("Data loaded successfully.")
