# Databricks notebook source
# MAGIC %run ../config/_env_config

# COMMAND ----------

notebook_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get().split("/")[-1]
config = load_config("../config/config.json", notebook_name)

print(config)
print(config["source_table"])
print(config["target_table"])

# COMMAND ----------

print("SGT001を実行しました")