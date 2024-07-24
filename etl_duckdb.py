import duckdb
import time

def create_duckdb():
    duckdb.sql(
    """
    SELECT
        cidade
        ,min(temperatura) AS temperature_min
        ,max(temperatura) AS temperature_max
        ,avg(temperatura) AS temperature_mean
    FROM
        read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'cidade':VARCHAR, 'temperatura':'DECIMAL(3,1)'})
    GROUP BY ALL
    ORDER BY ALL
    """
    ).show()

if __name__ == "__main__":
    import time
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f"Duckdb Took: {took:.2f} secunds")