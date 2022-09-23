import shelve
from datetime import datetime

__author__ = 'piper'

def initialize():
    db = shelve.open('database')
    if not 'memories' in db.keys():
        db['memories'] = {}
    db.close()

class Event():
    def __init__(self, item, inhow, desc=[], relations={'relation':'word'}, moment=datetime.ctime(datetime.now())):
        self.item = item
        self.desc = desc
        self.inhow = inhow
        self.moment = moment
        self.relations = relations
        self.moments = []

    def memorize(self):
        db = shelve.open('database')
        organize = {'item':self.item, 'moment': self.moment, 'desc':self.desc,
                    'inhow': self.inhow, 'relations': self.relations}
        db[self.item] = organize
        times = [self.moment]
        memories = db['memories']
        memories[self.item] = times
        db['memories'] = memories
        print(db[self.item])
        db.close()
        results = '\n{0}: {1} [{2}]\n'.format(self.item, memories[self.item][0],
                                              len(memories[self.item]))
        return results

    def recall(self):
        db = shelve.open('database')
        if self.item in db.keys():
            update = self.can_change(db)
            if update == 'desc':
                self.update_mem(db, 'desc')
            elif update == 'relations':
                self.update_mem(db, 'relations')
            memories = db['memories']
            moment = datetime.ctime(datetime.now())
            memories[self.item].append(moment)
            memories[self.item].sort()
            memories[self.item].reverse()
            db['memories'] = memories
            db.close()
            results = '\n{0}: {1} [{2}]\n'.format(self.item, memories[self.item][0],
                                                len(memories[self.item]))
            return results
        else:
            results = self.memorize()
            return results

    def can_change(self, db):
        item = db[self.item]
        if  item['desc'] != db[self.item]['desc']:
            return 'desc'
        elif item['relations'] != db[self.item]['relations']:
            return 'relations'
        else:
            return False

    def update_mem(self, db, what):
        item = db[self.item]
        if what == 'desc':
            desc = item['desc']
            desc.append(str(self.desc))
            item['desc'] = desc
            db[self.item] = item
        else:
            rel = item['relations']
            rel[self.relations['relation']] = self.relations['word']
            db['relations'] = rel
