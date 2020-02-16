import os
from etf import etf
from stock import stock

def generate_etf_enums(etf_directory, output_directory):
    etf_files = [file for file in os.listdir(etf_directory) if os.path.isfile(os.path.join(etf_directory, file))]

    with open(output_directory + "etf_enums.txt", "w+") as file:
        for etf_file_enum, etf_file in enumerate(etf_files):
            file.write("ETF_{0} = {1}\n".format(etf_file.split(".")[0].upper(), etf_file_enum+1))

def generate_stock_enums(stock_directory, output_directory):
    stock_files = [file for file in os.listdir(stock_directory) if os.path.isfile(os.path.join(stock_directory, file))]

    with open(output_directory + "stock_enums.txt", "w+") as file:
        for stock_file_enum, stock_file in enumerate(stock_files):
            file.write("STOCK_{} = {}\n".format(stock_file.split(".")[0].upper(), stock_file_enum+1))

def load_data():
    pass

if __name__ == "__main__":
    cwd = os.getcwd()
    etf_dir = cwd + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "ETFs"
    stock_dir = cwd + os.path.sep + ".." + os.path.sep + "data" + os.path.sep + "Stocks"
    output_directory = cwd + os.path.sep + ".." + os.path.sep + "outputs" + os.path.sep

#    stock.generate_enum___str__(stock_dir, output_directory)

    target_stock = None
    target_etf = None
