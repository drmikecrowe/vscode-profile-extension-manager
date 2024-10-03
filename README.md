# VS Code Extension Manager (VEM)

VS Code Extension Manager (VEM) is a powerful command-line tool designed to help you manage your Visual Studio Code extensions across different profiles. It allows you to dump, categorize, and apply extensions with ease, streamlining your VS Code setup process.

## Features

- Extract extensions from VS Code profiles
- Categorize extensions into groups
- Apply categorized extensions to specific profiles
- Support for multiple profiles
- Easy-to-use command-line interface

--- 

### Dumping Extensions

[![Dumping Extensions](assets/VPEM-dump.webm)](assets/VPEM-dump.webm)

### Catorizing Extensions

[![Catorizing Extensions](assets/VPEM-catorize.webm)](assets/VPEM-catorize.webm)

### Applying Extensions to Profile

[![Applying Extensions to Profile](assets/VPEM-apply.webm)](assets/VPEM-apply.webm)

---

## Installation

To install VEM, you can use pip:

```sh
git clone TODO
poetry install
TODO
```

## Usage

Here are some basic usage examples:

- Dump extensions from a profile:

```sh
   vem dump --profile "Default"
```

- Apply extensions to a profile:

```sh
   vem apply --profile "Work" --category "Python Development"
```

- List all categories:

```md
   vem list-categories
```

For more detailed usage instructions, please refer to the [documentation](link-to-documentation).

## Contributing

We welcome contributions to VEM! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with a clear message
4. Push your changes to your fork
5. Create a pull request

Please make sure to update tests as appropriate and adhere to the project's coding standards.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please file an issue on the [GitHub issue tracker](link-to-issues).

## Acknowledgements

We'd like to thank all the contributors who have helped make VEM better!
