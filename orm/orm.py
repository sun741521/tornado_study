from .sunckMysql import SunckMySQL
class ORM():
    def save(self):
        # insert into students (name,age) values('tyui',32)
        #                &        &   &             &    &
        #表名
        tableName = (self.__class__.__name__).lower()
        fieldsStr = valuesStr ="("
        for field in self.__dict__:
            fieldsStr += (field + ",")
            if isinstance(self.__dict__[field], str):
                valuesStr += ("'" + self.__dict__[field] + "',")
            else:
                valuesStr += (str(self.__dict__[field]) + ",")
        #(name,age)
        fieldsStr = fieldsStr[:len(fieldsStr)-1] + ")"
        #('tyui',32)
        valuesStr = valuesStr[:len(valuesStr) - 1] + ")"
        sql = "insert into " + tableName + " " + fieldsStr + " values " + valuesStr


        print(sql)
        db = SunckMySQL()
        # db2 = SunckMySQL()
        # print(db is db2)
        db.insert(sql)

    def delete(self):
        pass

    @classmethod
    def all(cls):
        # select * from students
        tableName = (cls.__name__).lower()
        sql = "select * from " + tableName
        db = SunckMySQL()
        print(sql)
        return db.get_all_obj(sql, tableName)

    @classmethod
    def filter(cls):
        pass

