#     def test_save_to_file_csv_two_squares(self):
#         s1 = Square(10, 7, 2, 8)
#         s2 = Square(8, 1, 2, 3)
#         Square.save_to_file_csv([s1, s2])
#         with open("Square.csv", "r") as f:
#             self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

#     def test_save_to_file__csv_cls_name(self):
#         s = Square(10, 7, 2, 8)
#         Base.save_to_file_csv([s])
#         with open("Base.csv", "r") as f:
#             self.assertTrue("8,10,7,2", f.read())

#     def test_save_to_file_csv_overwrite(self):
#         s = Square(9, 2, 39, 2)
#         Square.save_to_file_csv([s])
#         s = Square(10, 7, 2, 8)
#         Square.save_to_file_csv([s])
#         with open("Square.csv", "r") as f:
#             self.assertTrue("8,10,7,2", f.read())

#     def test_save_to_file__csv_None(self):
#         Square.save_to_file_csv(None)
#         with open("Square.csv", "r") as f:
#             self.assertEqual("[]", f.read())

#     def test_save_to_file_csv_empty_list(self):
#         Square.save_to_file_csv([])
#         with open("Square.csv", "r") as f:
#             self.assertEqual("[]", f.read())

#     def test_save_to_file_csv_no_args(self):
#         with self.assertRaises(TypeError):
#             Rectangle.save_to_file_csv()

#     def test_save_to_file_csv_more_than_one_arg(self):
#         with self.assertRaises(TypeError):
#             Square.save_to_file_csv([], 1)


# class TestBase_load_from_file_csv(unittest.TestCase):
#     """Unittests for testing load_from_file_csv method of Base class."""

#     @classmethod
#     def tearDown(self):
#         """Delete any created files."""
#         try:
#             os.remove("Rectangle.csv")
#         except IOError:
#             pass
#         try:
#             os.remove("Square.csv")
#         except IOError:
#             pass

#     def test_load_from_file_csv_first_rectangle(self):
#         r1 = Rectangle(10, 7, 2, 8, 1)
#         r2 = Rectangle(2, 4, 5, 6, 2)
#         Rectangle.save_to_file_csv([r1, r2])
#         list_rectangles_output = Rectangle.load_from_file_csv()
#         self.assertEqual(str(r1), str(list_rectangles_output[0]))

#     def test_load_from_file_csv_second_rectangle(self):
#         r1 = Rectangle(10, 7, 2, 8, 1)
#         r2 = Rectangle(2, 4, 5, 6, 2)
#         Rectangle.save_to_file_csv([r1, r2])
#         list_rectangles_output = Rectangle.load_from_file_csv()
#         self.assertEqual(str(r2), str(list_rectangles_output[1]))

#     def test_load_from_file_csv_rectangle_types(self):
#         r1 = Rectangle(10, 7, 2, 8, 1)
#         r2 = Rectangle(2, 4, 5, 6, 2)
#         Rectangle.save_to_file_csv([r1, r2])
#         output = Rectangle.load_from_file_csv()
#         self.assertTrue(all(type(obj) == Rectangle for obj in output))

#     def test_load_from_file_csv_first_square(self):
#         s1 = Square(5, 1, 3, 3)
#         s2 = Square(9, 5, 2, 3)
#         Square.save_to_file_csv([s1, s2])
#         list_squares_output = Square.load_from_file_csv()
#         self.assertEqual(str(s1), str(list_squares_output[0]))

#     def test_load_from_file_csv_second_square(self):
#         s1 = Square(5, 1, 3, 3)
#         s2 = Square(9, 5, 2, 3)
#         Square.save_to_file_csv([s1, s2])
#         list_squares_output = Square.load_from_file_csv()
#         self.assertEqual(str(s2), str(list_squares_output[1]))

#     def test_load_from_file_csv_square_types(self):
#         s1 = Square(5, 1, 3, 3)
#         s2 = Square(9, 5, 2, 3)
#         Square.save_to_file_csv([s1, s2])
#         output = Square.load_from_file_csv()
#         self.assertTrue(all(type(obj) == Square for obj in output))

#     def test_load_from_file_csv_no_file(self):
#         output = Square.load_from_file_csv()
#         self.assertEqual([], output)

#     def test_load_from_file_csv_more_than_one_arg(self):
#         with self.assertRaises(TypeError):
#             Base.load_from_file_csv([], 1)


# if __name__ == "__main__":
#     unittest.main()
