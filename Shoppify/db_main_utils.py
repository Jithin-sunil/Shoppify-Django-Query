import sqlite3

def execute_query(query, params=None, fetch=False, fetchone=False):
    with sqlite3.connect("db.sqlite3") as conn:
        cursor = conn.cursor()
        cursor.execute(query, params or [])
        if fetch:
            columns = [col[0] for col in cursor.description]
            if fetchone:
                row = cursor.fetchone()
                return dict(zip(columns, row)) if row else None
            else:
                
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
        else:
            conn.commit()
            return cursor.lastrowid if 'INSERT' in query.upper() else cursor.rowcount

def fetch_all(query, params=None):
    return execute_query(query, params, fetch=True)

def fetch_one(query, params=None):
    return execute_query(query, params, fetch=True, fetchone=True)

def insert(query, params=None):
    return execute_query(query, params)

def update(query, params=None):
    return execute_query(query, params)

def delete(query, params=None):
    return execute_query(query, params)