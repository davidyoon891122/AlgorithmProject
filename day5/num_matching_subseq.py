from typing import List

def num_matching_subseq(S: str, words: List[str]) -> int:
    matched_count = 0

    for word in words:
        pos = 0
        for i in range(len(word)):
            # Find matching position for each character
            found_pos = S[pos:].find(word[i])
            print(found_pos)
            if found_pos < 0:
                print('matched_count: {}'.format(matched_count))
                matched_count -= 1
                print('matched_count: {}'.format(matched_count))
                break
            else: # If found, take step position forward
                pos += found_pos + 1
        matched_count += 1
        print('outside matched_count: {}'.format(matched_count))
    return matched_count


print('result: {}'.format((num_matching_subseq('test', ['test', 'test1', 'testttete', 'test']))))
