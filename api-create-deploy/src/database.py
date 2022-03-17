import sqlite3
import logger


def __get_conn():
    return sqlite3.connect('database.db')


def init():
    create_tbl_deploys = '''
        CREATE TABLE IF NOT EXISTS deploys (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            deleted_at DATETIME,
            current_commit TEXT,
            previous_commit TEXT,
            asset_id INTEGER NOT NULL
        );
    '''
    create_index_deploys = '''
        CREATE INDEX IF NOT EXISTS idx_deploys ON deploys (
            id	ASC
        );
    '''

    try:
        con = __get_conn()

        with con:
            con.execute(create_tbl_deploys)
            con.execute(create_index_deploys)
    except Exception as e:
        logger.error("Couldn't initialize database")
        raise e


def create_deploy(deploy: dict):
    try:
        con = __get_conn()
        sql = '''
            INSERT INTO deploys(
                current_commit, previous_commit, asset_id
            ) values (?, ?, ?);
        '''

        values = (
            deploy['current_commit'],
            deploy['previous_commit'],
            deploy['asset_id']
        )

        with con:
            cur = con.execute(sql, values)
            deploy['id'] = cur.lastrowid

            logger.info(deploy)

            return deploy
    except Exception as e:
        logger.error("Couldn't insert deploy")
        raise e


def find_deploy(id: int):
    try:
        con = __get_conn()
        sql = '''
            SELECT id, created_at, updated_at, deleted_at, 
                current_commit, previous_commit, asset_id
            FROM deploys
            WHERE id = {};
        '''.format(id)

        row = con.execute(sql).fetchone()

        result = {
            'id': row[0],
            'created_at': row[1],
            'updated_at': row[2],
            'deleted_at': row[3],
            'current_commit': row[4],
            'previous_commit': row[5],
            'asset_id': row[6],
        }

        return result
    except Exception as e:
        logger.error("Couldn't find deploy")
        raise e
