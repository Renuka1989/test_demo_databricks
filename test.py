# Databricks notebook source
dbutils.fs.mount(
  source = "wasbs://contdemo@storagerenuka.blob.core.windows.net",
  mount_point = "/mnt/<Keyvalue>",
  extra_configs = {"fs.azure.account.key.adlsstorage.blob.core.windows.net":"4UHvmTXkqwWCa6oq+nKhS6t4IpD6oqcaS71kF0da+xuG+uTsTFLZpe3oEV8Nv8+FALtMsrNnpL4wTxlkh+qt+w=="})


