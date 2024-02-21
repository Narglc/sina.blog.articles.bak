import sqlite3

class SQLiteManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.create_table()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                            id INTEGER PRIMARY KEY,
                            article_id TEXT NOT NULL UNIQUE,
                            title TEXT NOT NULL,
                            class INTEGER NOT NULL,
                            tags TEXT NOT NULL,
                            has_image BOOLEAN DEFAULT FALSE,
                            content TEXT NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );''')
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS classtypes (
                            id INTEGER PRIMARY KEY,
                            class TEXT NOT NULL UNIQUE,
                            count INTEGER NOT NULL
                        );''')
        self.conn.commit()
        cursor.close()

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def getClassType(self, class_name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO classtypes (class, count) VALUES (?, 0)", (class_name,))
        cursor.execute("UPDATE classtypes SET count = count + 1 WHERE class = ?", (class_name,))
        self.conn.commit()

        # 获取修改行的主键值
        cursor.execute("SELECT id FROM classtypes WHERE class = ?", (class_name,))
        row = cursor.fetchone()
        modified_id = row[0] if row else None
        
        cursor.close()
        return modified_id

    def insertArticle(self,article_id, title, class_id, tags, has_image, content, created_at):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO articles (article_id, title, class, tags, has_image, content, created_at) 
                          VALUES (?, ?, ?, ?, ?, ?, ?)''', (article_id,title, class_id, tags, has_image, content, created_at))
        self.conn.commit()
        cursor.close()

    def checkArticleExist(self, article_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT article_id FROM articles WHERE article_id = ?", (article_id,))
        row = cursor.fetchone()
        cursor.close()
        return row is not None

    def getAllClassTypes(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id,class FROM classtypes")
        rows = cursor.fetchall()
        class_types = [{"id": row[0], "type": row[1]} for row in rows]
        cursor.close()
        return class_types

    def getOneTypeArticlesList(self, classType):
        cursor = self.conn.cursor()
        cursor.execute("SELECT title, created_at FROM articles WHERE class = ? ORDER BY created_at ASC", (classType,))
        rows = cursor.fetchall()
        articles_list = [{"title": row[0], "created_at": row[1]} for row in rows]
        cursor.close()
        return articles_list
