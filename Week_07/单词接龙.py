题目：https://leetcode-cn.com/problems/word-ladder 单词接龙
思路：搜索，BFS

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        arr = set(wordList)
        q = collections.deque([(beginWord, 1)])
        alpha = string.ascii_lowercase
        visited = set()

        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(beginWord)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in arr and new_word not in visited:
                        q.append((new_word, length + 1))
                        visited.add(new_word)
        return 0