from collections import namedtuple


DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidation_Config",["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                  "transformed_train_dir",
                                                                  "transformed_test_dir",
                                                                  "preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trianed_model_file_path","base_accuracy"])                                                                  

ModelEvalutionConfig = namedtuple("ModelEvalution_Config",["model_evalution_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])