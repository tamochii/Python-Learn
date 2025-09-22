# Python Utility Tools - AI Agent Instructions

## Project Overview
This is a collection of Python utility scripts for file operations, image processing, web downloads, and media organization. Each script is self-contained and focuses on a specific task domain.

## Code Conventions & Patterns

### File Path Handling
- **Always use raw strings** for Windows paths: `r'C:\path\to\file'`
- **Use `os.path.join()`** for cross-platform path construction
- **Use `os.makedirs(path, exist_ok=True)`** pattern for safe directory creation

Example from `file.py`:
```python
source_dir = r'F:\1_wrok\Topaz\TopazGigapixelAi\OutPut'
os.makedirs(os.path.join(source_dir, str(year)), exist_ok=True)
```

### Error Handling Patterns
- Use **try-except with specific feedback** for file operations
- Provide **descriptive Chinese error messages** for user clarity
- Include **debug print statements** for troubleshooting

Example from `zip.py`:
```python
try:
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(extract_to)
    print(f'✅ 成功解压：{zip_path} -> {extract_to}')
except Exception as e:
    print(f'❌ 解压失败，错误信息：{e}')
```

### Batch Processing Pattern
- Use **range-based loops** for numbered sequences (years, episodes)
- Implement **list comprehensions** for URL/filename transformations
- Always include **progress feedback** with print statements

Example from `download_images.py`:
```python
new_image_urls = [url.replace("amethyst", replacement) for url in image_urls]
for url in new_image_urls:
    # Process with feedback
    print(f"Downloaded: {file_name}")
```

## Script Categories

### File Organization (`file.py`, `rename.py`)
- **Year-based categorization**: Extract years from filenames using string matching
- **Batch renaming**: Use format strings with zero-padding `{:02d}`
- **File validation**: Check expected counts before processing

### Media Processing (`test.py` - WebP conversion)
- **PIL/Pillow**: Standard library for image format conversion
- **RGB conversion**: Always convert to RGB before saving WebP
- **Quality settings**: Use `quality=100` for maximum quality

### Web Operations (`download_images.py`)
- **requests library**: Standard for HTTP downloads
- **URL manipulation**: String replacement for batch URL generation
- **File writing**: Use binary mode `'wb'` for image downloads

### Utility Operations (`zip.py`, `creat_package.py`)
- **Safety checks**: Validate file existence and format before processing
- **Unicode handling**: Support for Chinese characters in paths and names
- **Status indicators**: Use emoji (✅❌) for clear operation feedback

## Development Workflow

### Testing Approach
- **No formal test framework** - scripts are single-use utilities
- **Manual verification** through print statements and file checks
- **Small batch testing** recommended before full runs

### Dependencies
- Standard library preferred (`os`, `shutil`, `zipfile`)
- External: `requests` for downloads, `PIL` for image processing
- No virtual environment setup documented

### Debugging
- **Verbose logging**: Include filename and operation details in prints
- **Step-by-step feedback**: Show progress for each file processed
- **Error context**: Include original filename/path in error messages

## AI Agent Guidelines

When working with this codebase:
1. **Preserve Chinese comments and messages** - this appears to be the primary language
2. **Maintain the print-heavy debugging style** - users rely on console feedback
3. **Use raw strings for all Windows paths** - critical for path handling
4. **Follow the existing error handling patterns** - try-except with descriptive feedback
5. **Keep scripts self-contained** - avoid introducing complex dependencies
6. **Test with small batches first** - these scripts often process large file sets

## Common Operations
- Creating numbered folders: `range(start, end)` with `os.makedirs()`
- Batch file moves: `shutil.move()` with year/pattern detection
- Image format conversion: PIL with RGB conversion step
- Web downloads: `requests.get()` with binary file writing