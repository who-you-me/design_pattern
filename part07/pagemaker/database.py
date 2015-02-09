# coding: utf-8

class Database(object):
    @classmethod
    def get_properties(cls, dbname):
        filename = dbname + ".txt"
        prop = {}
        try:
            f = open(filename)
            for row in f:
                key, value = row.split("=")[:2]
                prop[key] = value.strip()
        except IOError:
            print("Warning: {} is not found".format(filename))
        finally:
            f.close()
        return prop

