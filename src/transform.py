


def transform_data(df):

    print("Transforming data...")

    #Remove duplicate Records
    df=df.drop_duplicates()

    print(type(df))

    #Remove rows where important values are missing
    df=df.dropna(subset=["order_id","product","quantity","price","city"])

    #Calculate total amount
    df["total_amount"]=df["quantity"] * df["price"]

    #product-wise sales
    product_sales=(
        df.groupby("product")["total_amount"].sum().sort_values(ascending=False)
    )

    #City-wise sales
    city_sales=(
        df.groupby("city")["total_amount"].sum().sort_values(ascending=False)
    )

    #Best Selling product
    best_product=product_sales.idxmax()

    #Highest sales city
    best_city=city_sales.idxmax()

    #Total sales
    total_sales=df["total_amount"].sum()

    summary={
        "total_sales": total_sales,
        "best_product": best_product,
        "best_city": best_city
    }

    return df, product_sales, city_sales,summary