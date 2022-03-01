from app.core.core import cur

def get_register(search):
    cur.execute(search)
    result = []
    columns = cur.description
    for value in cur.fetchall():
        tmp = {}
        for (index,column) in enumerate(value):
            tmp[columns[index][0]] = "" if column is None else column
        result.append(tmp)
    return result    