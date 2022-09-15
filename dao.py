from unicodedata import name
from dto import bitDTO
from dbutil import getConnect

#  id, asset, name, date, open, high, low, close
class bitDAO:
    def coininsert(self, bitDTO):
        try:
            conn = getConnect()
            cur = conn.cursor()
            cur.execute('insert into Crypto (asset, name, date, open, high, low, close ) values (%s,%s,%s,%s,%s,%s,%s)',
                        (bitDTO.getAsset(),bitDTO.getName(),bitDTO.getDate(),bitDTO.getOpen(),bitDTO.getHigh(),bitDTO.getLow(),bitDTO.getClose()))
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cur.close()
            conn.close()

    def allcoin(self, name):
        try:
            conn = getConnect()
            cur = conn.cursor()

            cur.execute('select * from crypto where name=%s', (name))
            myresult = cur.fetchall()
            
            conn.commit()

            return myresult
        except Exception as e:
            conn.rollback()
            print(e)

        finally:
            cur.close()
            conn.close()
        

    def deletecoin(self, date, asset):
        try:
            conn = getConnect()
            cur = conn.cursor()

            cur.execute('delete from crypto where date=%s && asset=%s', (date, asset))

            conn.commit()

        except Exception as e:
            conn.rollback()
            print(e)

        finally:
            cur.close()
            conn.close()
    
    def minmax(self,name):
        myresult = []
        try:
            conn = getConnect()
            cur = conn.cursor()

            cur.execute('select name,date date_high,high from crypto where name = %s order by high desc limit 1',(name))
            max = cur.fetchone()
            
            cur.execute('select name,date date_low,low from crypto where name = %s order by low asc limit 1',(name))
            min = cur.fetchone()

            myresult = [max, min]
        

        
        
        except Exception as e:
            conn.rollback()
            print(e)

        finally:
            cur.close()
            conn.close()

        return myresult

    def selectname(self):
        myresult = []
        try:
            conn = getConnect()
            cur = conn.cursor()
            cur.execute('select distinct name from crypto')

            myresult = cur.fetchall()
            
            
        except Exception as e:
            conn.rollback()
            print(e)

        finally:
            cur.close()
            conn.close()
            
        return myresult
