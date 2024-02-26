import unittest

from domains.helper.json_encoder import convert_python_object_to_dict


class TestConvertPythonObjectToDict(unittest.TestCase):

    def test_convert_python_object_to_dict(self):
        class MySubClass:
            def __init__(self):
                self.attr1 = 1
                self.attr2 = "test"
                self.attr3 = [1, 2, 3]

        # Define a sample Python object to test
        class MyClass:
            def __init__(self):
                self.attr1 = 1
                self.attr2 = "test"
                self.attr3 = [1, 2, 3]
                self.attr4 = MySubClass()
                self.attr5 = {"attr1": 1}
                self.attr6 = None

        # Create an instance of the sample object
        obj = MyClass()

        # Call the function and check the result
        result = convert_python_object_to_dict(obj)

        # Assert that the result is as expected
        expected_result = {
            "attr1": 1,
            "attr2": "test",
            "attr3": [1, 2, 3],
            "attr4": {"attr1": 1, "attr2": "test", "attr3": [1, 2, 3]},
            "attr5": {"attr1": 1},
        }
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
