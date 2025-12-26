# LeetCode Problem Repository

A structured repository for tracking and organizing LeetCode problems with automated template generation.

## 📁 Repository Structure

```
leetcode/
├── Problems/
│   ├── Easy/
│   │   └── [Category]/
│   │       ├── [number]_[problem_name].md
│   │       └── assets/
│   ├── Medium/
│   │   └── [Category]/
│   │       ├── [number]_[problem_name].md
│   │       └── assets/
│   └── Hard/
│       └── [Category]/
│           ├── [number]_[problem_name].md
│           └── assets/
├── utils/
│   └── create_problem.py    # Script to generate problem templates
├── Algorithms/               # Algorithm implementations
├── Makefile                 # Convenience commands
├── new                      # Wrapper script for creating problems
└── requirements.txt         # Python dependencies
```

## 🚀 Quick Start

### 1. Setup

```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (optional - only needed for auto-fetching)
pip install -r requirements.txt
```

### 2. Create a New Problem

You have three ways to create a new problem template:

#### Option A: Using the wrapper script (easiest)
```bash
# Auto-fetch from LeetCode API (requires requests library)
./new 128

# Manual specification
./new 128 "Two Sum" Easy Array
```

#### Option B: Using Make
```bash
# Auto-fetch from LeetCode
make new NUM=128

# With difficulty and category
make new NUM=128 DIFF=Medium CAT=Array

# Full manual specification
make new NUM=1 TITLE="Two Sum" DIFF=Easy CAT=Array
```

#### Option C: Using Python directly
```bash
# Auto-fetch from LeetCode (requires requests)
python3 utils/create_problem.py 128

# Manual specification
python3 utils/create_problem.py 128 "Two Sum" Easy Array
```

## 📝 Usage Examples

### Auto-fetch from LeetCode API

If you have `requests` installed, you can just provide the problem number:

```bash
./new 128
```

The script will automatically fetch:
- Problem title
- Difficulty level
- Category (from tags)

### Partial Manual Specification

You can provide partial information and let the script fetch the rest:

```bash
# Fetch difficulty and category
./new 128 "Longest Consecutive Sequence"

# Fetch only category
./new 128 "Two Sum" Easy
```

### Full Manual Specification

If you don't have `requests` installed or want to specify everything:

```bash
./new 128 "Longest Consecutive Sequence" Medium Array
```

## 📋 Problem Template Structure

Each problem file includes:

- **Problem metadata**: Number, title, difficulty, LeetCode link
- **Description**: Problem description section
- **Examples**: Input/output examples with explanations
- **Constraints**: Problem constraints
- **Approach**: Your solution approach
- **Solution Code**: Your implementation
- **Time & Space Complexity**: Analysis
- **Notes**: Additional insights and optimizations
- **Alternative Solutions**: Multiple approaches if applicable
- **Related Problems**: Links to similar problems

## 🛠️ Features

- ✅ **Auto-fetching**: Automatically retrieves problem metadata from LeetCode API
- ✅ **Organized Structure**: Problems organized by difficulty and category
- ✅ **Template Generation**: Creates markdown templates with all necessary sections
- ✅ **Assets Directory**: Automatically creates `assets/` folder for each category
- ✅ **Multiple Interfaces**: Command-line script, Makefile, and wrapper script

## 📦 Dependencies

- **Python 3.6+**: Required for the script
- **requests** (optional): For auto-fetching problem data from LeetCode API
  ```bash
  pip install requests
  ```

## 🔧 Troubleshooting

### Auto-fetch not working?

1. **Check if requests is installed:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify network connection**: The script needs internet access to fetch from LeetCode API

3. **Use manual specification**: If auto-fetch fails, provide the information manually:
   ```bash
   ./new 128 "Problem Title" Medium Array
   ```

### File already exists?

The script will prompt you before overwriting existing files. You can:
- Type `y` to overwrite
- Type `N` (or anything else) to cancel

## 📚 Directory Naming

- **Difficulty**: `Easy`, `Medium`, `Hard` (case-insensitive)
- **Category**: Any category name (e.g., `Array`, `Strings`, `Dynamic Programming`, `Trees`)

The script automatically creates directories if they don't exist.

## 💡 Tips

1. **Use auto-fetch when possible**: It saves time and ensures accuracy
2. **Keep categories consistent**: Use the same category names for similar problems
3. **Add assets**: Use the `assets/` folder for diagrams, images, or additional files
4. **Update templates**: Fill in all sections to maximize learning value

## 🤝 Contributing

Feel free to extend this repository with:
- Additional problem categories
- Algorithm implementations in `Algorithms/`
- Improvements to the template generator
- Documentation enhancements

## 📄 License

This repository is for personal use in tracking LeetCode practice problems.

---

