import os

from sheet_structure import CellType


class ProtoGenerator:

    def __init__(self):
        self.output_dir = "../proto/"
        self.proto_package_name = ""
        self.sheet_structure_obj = None

        self.structure_template = 'syntax = "proto3";\n' \
                                  'package {package_name};\n' \
                                  '\n' \
                                  'message {proto_name} {\n'
        self.element_template = '    {specify_field}{type} {element_name} = {order};\n'

    def set_output_dir(self, output_dir):
        self.output_dir = output_dir

    def generate(self, proto_package_name, sheet_structure_obj):
        self.proto_package_name = proto_package_name
        self.sheet_structure_obj = sheet_structure_obj
        self.write_to_file()

    def write_to_file(self):
        file_name = self.output_dir + self.sheet_structure_obj.sheet_name + ".proto"
        file = open(file_name, "w")
        file.write(self.compose_content())
        file.close()

    def compose_content(self):
        content = self.structure_template
        content = content.replace('{proto_name}', self.sheet_structure_obj.sheet_name)
        content = content.replace('{package_name}', self.proto_package_name)
        count = 0
        for name, column_value_type in self.sheet_structure_obj.column_name_2_type.items():
            count += 1
            element = self.element_template
            if column_value_type & CellType.ARRAY.value is CellType.ARRAY.value:
                element = element.replace('{specify_field}', 'repeated ')
                column_value_type -= CellType.ARRAY.value
            else:
                element = element.replace('{specify_field}', '')
            element = element.replace('{type}', CellType.to_string(CellType(column_value_type)))
            element = element.replace('{element_name}', name)
            element = element.replace('{order}', str(count))
            content += element
        content += '}'
        return content

