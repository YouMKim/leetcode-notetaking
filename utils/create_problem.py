#!/usr/bin/env python3
"""
CLI utility to create a new LeetCode problem markdown template.

Usage:
    # Auto-fetch from LeetCode (just provide number, requires 'requests' library)
    python utils/create_problem.py 128
    
    # Manual specification (positional arguments)
    python utils/create_problem.py 128 "Two Sum" Easy Arrays
    
    # Partial specification (will auto-fetch missing info if 'requests' installed)
    python utils/create_problem.py 128 "Two Sum" Easy
    python utils/create_problem.py 128 "Two Sum"
    python utils/create_problem.py 128

Examples:
    python utils/create_problem.py 128
    python utils/create_problem.py 1 "Two Sum" Easy Arrays
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
    Fetch problem metadata from LeetCode GraphQL API.
    Returns (title, difficulty, category/tags) or None if fetch fails.
    """
    if not HAS_REQUESTS:
        return None
    
    # LeetCode GraphQL endpoint
    url = "https://leetcode.com/graphql/"
    
    query = """
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
            json={"query": query, "variables": variables},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        questions = data.get("data", {}).get("problemsetQuestionList", {}).get("questions", [])
        if not questions:
            return None
        
        # Find exact match by frontend question ID
        for question in questions:
            frontend_id = str(question.get("frontendQuestionId", ""))
            if frontend_id == str(problem_number):
                title = question.get("title", "")
                difficulty = question.get("difficulty", "")
                tags = [tag.get("name") for tag in question.get("topicTags", [])]
                # Use first tag as category, or "Arrays" as default
                category = tags[0] if tags else "Arrays"
                return title, difficulty, category
        
        # If exact match not found, try without search filter (might be slow)
        # For now, return None and let user provide manually
        return None
    except requests.exceptions.RequestException as e:
        print(f"Warning: Network error fetching from LeetCode API: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Warning: Could not fetch from LeetCode API: {e}", file=sys.stderr)
        return None


def create_problem_template(number: int, title: str, difficulty: str, category: str = None) -> str:
    """Generate the markdown template content."""
    leetcode_url = f"https://leetcode.com/problems/{sanitize_filename(title).replace('_', '-')}/"
    
    template = f"""# {number}. {title}

**Difficulty:** {difficulty}  
**LeetCode Link:** [{number}. {title}]({leetcode_url})

---

## Description

<!-- Insert problem description here -->

---

## Examples

### Example 1

**Input:**
```
<!-- Insert input here -->
```

**Output:**
```
<!-- Insert output here -->
```

**Explanation:**
<!-- Insert explanation here -->

---

## Constraints

<!-- Insert constraints here -->

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
                       help="Problem category (e.g., 'Arrays', 'Strings')")
    parser.add_argument("--no-fetch", action="store_true",
                       help="Don't try to fetch from API (requires title and difficulty)")
    
    args = parser.parse_args()
    
    title = args.title
    difficulty = args.difficulty
    category = args.category
    
    # Try to fetch from LeetCode if needed
    if not args.no_fetch and (not title or not difficulty):
        if HAS_REQUESTS:
            print(f"Fetching problem {args.number} from LeetCode...")
            result = fetch_problem_from_leetcode(args.number)
            if result:
                fetched_title, fetched_difficulty, fetched_category = result
                if not title:
                    title = fetched_title
                    print(f"✓ Found title: {title}")
                if not difficulty:
                    difficulty = fetched_difficulty
                    print(f"✓ Found difficulty: {difficulty}")
                if not category:
                    category = fetched_category
                    print(f"✓ Found category: {category}")
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
    template = create_problem_template(args.number, title, difficulty, category)
    
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

