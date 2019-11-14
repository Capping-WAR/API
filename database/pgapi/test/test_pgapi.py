from pgapi import PGAPI

class TestPGAPI:
    pgapi = PGAPI()
    def testInsert(self):
        values = [
            "20077999,'this is a test', 1, 1, 1, 1, 1, current_timestamp"
        ]
        cols = """
        userId, sentence, rule1, rule2, rule3, rule4, rule5, dateAdded
        """
        results = self.pgapi.insert('Sentences', values, cols)
        assert str(results) == 'no results to fetch'

    def testGet(self):
        results = self.pgapi.get('Sentences')
        assert results != []

    def testUpdate(self):
        values = {
            'rule1': 0,
            'rule2': 0
        }
        results = self.pgapi.update(
            'Sentences', values, 'WHERE sentence=\'this is a test\''
            )
        assert str(results) == 'no results to fetch' 

    def testDelete(self):
        results = self.pgapi.delete(
            'Sentences', 'WHERE sentence=\'this is a test\''
            )
        assert str(results) == 'no results to fetch'
    
    


 
 