import importlib
import sheet_structure


class BinaryDataGenerator:

    def __init__(self):
        self.output_dir = "../binary_data/"
        self.pb_objects = []
        self.pb_module = None
        self.pb_class = None

    def set_output_dir(self, output_dir):
        self.output_dir = output_dir

    def generate(self, sheet, sheet_structure_obj):
        self.import_pb_module(sheet_structure_obj)
        for row in range(2, sheet.nrows):
            pb_object = self.pb_class()
            column_num = len(sheet_structure_obj.columns_name)
            for column in range(0, column_num):
                cell_value = sheet.cell_value(row, column)
                self.set_vaule_to_pb_object(pb_object, cell_value, row, column, sheet_structure_obj)
            self.pb_objects.append(pb_object)
        self.save_data_to_file(sheet_structure_obj.sheet_name)

    def import_pb_module(self, sheet_structure_obj):
        module_name = "pb." + sheet_structure_obj.sheet_name + "_pb2"
        self.pb_module = importlib.import_module(module_name)
        self.pb_class = getattr(self.pb_module, sheet_structure_obj.sheet_name)

    def set_vaule_to_pb_object(self, pb_object, cell_value, row, column, sheet_structure_obj):
        column_name = sheet_structure_obj.columns_name[column]
        column_value_type = sheet_structure_obj.column_name_2_type[column_name]

        if column_value_type & sheet_structure.CellType.ARRAY.value is sheet_structure.CellType.ARRAY.value:
            values = []
            if cell_value is not ";":
                values = cell_value.split(";")
            values_num = len(values)
            if values_num > 0:
                if values[values_num - 1] is "":
                    values = values[:values_num - 1]

            column_value_type -= sheet_structure.CellType.ARRAY.value
            value_list = getattr(pb_object, column_name)
            if column_value_type is sheet_structure.CellType.STRING.value:
                for value in values:
                    value_list.append(value)
            else:
                for value in values:
                    if value.isdigit():
                        value_list.append(int(value))
                    else:
                        print("cell config error, row:%d column:%d" % (row + 1, column + 1))
                        exit(0)
        else:
            if column_value_type is sheet_structure.CellType.STRING.value:
                setattr(pb_object, column_name, cell_value)
            else:
                if cell_value is not "":
                    setattr(pb_object, column_name, int(cell_value))
                else:
                    print("cell config error, row:%d column:%d" % (row + 1, column + 1))
                    exit(0)

    def save_data_to_file(self, sheet_name):
        file_name = self.output_dir + sheet_name + ".byte"
        file = open(file_name, "w")
        for pb_object in self.pb_objects:
            file.write(str(pb_object.SerializeToString()) + "\n")
        file.close()
