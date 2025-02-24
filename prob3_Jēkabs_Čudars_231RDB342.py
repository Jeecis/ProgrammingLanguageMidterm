def clean_text(text, ignore_case):
    if ignore_case:
        text = text.lower()
    return text

#Asked for copilot to help in some cases and claude too.
def full_alphabet_len(text: str, ignore_case: bool = True, custom_a: str = None) -> int:
    # Helper function to get clean text (only alphabet characters)
    def clean_text(s: str) -> str:
        if ignore_case:
            s = s.lower()
        return ''.join(c for c in s if c.isalpha())
    
    # Determine alphabet to use
    if custom_a:
        alphabet = set(custom_a)
    else:
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
    alphabet_size = len(alphabet)
    
    text = clean_text(text)
    if not text:
        return 0
        
    # Sliding window approach
    char_count = {}
    complete_alphabets = 0
    left = 0
    min_length = float('inf')
        
    for right in range(len(text)):
        current_char = text[right]
        # Add new character to count
        # If current character is not in alphabet consider its default value to be zero and increment it by 1
        char_count[current_char] = char_count.get(current_char, 0) + 1
        
        # Check if we have a complete alphabet
        # Count the number of unique characters in the current window that meet the complete_alphabet requirement
        current_unique = 0
        for c in alphabet:
            if char_count.get(c, 0) >= 2:
                current_unique += 1
        
        # Now we apply sliding window approach
        # I knew that sliding window approach would be the right choice here but I didn't know how to implement it
        # So I asked Deepseek Distilled version from t3.chat and then implemented it
        # Try to minimize window from left while maintaining two complete alphabets
        while left <= right:
            if current_unique == alphabet_size:
                # We have two complete alphabets, try to minimize
                # Check if all characters in the alphabet meet the complete_alphabet requirement
                all_chars_meet_requirement = True
                for c in alphabet:
                    # If character count is less than complete_alphabet, break
                    if char_count.get(c, 0) < 2:
                        all_chars_meet_requirement = False
                        break
                
                # If all characters meet the requirement, update the minimum length
                if all_chars_meet_requirement:
                    min_length = min(min_length, right - left + 1)
                    
                # Try to remove leftmost character
                leftChar = text[left]
                char_count[leftChar] -= 1 # Remove 1 point from character from count

                # If character count is less than complete_alphabet and character is in alphabet, decrement current_unique
                if char_count[leftChar] < 2 and leftChar in alphabet:
                    current_unique -= 1

                left += 1 #Adjust the left position
            else:
                break
                
    return min_length if min_length != float('inf') else -1

# Test cases
test_text = "aabcdefghijKK 1, lmnopqrstuvwxyzaaabcdefghijKK 1, lmnopqrstuvwxyza"
print(full_alphabet_len(test_text))  # Should print 55

# Test with custom alphabet (Latvian)
latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
test_latvian = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzžaābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
print(full_alphabet_len(test_latvian, custom_a=latvian_alphabet))  # Should print 66

submission_test ="I sang, and thought I sang very well; but he just looked up into my face with a very quizzical expression, and said, 'How long have you been singing, Mademoiselle?' Outside an advertisment flew by: Brown jars prevented the mixture from freezing too quickly."
print(full_alphabet_len(submission_test))
# Result 169