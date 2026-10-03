from src.extract import extract_data
from src.load import load_data
from src.transform import transform_data


def run_pipeline():

    print("=======================")
    print("SALES DATA ENGINEERING PIPELINE")
    print("=======================")

    #Extract
    df=extract_data(
        "data/raw/sales.csv"
    )

    #Transform
    df,product_sales,city_sales,summary=transform_data(df)

    #Load
    load_data(
        df,
        product_sales,
        city_sales,
        summary
    )

    #Report
    print("\n===== SALES REPORT=======")

    print("Total Sales:", summary["total_sales"])
    print("Best Selling product:", summary["best_product"])
    print("Highest Sales City:", summary["best_city"])

    print("\nProduct-wise Sales:")
    print(product_sales)

    print("\nCity-wise Sales:")
    print(city_sales)

    print("\nPipeline completed successfully!")

if __name__=="__main__":
    run_pipeline()


