import unittest

"""
Count names with more than size_critique letters
"""
def count_len_names(prenoms:list) -> int:
    size_critique=7
    more_than_seven = 0
    for prenom in prenoms:
        # parcours de la liste et regarde si plus grand que la size_critique, et incrementation du compte si oui
        if len(prenom) > size_critique:
            more_than_seven += 1
            print("Prenom supérieur à",size_critique,": ",prenom)
        else:
            print("Prenom inférieur ou égal à", size_critique,": ",prenom)
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_len_names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()