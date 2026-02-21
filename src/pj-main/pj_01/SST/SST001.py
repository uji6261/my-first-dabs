# Databricks notebook source
notebook_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get().split("/")[-1]

print(notebook_name)

# COMMAND ----------

dbutils.widgets.text("ENV", "local_test")
env = dbutils.widgets.get("ENV")

print(env)
