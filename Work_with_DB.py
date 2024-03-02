from DBcm import DBContextManager


def select_dict(config: dict, _sql: str):
    with DBContextManager(config) as cur:
        if cur is None:
            raise ValueError("Cursor doesn't exist")
        else:
            cur.execute(_sql)
            result = cur.fetchall()

            if result:
                scheme = [item[0] for item in cur.description]
                result_dict = []

                for product in result:
                    result_dict.append(dict(zip(scheme, product)))

                return result_dict
            else:
                return None


def select_tab(config: dict, _sql: str):
    with DBContextManager(config) as cur:
        cur.execute(_sql)
        res = cur.fetchall()

        if res is None:
            return None
        elif len(res) == 0:
            return -1
        else:
            schema = [item[0] for item in cur.description]
            res_dict = [schema, ]

            for product in res:
                res_dict.append(product)

            return res_dict


def select_distinct(config: dict, sql: str):
    with DBContextManager(config) as cur:
        cur.execute(sql)
        res = cur.fetchall()

        if res is None:
            return None
        elif len(res) == 0:
            return -1
        else:
            res_tuple = []

            for buf in res:
                res_tuple.append(buf[0])

            res_tuple = tuple(res_tuple)

            return res_tuple


def call_procedure(db_config: dict, proc_name: str, args=(), argpos=()):
    res = []

    with DBContextManager(db_config) as cur:
        cur.callproc(proc_name, args)

        for i in argpos:
            cur.execute(f'select @_{proc_name}_{i}')
            res.append(cur.fetchone()[0])

    return res
