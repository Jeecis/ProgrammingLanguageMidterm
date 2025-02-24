# 231RDB342
def full_alphabet_len(text: str, ignore_case: bool = True, custom_a: str = None) -> int:
    # Default English alphabet if custom_a is not provided
    alphabet = custom_a if custom_a else "abcdefghijklmnopqrstuvwxyz"
    
    # Convert to set for O(1) lookups
    needed_chars = set(alphabet.lower() if ignore_case else alphabet)
    
    # Remove non-alphabet characters and handle case
    cleaned_text = "".join(c for c in text if c.isalpha())
    if ignore_case:
        cleaned_text = cleaned_text.lower()
    
    n = len(cleaned_text)
    if n == 0:
        return 0
        
    # Sliding window approach
    char_count = {}
    min_length = float('inf')
    start = 0
    
    for end in range(n):
        # Add current character to window
        curr_char = cleaned_text[end]
        char_count[curr_char] = char_count.get(curr_char, 0) + 1
        
        # Try to minimize window from start while maintaining all needed chars
        while start <= end:
            # Check if we have all needed characters
            current_chars = set(char_count.keys())
            if not needed_chars.issubset(current_chars):
                break
                
            # Update minimum length if we found a valid window
            min_length = min(min_length, end - start + 1)
            
            # Try to remove start character
            start_char = cleaned_text[start]
            char_count[start_char] -= 1
            if char_count[start_char] == 0:
                del char_count[start_char]
            start += 1
    
    return min_length if min_length != float('inf') else 0

# Test cases
def run_tests():
    # Basic test
    assert full_alphabet_len("aabcdefghijKK 1, lmnopqrstuvwxyza") == 27
    
    # Test with custom alphabet (Latvian)
    latvian_alphabet = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
    
    # Test with empty string
    assert full_alphabet_len("") == 0
    
    # Test with missing letters
    assert full_alphabet_len("abcde") == 0
    
    # Test with case sensitivity
    test_str = "abcdefghijklmnopqrstuvwxyz"
    assert full_alphabet_len(test_str, ignore_case=False) == 26
    assert full_alphabet_len(test_str.upper(), ignore_case=False) == 0
    
    # Test with custom alphabet
    assert full_alphabet_len("aābcčdeēfgģhiījkķlļmnņoprsštuūvzž", 
                           custom_a=latvian_alphabet) == 33
    
    print("All tests passed!")

run_tests()