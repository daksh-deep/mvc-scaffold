# MVC Scaffold

A Python script that automatically generates a robust MVC (Model-View-Controller) project structure for Node.js applications. This tool helps developers scaffold a new project efficiently with all necessary directories, configuration files, and dependencies.

## Features

- Generates a complete MVC folder structure
- Creates essential configuration files for the project
- Sets up environment variables with `.env`
- Initializes npm and installs dependencies like Express, Mongoose, and Dotenv
- Offers support for both JavaScript and TypeScript
- Provides boilerplate database connection code (`database_config.js` or `database_config.ts`)

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
├── .env
└── README.md
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/daksh-deep/mvc-scaffold.git
   ```

2. Navigate to the script directory:
   ```bash
   cd mvc-scaffold
   ```

3. Ensure Python 3.8.1 (and above) is installed on your system.

## Usage

Run the script using Python:

```bash
python mvc_scaffold.py
```

The script will prompt you to:
- Choose between JavaScript and TypeScript.
- Enter the port number for your application.

Once completed, the script will create all necessary folders, files, and configurations in your current directory.

## Generated Files

- **app.js** or **app.ts**: Main application entry point
- **.env**: Environment variables configuration
- **config/database_config.js** or **config/database_config.ts**: Database configuration settings
- **logs/app.log**: Application logging file
- MVC directories: `controllers/`, `models/`, `routes/`, `views/`
- **README.md**: Documentation for the project

## Environment Variables

The script creates a `.env` file with the following default values:

```env
PORT=<your_port_number>
DATABASE_URL=<your_mongo_connection>
```

Update these values based on your project requirements.

## Customization

You can modify the script to:
- Add more directories
- Include additional configuration files
- Customize boilerplate templates
- Install additional dependencies

Simply edit the `folders` list or `create_file()` function in the script.

## Requirements

- Python 3.8.1 (and above)
- Node.js and npm installed on your system
- Write permissions in the target directory

## Dependencies
- **inquirer**  
> The script internally installs the `inquirer` package if it's not already installed in your environment. This package is used to prompt the user for input during the setup process.

## Contributing

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request.

## Author

For any inquiries or support, please contact:
- **Daksh Deep**: [dakshsaxena04@gmail.com](mailto:dakshsaxena04@gmail.com)

Follow me on:
- LinkedIn: [Daksh Deep](https://www.linkedin.com/in/daksh-deep-791a1a298/)
- GitHub: [Daksh Deep](https://github.com/daksh-deep)

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Inspired by common MVC architecture patterns in modern web development.

