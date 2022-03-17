import sqlite3
import logger


def __get_conn():
    return sqlite3.connect('database.db')


def init():
    create_tbl_deploy_authors = '''
        CREATE TABLE IF NOT EXISTS deploy_authors (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            deleted_at DATETIME,
            deploy_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            commit_hash TEXT NOT NULL
        );
    '''
    create_index_deploy_authors = '''
        CREATE INDEX IF NOT EXISTS idx_deploy_authors ON deploy_authors (
            id	ASC
        );
    '''

    try:
        con = __get_conn()

        with con:
            con.execute(create_tbl_deploy_authors)
            con.execute(create_index_deploy_authors)
    except Exception as e:
        logger.error("Couldn't initialize database")
        raise e


def create_deploy_author(author: dict):
    try:
        con = __get_conn()
        sql = '''
            INSERT INTO deploy_authors(
                deploy_id, name, email, commit_hash
            ) values (?, ?, ?, ?);
        '''

        values = (
            author['deploy_id'],
            author['name'],
            author['email'],
            author['commit_hash'],
        )

        with con:
            cur = con.execute(sql, values)
            author['id'] = cur.lastrowid

            logger.info(author)

            return author
    except Exception as e:
        logger.error("Couldn't insert deploy author")
        raise e


def find_deploy_author(id: int):
    try:
        con = __get_conn()
        sql = '''
            SELECT id, created_at, updated_at, deleted_at, 
                deploy_id, name, email, commit_hash
            FROM deploy_authors
            WHERE id = {};
        '''.format(id)

        row = con.execute(sql).fetchone()

        result = {
            'id': row[0],
            'created_at': row[1],
            'updated_at': row[2],
            'deleted_at': row[3],
            'deploy_id': row[4],
            'name': row[5],
            'email': row[6],
            'commit_hash': row[7],
        }

        return result
    except Exception as e:
        logger.error("Couldn't find deploy author")
        raise e
