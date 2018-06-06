import xlrd
import re
from enum import Enum


class CellType(Enum):
    INT = int('00000001', 2)
    BOOL = int('00000010', 2)
    STRING = int('00000100', 2)
    DATE = int('00001000', 2)
    ARRAY = int('00010000', 2)
    ERROR = int('00100000', 2)

    @staticmethod
    def to_string(cell_type):
        if cell_type is CellType.INT:
            return 'int64'
        elif cell_type is CellType.BOOL:
            return 'bool'
        elif cell_type is CellType.STRING:
            return 'string'
        elif cell_type is CellType.DATE:
            return 'int64'
        return ''


def get_text_cell_real_type(cell_value):
    is_array = re.match('^([^;]*;)+.*$', cell_value)
    if is_array:
        first_value = cell_value[:cell_value.find(';')]
        if first_value.isdigit():
            return CellType.INT.value + CellType.ARRAY.value
        else:
            return CellType.STRING.value + CellType.ARRAY.value
    else:
        return CellType.STRING.value


def get_cell_type(cell):
    if cell.ctype is xlrd.XL_CELL_NUMBER:
        return CellType.INT.value
    elif cell.ctype is xlrd.XL_CELL_BOOLEAN:
        return CellType.BOOL.value
    elif cell.ctype is xlrd.XL_CELL_DATE:
        return CellType.DATE.value
    elif cell.ctype is xlrd.XL_CELL_TEXT:
        return get_text_cell_real_type(cell.value)
    else:
        return CellType.ERROR.value


class SheetStructure:

    def __init__(self):
        self.sheet_name = ""
        self.columns_name = []
        self.column_name_2_type = {}

    def analyze_sheet(self, sheet, sheet_name):
        self.sheet_name = sheet_name
        self.get_column_name_and_type(sheet)

    def get_column_name_and_type(self, sheet):
        for column in range(sheet.ncols):
            column_name = sheet.cell_value(0, column)
            column_name = self.format_column_name(column_name)
            if column_name is '':
                print("column:%d, column_name can't be empty" % column)
                exit(0)
            self.columns_name.append(column_name)
            column_type = get_cell_type(sheet.cell(2, column))
            if column_type is CellType.ERROR.value:
                print("column:%d data type error" % column)
                exit(0)
            self.column_name_2_type[column_name] = column_type

    def format_column_name(self, column_name):
        is_big_camel_format = re.fullmatch("([A-Z][a-z]*)+", column_name)
        if is_big_camel_format:
            words = re.split("([A-Z][a-z]*)", column_name)
            column_name = ''
            for word in words:
                if word is not '':
                    column_name += word.lower()
                    column_name += "_"
            column_name = column_name[:len(column_name) - 1]
        else:
            column_name = column_name.lower()
        return column_name