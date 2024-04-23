import uuid

def generate_string(length: int = 0):
    """
    Generatee a radom string using uuid4
    Args:
         length: the returned strinng length
    """
    generated_str = uuid.uuid4().hex
    if length <= 0:
        return generated_str
    else:
        return generated_str[:length]


#A few methods maybe will help at one point:

def read_from_file(file_path: str) -> str:
    """
    Read content from a file annd rerturn it
    :param file_path: path of file
    :return: str with file content
    """
    with open (file_path, 'r') as my_file:
        return my_file.read()

def list_to_str(input_list: list) -> str:
    """
    Convert a list to a strinng of comma separarted values
    :param input_list: list of eelements you want to convert e.g. [123, "key1", 222, "key2"]
    :return: string with content = "123, key1, 222, key2"
    """
    output_string = ', '.join(map(str, input_list))
    return output_string