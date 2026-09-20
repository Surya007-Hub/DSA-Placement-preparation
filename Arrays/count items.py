class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            if ruleKey == "type" and item[0] == ruleValue:
                count += 1
            elif ruleKey == "color" and item[1] == ruleValue:
                count += 1
            elif ruleKey == "name" and item[2] == ruleValue:
                count += 1
        return count


if __name__ == "__main__":
    items = [
        ["phone", "blue", "pixel"],
        ["computer", "silver", "lenovo"],
        ["phone", "gold", "iphone"],
        ["computer", "silver", "macbook"],
    ]

    result = Solution().countMatches(items, "color", "silver")
    print(f"Number of matches for color='silver': {result}")
    print(f"Number of matches for type='phone': {Solution().countMatches(items, 'type', 'phone')}")