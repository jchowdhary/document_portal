import yaml


def load_config(file_path) -> dict:
    """Load a YAML configuration file and return its contents as a dictionary."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    print(f"Configuration loaded from {file_path}:\n{config}")
    return config

#load_config("/home/jayant/KrishAcademy/Module1/document_portal/config/config.yaml")
if __name__ == "__main__":
    config = load_config("/home/jayant/KrishAcademy/Module1/document_portal/config/config.yaml")
