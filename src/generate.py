import proto_generator
import xlrd
import os
import configparser
from sheet_structure import SheetStructure
from binary_data_generator import BinaryDataGenerator


def table_to_proto_and_binary(file_path, proto_name, config):
    proto_dir = "../proto/"
    if config["Path"].get("ProtoDir"):
        proto_dir = config["Path"]["ProtoDir"]
    if not os.path.exists(proto_dir):
        os.makedirs(proto_dir)

    binary_data_dir = "../binary_data/"
    if config["Path"].get("BinaryDataDir"):
        binary_data_dir = config["Path"]["BinaryDataDir"]
    if not os.path.exists(binary_data_dir):
        os.makedirs(binary_data_dir)

    temp_pb_file_dir = "../pb/"
    if config["Path"].get("TempPbFileDir"):
        temp_pb_file_dir = config["Path"]["TempPbFileDir"]
    if not os.path.exists(temp_pb_file_dir):
        os.makedirs(temp_pb_file_dir)

    work_book = xlrd.open_workbook(file_path)
    sheet = work_book.sheet_by_index(0)

    sheet_structure_obj = SheetStructure()
    sheet_structure_obj.analyze_sheet(sheet, proto_name)

    p_generator = proto_generator.ProtoGenerator()
    p_generator.set_output_dir(proto_dir)
    p_generator.generate(proto_package, sheet_structure_obj)

    proto_file_path = proto_dir + proto_name + ".proto"
    command = "protoc -I=" + proto_dir + " --python_out=" + temp_pb_file_dir + " " + proto_file_path
    os.system(command)

    b_generator = BinaryDataGenerator()
    b_generator.set_output_dir(binary_data_dir)
    b_generator.generate(sheet, sheet_structure_obj)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("./config.ini")
    if not config.has_section("Path") or not config.has_section("ProtoConfig"):
        print("Error, don't have [Path] or [ProtoConfig]")
        exit(0)
    table_dir = config["Path"]["TableDir"]
    proto_package = config["ProtoConfig"]["Package"]

    for root, dirs, files in os.walk(table_dir):
        for name in files:
            file_path = os.path.join(root, name)
            print("Handling ", file_path)
            proto_name = name[:name.find(".")]
            table_to_proto_and_binary(file_path, proto_name, config)




