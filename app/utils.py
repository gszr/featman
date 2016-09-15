
# does something on the db (callback dbop)
# and then uses callback 'commit' to commit the changes
def db_do(dbop, commit, obj):
    dbop(obj)
    commit()
