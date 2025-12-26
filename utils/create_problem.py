#!/usr/bin/env python3
"""
CLI utility to create a new LeetCode problem markdown template.

Usage:
    # Auto-fetch from LeetCode (just provide number, requires 'requests' library)
    python utils/create_problem.py 128
    
    # Manual specification (positional arguments)
    python utils/create_problem.py 128 "Two Sum" Easy Array
    
    # Partial specification (will auto-fetch missing info if 'requests' installed)
    python utils/create_problem.py 128 "Two Sum" Easy
    python utils/create_problem.py 128 "Two Sum"
    python utils/create_problem.py 128

Examples:
    python utils/create_problem.py 128
    python utils/create_problem.py 1 "Two Sum" Easy Array
    python utils/create_problem.py 128 "Longest Consecutive Sequence" Medium

Note: For auto-fetch to work, install requests: pip install requests
      If 'requests' is not installed, you must provide title and difficulty.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def sanitize_filename(title: str) -> str:
    """Convert title to a valid filename."""
    # Convert to lowercase and replace spaces with underscores
    filename = title.lower().replace(" ", "_")
    # Remove special characters, keep only alphanumeric and underscores
    filename = re.sub(r'[^a-z0-9_]', '', filename)
    return filename


def format_examples(examples: str) -> str:
    """Format example testcases into markdown format."""
    if not examples:
        return """### Example 1

**Input:**
```
<!-- Insert input here -->
```

**Output:**
```
<!-- Insert output here -->
```

**Explanation:**
<!-- Insert explanation here -->"""
    
    # Examples are usually comma-separated or newline-separated
    # Format: "nums = [2,7,11,15], target = 9" or similar
    example_parts = examples.split('\n')
    formatted = []
    
    for i, example in enumerate(example_parts, 1):
        if not example.strip():
            continue
        formatted.append(f"""### Example {i}

**Input:**
```
{example.strip()}
```

**Output:**
```
<!-- Insert expected output here -->
```

**Explanation:**
<!-- Insert explanation here -->""")
    
    if formatted:
        return '\n\n'.join(formatted)
    else:
        return """### Example 1

**Input:**
```
<!-- Insert input here -->
```

**Output:**
```
<!-- Insert output here -->
```

