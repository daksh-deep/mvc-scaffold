# MVC Setup Script

A Python script that automatically generates a basic MVC (Model-View-Controller) project structure for Node.js applications. This tool helps developers quickly scaffold a new project with the necessary directories and configuration files.

## Features

- Creates a complete MVC folder structure
- Generates essential configuration files
- Sets up environment variables
- Creates initial logging setup
- Establishes a clean project foundation

## Generated Structure

```
project-root/
├── controllers/
├── views/
├── routes/
├── models/
├── config/
│   └── database_config.js
├── logs/
│   └── app.log
├── app.js
└── .env
```

## Installation

1. Clone this repository:
```git
git clone https://github.com/daksh-deep/mvc-setup-script.git
```

2. Navigate to the script directory:
```bash
cd mvc-setup-script
```

## Usage

Run the script using Python:

```python
python setup.py
```

The script will automatically create all necessary folders and files in your current directory.

## Generated Files

- **app.js**: Main application entry point
- **.env**: Environment variables configuration
- **config/database_config.js**: Database configuration settings
- **logs/app.log**: Application logging file
- Various MVC directories for organizing your code

## Environment Variables

The script creates a `.env` file with initial configuration:

```env
PORT=<value>
DATABASE_URL=<your_mongo_connection>
```

Make sure to update these values according to your project requirements.

## Customization

You can modify the script to:
- Add more directories
- Include additional configuration files
- Customize file templates
- Add specific framework dependencies

Simply edit the `folders` list or `create_file()` function calls in the script.

## Requirements

- Python 3.x
- Write permissions in the target directory

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Author

For any inquiries or support, please contact:
- **Daksh Deep**: [dakshsaxena04@gmail.com](mailto:dakshsaxena04@gmail.com)

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Inspired by common MVC architecture patterns in modern web development
