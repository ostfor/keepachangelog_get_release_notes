Script allows parsing release notes from CHANGELOG.md

Format for CHANGELOG is https://keepachangelog.com/en/1.0.0/

# Script description

```
usage: keepachangelog_get_release_notes [-h] [--tag TAG] [--changelog_file CHANGELOG_FILE]

optional arguments:
  -h, --help            show this help message and exit
  --tag TAG, -t TAG     tag which should be used for a doc
  --changelog_file CHANGELOG_FILE, -c CHANGELOG_FILE
                        file CHANGELOG.md in 'keep a changlog' format
```

Example:

```bash
keepachangelog_get_release_notes -t 0.0.0 -c ./CHANGELOG.md 
```

Output:

```
### Added
- Added script for parsing CHANGELOG.md  

[Unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.0.0...HEAD

```
