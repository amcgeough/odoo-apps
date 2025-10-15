import logging

def install_pg_trgm(cr, registry):
    """
    Ensure the pg_trgm extension is installed
    """
    try:
        cr.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")
        cr.commit()
        logging.info("PostgreSQL extension pg_trgm installed or already present.")
    except Exception as e:
        logging.error("Failed to install pg_trgm extension: %s", e)
