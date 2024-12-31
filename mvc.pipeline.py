import os

def create_file(path, content=""):
    """Helper function to create a file with optional content."""
    try:
        with open(path, 'w') as file:
            file.write(content)
        print(f"Created file: {path}")
    except Exception as e:
        print(f"Error creating file {path}: {e}")

def main():
    # Define folder structure
    folders = ['controllers', 'views', 'routes', 'models', 'config', 'logs']

    # Create folders
    for folder in folders:
        try:
            os.makedirs(folder, exist_ok=True)
            print(f"Created folder: {folder}")
        except Exception as e:
            print(f"Error creating folder {folder}: {e}")

    # Create root files
    create_file('app.js')
    create_file('.env', "PORT=3000\nDATABASE_URL=<your_mongo_connection>")
    create_file('config/database_config.js')

    # Updated README content
    readme_content = '''
    ## Project Setup
    Generated using Python Script - [Github](https://github.com/daksh-deep/mvc-setup-script)

    ## Author
    For any inquiries or support, please contact:
    - **Daksh Deep**: [dakshsaxena04@gmail.com](mailto:dakshsaxena04@gmail.com)

    ## License

    This project is open-source and available under the **MIT License**.
    '''

    create_file('README.md', readme_content)

    # Create logs folder and log file
    create_file('logs/app.log')

    print("MVC structure created successfully.")

if __name__ == '__main__':
    main()