**Explanation:**
<!-- Insert explanation here -->"""


def get_difficulty_path(difficulty: str) -> str:
    """Get the directory path for a difficulty level."""
    difficulty_map = {
        "easy": "Easy",
        "medium": "Medium",
        "hard": "Hard",
    }
    return difficulty_map.get(difficulty.lower(), difficulty.capitalize())


def fetch_problem_from_leetcode(problem_number: int):
    """
    Fetch problem metadata and content from LeetCode GraphQL API.
    Returns (title, difficulty, category/tags, description, examples, constraints) or None if fetch fails.
    """
    if not HAS_REQUESTS:
        return None
    
    # LeetCode GraphQL endpoint
    url = "https://leetcode.com/graphql/"
    
    # First query: Get basic metadata and titleSlug
    list_query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(
        categorySlug: $categorySlug
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        total: totalNum
        questions: data {
          acRate
          difficulty
          freqBar
          frontendQuestionId: questionFrontendId
          isFavor
          paidOnly: isPaidOnly
          status
          title
          titleSlug
          topicTags {
            name
            id
            slug
          }
          hasSolution
          hasVideoSolution
        }
      }
    }
    """
    
    # Try to fetch by problem number - search with a larger limit to find the problem
    variables = {
        "categorySlug": "",
        "skip": 0,
        "limit": 50,  # Increase limit to have better chance of finding the problem
        "filters": {
            "searchKeywords": str(problem_number)
        }
    }
    
    try:
        response = requests.post(
            url,
            json={"query": list_query, "variables": variables},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        questions = data.get("data", {}).get("problemsetQuestionList", {}).get("questions", [])
        if not questions:
            return None
        
        # Find exact match by frontend question ID
        title_slug = None
        title = None
        difficulty = None
        category = None
        
        for question in questions:
            frontend_id = str(question.get("frontendQuestionId", ""))
            if frontend_id == str(problem_number):
                title = question.get("title", "")
                difficulty = question.get("difficulty", "")
                title_slug = question.get("titleSlug", "")
                tags = [tag.get("name") for tag in question.get("topicTags", [])]
                # Use first tag as category, or "Array" as default
                category = tags[0] if tags else "Array"
                break
        
        if not title_slug:
            return None
        
        # Second query: Get full problem content
        content_query = """
        query questionContent($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            content
            exampleTestcases
            metaData
          }
        }
        """
        
        content_variables = {"titleSlug": title_slug}
        content_response = requests.post(
            url,
            json={"query": content_query, "variables": content_variables},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        content_response.raise_for_status()
        content_data = content_response.json()
        
        question_data = content_data.get("data", {}).get("question", {})
        content = question_data.get("content", "")
        example_testcases = question_data.get("exampleTestcases", "")
        metadata = question_data.get("metaData", "")
        
        # Parse description, examples, and constraints from content
        description, examples, constraints = parse_problem_content(content, example_testcases)
        
        return title, difficulty, category, description, examples, constraints
        
    except requests.exceptions.RequestException as e:
        print(f"Warning: Network error fetching from LeetCode API: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Warning: Could not fetch from LeetCode API: {e}", file=sys.stderr)
        return None


def parse_problem_content(content: str, example_testcases: str):
    """
    Parse HTML content from LeetCode to extract description, examples, and constraints.
    Returns (description, examples, constraints) as formatted strings.
    """
    if not content:
        return None, None, None
    
    try:
        from html import unescape
        import re
        
        # Remove HTML tags but preserve structure
        # Replace <p> with newlines, <strong> with **, etc.
        content_processed = content
        content_processed = re.sub(r'<p>', '\n', content_processed)
        content_processed = re.sub(r'</p>', '\n', content_processed)
        content_processed = re.sub(r'<strong>', '**', content_processed)
        content_processed = re.sub(r'</strong>', '**', content_processed)
        content_processed = re.sub(r'<em>', '*', content_processed)
        content_processed = re.sub(r'</em>', '*', content_processed)
        content_processed = re.sub(r'<code>', '`', content_processed)
        content_processed = re.sub(r'</code>', '`', content_processed)
        content_processed = re.sub(r'<pre>', '```\n', content_processed)
        content_processed = re.sub(r'</pre>', '\n```', content_processed)
        content_processed = re.sub(r'<li>', '- ', content_processed)
        content_processed = re.sub(r'</li>', '\n', content_processed)
        content_processed = re.sub(r'<ul>', '\n', content_processed)
        content_processed = re.sub(r'</ul>', '\n', content_processed)
        content_processed = re.sub(r'<ol>', '\n', content_processed)
        content_processed = re.sub(r'</ol>', '\n', content_processed)
        
        # Remove remaining HTML tags
        content_clean = re.sub(r'<[^>]+>', '', content_processed)
        content_clean = unescape(content_clean)
        
        # Clean up extra whitespace
        content_clean = re.sub(r'\n{3,}', '\n\n', content_clean)
        content_clean = content_clean.strip()
        
        # Split content into sections
        # Try to find constraints section
        constraints = None
        constraints_patterns = [
            r'(?:Constraints?:?\s*)(.*?)(?=\n\n##|\n\n---|\Z)',
            r'(?:Constraints?:?\s*)(.*?)(?=\n\n[#]|\Z)',
        ]
        
        for pattern in constraints_patterns:
            match = re.search(pattern, content_clean, re.IGNORECASE | re.DOTALL)
            if match:
                constraints = match.group(1).strip()
                # Remove constraints from description
                content_clean = content_clean[:match.start()].strip()
                break
        
        # If no constraints found, try to extract from end of content
        if not constraints:
            # Look for common constraint keywords at the end
            lines = content_clean.split('\n')
            constraint_start = None
            for i, line in enumerate(lines):
                if re.search(r'constraints?', line, re.IGNORECASE):
                    constraint_start = i
                    break
            
            if constraint_start:
                constraint_lines = lines[constraint_start:]
                constraints = '\n'.join(constraint_lines).strip()
                content_clean = '\n'.join(lines[:constraint_start]).strip()
        
        # Description is the remaining content
        description = content_clean if content_clean else None
        
        # Examples from testcases
        examples = example_testcases if example_testcases else None
        
        return description, examples, constraints
        
    except Exception as e:
        print(f"Warning: Could not parse problem content: {e}", file=sys.stderr)
        return None, None, None


def create_problem_template(number: int, title: str, difficulty: str, category: str = None, 
                            description: str = None, examples: str = None, constraints: str = None) -> str:
    """Generate the markdown template content."""
    leetcode_url = f"https://leetcode.com/problems/{sanitize_filename(title).replace('_', '-')}/"
    
    # Format description
    description_text = description if description else "<!-- Insert problem description here -->"
    
    # Format constraints
    constraints_text = constraints if constraints else "<!-- Insert constraints here -->"
    if constraints_text and not constraints_text.startswith("<!--"):
        # Format constraints as a list if they're not already formatted
        constraints_lines = [line.strip() for line in constraints_text.split('\n') if line.strip()]
        if len(constraints_lines) > 1:
            constraints_text = '\n'.join(f"- {line}" if not line.startswith('-') else line for line in constraints_lines)
    
    template = f"""# {number}. {title}

**Difficulty:** {difficulty}  
**LeetCode Link:** [{number}. {title}]({leetcode_url})

---

## Description

{description_text}

---

## Constraints

{constraints_text}

---

## Approach

<!-- Explain your approach to solving this problem -->

---

## Solution Code

```python
class Solution:
    def solve(self):
        # Your solution here
        pass
```

---

## Time & Space Complexity

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

## Notes

<!-- Add any additional notes, insights, optimizations, or pitfalls here -->

---

## Alternative Solutions

<!-- If you have multiple approaches, document them here -->

---

## Related Problems

<!-- Link to related problems if applicable -->
"""
    return template


def main():
    parser = argparse.ArgumentParser(
        description="Create a new LeetCode problem markdown template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("number", type=int, help="Problem number (e.g., 128)")
    parser.add_argument("title", type=str, nargs="?", default=None,
                       help="Problem title (optional, will fetch if not provided)")
    parser.add_argument("difficulty", type=str, nargs="?", default=None,
                       choices=["Easy", "Medium", "Hard", "easy", "medium", "hard"],
                       help="Problem difficulty (optional, will fetch if not provided)")
    parser.add_argument("category", type=str, nargs="?", default=None,
                       help="Problem category (e.g., 'Array', 'Strings') - positional argument")
    parser.add_argument("--cat", "-c", dest="category_override", type=str, default=None,
                       help="Override category (use this to specify only category)")
    parser.add_argument("--no-fetch", action="store_true",
                       help="Don't try to fetch from API (requires title and difficulty)")
    
    args = parser.parse_args()
    
    title = args.title
    difficulty = args.difficulty
    # Use --cat flag if provided, otherwise use positional category argument
    category = args.category_override if args.category_override else args.category
    
    # Try to fetch from LeetCode if needed
    description = None
    examples = None
    constraints = None
    
    if not args.no_fetch and (not title or not difficulty):
        if HAS_REQUESTS:
            print(f"Fetching problem {args.number} from LeetCode...")
            result = fetch_problem_from_leetcode(args.number)
            if result:
                if len(result) == 6:  # New format with description, examples, constraints
                    fetched_title, fetched_difficulty, fetched_category, description, examples, constraints = result
                else:  # Fallback to old format
                    fetched_title, fetched_difficulty, fetched_category = result[:3]
                
                if not title:
                    title = fetched_title
                    print(f"✓ Found title: {title}")
                if not difficulty:
                    difficulty = fetched_difficulty
                    print(f"✓ Found difficulty: {difficulty}")
                if not category:
                    category = fetched_category
                    print(f"✓ Found category: {category}")
                if description:
                    print(f"✓ Fetched description (includes examples)")
                if constraints:
                    print(f"✓ Fetched constraints")
            else:
                print("⚠ Could not fetch from LeetCode API.")
                if not title or not difficulty:
                    print("   Please provide --title and --difficulty manually, or install 'requests' library.")
        else:
            print("⚠ 'requests' library not installed.")
            print("   Install with: pip install requests")
            print("   Or provide --title and --difficulty manually.")
    
    # Validate required fields
    if not title:
        print("Error: Problem title is required. Use --title or install 'requests' for auto-fetch.")
        sys.exit(1)
    
    if not difficulty:
        print("Error: Problem difficulty is required. Use --difficulty or install 'requests' for auto-fetch.")
        sys.exit(1)
    
    # Get the repository root (assuming script is in utils/)
    repo_root = Path(__file__).parent.parent
    
    # Build the directory path
    difficulty_dir = get_difficulty_path(difficulty)
    if category:
        problem_dir = repo_root / "Problems" / difficulty_dir / category
    else:
        problem_dir = repo_root / "Problems" / difficulty_dir
    
    # Create directory if it doesn't exist
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    filename_base = sanitize_filename(title)
    filename = f"{args.number}_{filename_base}.md"
    filepath = problem_dir / filename
    
    # Check if file already exists
    if filepath.exists():
        response = input(f"File {filepath} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            return
    
    # Generate template
    template = create_problem_template(args.number, title, difficulty, category, description, examples, constraints)
    
    # Write file
    with open(filepath, 'w') as f:
        f.write(template)
    
    print(f"✓ Created problem template: {filepath}")
    
    # Create assets directory
    assets_dir = problem_dir / "assets"
    assets_dir.mkdir(exist_ok=True)
    print(f"✓ Assets directory ready: {assets_dir}")


if __name__ == "__main__":
    main()

