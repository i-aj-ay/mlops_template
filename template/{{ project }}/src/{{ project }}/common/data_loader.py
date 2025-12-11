from loguru import logger


def data_helper(spark, config):
    source_type = config.get("source_data_type")
    source_info = config.get("databricks_table") if source_type == "databricks_table" else {}
    
    flag = False
    if source_info:
        source_table = source_info.get("table_name")
        df_table = spark.sql(f"SELECT * FROM {source_table}")
        logger.info(f"Table read successfully - `{source_table}`.")
        flag = True
    else:
        message = f"Received empty source details - `{source_info}`."
        logger.error(message)
        raise ValueError(message)
    
    if flag:
        target_info = config.get("target_details")
        target_table = target_info.get("table_name")
        df_table.write.format("delta").mode("overwrite").saveAsTable(f"{target_table}")
        logger.info(f"Source data written successfully - `{target_table}`")
    
    return {"source_table": source_table, "target_table": target_table}


def load_data(spark, func_conf):
    config = func_conf["kwargs"]
    data_output = data_helper(spark=spark, config=config)
    return data_output