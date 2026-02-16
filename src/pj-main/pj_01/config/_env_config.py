# Databricks notebook source
# ワークスペースのURLを取得
workspace_url = spark.conf.get("spark.databricks.workspaceUrl", "unknown")

if "dbc-30ac84d8-3e9b" in workspace_url:
    ENV = "dev"
    CATALOG = "dev_catalog"
    STORAGE_PATH = "/Volumes/dev_catalog/raw_data"
else:
    ENV = "prod"
    CATALOG = "prod_catalog"
    STORAGE_PATH = "/Volumes/prod_catalog/raw_data"

print(workspace_url)
print(ENV)

# COMMAND ----------

import json

def load_config(file_path, notebook_name):
    """
    JSONファイルを読み込み、指定されたnotebook_nameの設定を抽出し、
    環境変数（${CATALOG}等）を置換して辞書として返す
    """
    try:
        with open(file_path, 'r') as f:
            full_config = json.load(f)

        # 1. 指定されたノートブック名のセクションを取得
        if notebook_name not in full_config:
            raise KeyError(f"Notebook key '{notebook_name}' not found in {file_path}")
            
        target_section = full_config[notebook_name]
        
        # 2. 置換ルールを定義
        replacements = {
            "${CATALOG}": CATALOG,
            "${STORAGE_PATH}": STORAGE_PATH,
            "${ENV}": ENV
        }
        
        # 3. セクション内の各値をループして置換
        # 値が文字列の場合のみ置換を実行するようにガードをかける
        final_config = {}
        for key, value in target_section.items():
            if isinstance(value, str):
                new_value = value
                for placeholder, actual_val in replacements.items():
                    new_value = new_value.replace(placeholder, actual_val)
                final_config[key] = new_value
            else:
                final_config[key] = value
                
        return final_config
    
    except FileNotFoundError:
        raise Exception(f"Config file not found: {file_path}")
    except json.JSONDecodeError:
        raise Exception(f"Failed to parse JSON file: {file_path}")