import os

def load_data():
    pass

if __name__ == "__main__":
    cwd = os.getcwd()
    etf_dir = cwd + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "ETFs"
    stock_dir = cwd + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "Stocks"
    output_directory = cwd + os.path.sep + ".." + os.path.sep + "outputs" + os.path.sep
    poker_directory = None

#    stock.generate_enum___str__(stock_dir, output_directory)

    target_stock = None
    target_etf = None
