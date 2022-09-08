import psycopg2

log = False


def lab_database_connection():
    connection = psycopg2.connect(user="clinlims", password="", host="192.168.1.182", port="5432", database="clinlims")

    return connection


def get_lab_result_by_id(resultid):
    try:
        connection = lab_database_connection()

        cursor = connection.cursor()

        if log:
            print("Get Table record ")
        sql_select_query = """select * from result where id = %s"""
        cursor.execute(sql_select_query, (resultid,))
        record = cursor.fetchone()
        if log:
            print(record)
        return record
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def update_result(resultid, value):
    try:
        connection = lab_database_connection()

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select id, value from result where id = %s"""
        cursor.execute(sql_select_query, (resultid,))
        record = cursor.fetchone()
        if log:
            print(record)

        # Update single record now
        sql_update_query = """Update result set value = %s where id = %s"""
        cursor.execute(sql_update_query, (value, resultid))
        connection.commit()
        count = cursor.rowcount
        if log:
            print(count, "Record Updated successfully ")

        if log:
            print("Table After updating record ")
        sql_select_query = """select * from result where id = %s"""
        cursor.execute(sql_select_query, (resultid,))
        record = cursor.fetchone()
        if log:
            print(record)

        return record

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_organization_data(value):
    try:
        connection = lab_database_connection()

        cursor = connection.cursor()

        print("Get organization record ")
        #         sql_select_query = """SELECT * FROM organization WHERE name=%s"""
        sql_select_query = """SELECT * FROM clinlims.organization\
            JOIN clinlims.referral ON clinlims.organization.id=clinlims.referral.organization_id\
            JOIN clinlims.referral_result ON clinlims.referral_result.referral_id=clinlims.referral.id\
            WHERE name=%s"""
        cursor.execute(sql_select_query, (value,))
        records = cursor.fetchall()
        if log:
            print(records)
        return records
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_test_details(test_id):
    try:
        connection = lab_database_connection()

        cursor = connection.cursor()

        print("Get test details")
        sql_select_query = """select * from clinlims.test WHERE id=%s"""
        cursor.execute(sql_select_query, (test_id,))
        record = cursor.fetchone()
        if log:
            print(record)

        return record

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_sample_by_id(sample_id):
    try:
        connection = psycopg2.connect(
            user="clinlims", password="", host="192.168.1.182", port="5432", database="clinlims"
        )

        cursor = connection.cursor()

        print("get_sample_by_id ")
        sql_select_query = """select * from clinlims.sample where id = %s"""
        cursor.execute(sql_select_query, (sample_id,))
        record = cursor.fetchone()
        if log:
            print(record)
        return record
    except (Exception, psycopg2.Error) as error:
        print("get_sample_by_id: Error", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("get_sample_by_id: PostgreSQL connection is closed")


def get_patient_identity_by_patient_id(patient_id):
    try:
        connection = psycopg2.connect(
            user="clinlims", password="", host="192.168.1.182", port="5432", database="clinlims"
        )

        cursor = connection.cursor()

        print("Get Table record ")
        sql_select_query = """select identity_data from clinlims.patient_identity where patient_id = %s"""
        cursor.execute(sql_select_query, (patient_id,))
        record = cursor.fetchone()
        if log:
            print(record)
        return record
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("get_patient_identity_by_patient_id: PostgreSQL connection is closed")


def get_lab_result_by_id(resultid):
    try:
        connection = psycopg2.connect(
            user="clinlims", password="", host="192.168.1.182", port="5432", database="clinlims"
        )

        cursor = connection.cursor()

        print("get_lab_result_by_id: Get Table record ")
        sql_select_query = """select * from result where id = %s"""
        cursor.execute(sql_select_query, (resultid,))
        record = cursor.fetchone()
        if log:
            print("get_lab_result_by_id: record", record)
        return record
    except (Exception, psycopg2.Error) as error:
        print("get_lab_result_by_id: Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("get_lab_result_by_id: PostgreSQL connection is closed")


def get_person_by_id(person_id):
    try:
        connection = psycopg2.connect(
            user="clinlims", password="", host="192.168.1.182", port="5432", database="clinlims"
        )

        cursor = connection.cursor()

        print("Get patient details")
        sql_select_query = """select * from clinlims.person WHERE id=%s"""
        cursor.execute(sql_select_query, (person_id,))
        record = cursor.fetchone()
        if log:
            print(record)
        return record

    except (Exception, psycopg2.Error) as error:
        print("get_person_by_id: Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_patient_information_by_id(patient_id):
    try:
        connection = psycopg2.connect(
            user="clinlims", password="", host="192.168.1.182", port="5432", database="clinlims"
        )

        cursor = connection.cursor()

        print("Get test details")
        sql_select_query = """SELECT * FROM clinlims.patient WHERE id=%s"""
        cursor.execute(sql_select_query, (patient_id,))
        record = cursor.fetchone()
        if log:
            print(record)
        return record
    except (Exception, psycopg2.Error) as error:
        print("get_patient_information_by_id: Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_analysis_by_test_id(test_id):
    try:
        connection = psycopg2.connect(
            user="clinlims", password="", host="192.168.1.182", port="5432", database="clinlims"
        )

        cursor = connection.cursor()

        print("get_analysis_by_test_id: ")
        #         sql_select_query = """select * from clinlims.analysis WHERE id=%s"""
        sql_select_query = """SELECT clinlims.sample_human.samp_id, clinlims.sample_human.patient_id FROM clinlims.analysis
JOIN clinlims.sample_item ON clinlims.analysis.sampitem_id=clinlims.sample_item.id
JOIN clinlims.sample_human ON clinlims.sample_item.samp_id=clinlims.sample_human.samp_id
WHERE clinlims.analysis.test_id=%s"""
        cursor.execute(sql_select_query, (test_id,))
        record = cursor.fetchone()
        if log:
            print(record)

        return record

    except (Exception, psycopg2.Error) as error:
        print("get_analysis_by_test_id: Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("get_analysis_by_test_id: PostgreSQL connection is closed")
