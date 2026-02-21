# Databricks notebook source
notebook_name = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get().split("/")[-1]

print(notebook_name)

# COMMAND ----------

dbutils.widgets.text("env", "local_test")
ENV = dbutils.widgets.get("env")

print(ENV)

# COMMAND ----------

print('test')
