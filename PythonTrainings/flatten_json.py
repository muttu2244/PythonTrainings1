# def flattenJsonInput(jsonFile):
# 	with open(jsonFile,r) as file:
# 		input = json.dumps(file)
#
#     for key in input.keys():
#         if Key is dict:
#             for i in key.keys():
#                 key = key + "_" + (key.keys[i]))
#
#         print(key + ":" + input[key])


# for a array value of a key
unflat_json = {
    "Key1": "Value1",
    "Key2": {
        "Key21": "Value21",
        "Key22": {
            "Key221": "Value221"
            }
        },
    "Key3": ["Value31", "Value32"]
}


# Function for flattening
# json
def flatten_json(y):
    out = {}

    def flatten(x, name=''):

        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

                # If the Nested key-value
        # pair is of list type
        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# Driver code
print(flatten_json(unflat_json))