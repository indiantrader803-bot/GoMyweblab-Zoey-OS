import sqlite3

conn = sqlite3.connect('autonomous-org-core/data/gomyweblab_state.db')
cur = conn.cursor()
tables = [r[0] for r in cur.execute('SELECT name FROM sqlite_master WHERE type="table"').fetchall()]
print('Tables:', tables)
for t in tables:
    count = cur.execute(f'SELECT count(*) FROM {t}').fetchone()[0]
    print(f'{t}: {count} rows')
    try:
        rows = cur.execute(f'SELECT * FROM {t} LIMIT 5').fetchall()
        print(f'Sample {t}:', rows)
    except Exception as e:
        print(f'Error reading {t}:', e)
