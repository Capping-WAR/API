from orm import ORM

class TestORM:
    orm = ORM()
    def testInsert(self):
        values = ["1, 1, 'test', current_timestamp"]
        cols = 'balaccuracy, rulenum, loc, dateadded'
        results = self.orm.insert('Versions', values, cols)
        assert str(results) == 'no results to fetch'

    def testGet(self):
        results = self.orm.get('Versions')
        assert results != []
    
        print(results)

    def testDelete(self):
        results = self.orm.delete('Versions', 'loc=\'test\'')
        assert str(results) == 'no results to fetch'

