import proto_generator
import xlrd
import os
from sheet_structure import SheetStructure
from binary_data_generator import BinaryDataGenerator

if __name__ == "__main__":
    work_book = xlrd.open_workbook("./table/hero.xlsx")
    sheet = work_book.sheet_by_index(0)

    sheet_structure_obj = SheetStructure()
    sheet_structure_obj.analyze_sheet(sheet, "hero")

    p_generator = proto_generator.ProtoGenerator()
    p_generator.set_output_dir("./proto/")
    p_generator.generate("TableProto", sheet_structure_obj)

    os.system("protoc -I=./proto --python_out=./pb ./proto/hero.proto")

    b_generator = BinaryDataGenerator()
    b_generator.generate(sheet, sheet_structure_obj)



