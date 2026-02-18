# Databricks notebook source
# MAGIC %run ../config/_env_config

# COMMAND ----------

dbutils.widgets.text("ENV", "local_test")
env = dbutils.widgets.get("ENV")

notebook_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get().split("/")[-1]
config = load_config("../config/config.json", notebook_name)

print(config)
print(config["source_table"])
print(config["target_table"])

# COMMAND ----------

print("SST001を実行しました")
print(env)

print("Git Folder作成しました")
