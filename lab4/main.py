from collections import defaultdict

# Толь бичигт байгаа үгсийн жагсаалтыг тодорхойлсон хэсэг
dictionary = set(['create', 'crate', 'crate', 'grate', 'great', 'greet', 'green', 'creen'])

# Графикийг илэрхийлэх хоосон толь бичиг үүсгэсэн хэсэг
graph = defaultdict(set)

# Толь бичгийн үг бүрийн хувьд давталт явуулсан
for word in dictionary:
    # үг дэх үсэг бүрийн хувьд явуулсан давталт
    for i in range(len(word)):
        # Үсгийг солих хэсэг
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            
            if letter != word[i]:
                new_word = word[:i] + letter + word[i+1:]
                if new_word in dictionary and new_word != word:
                    
                    graph[word].add(new_word)
                    graph[new_word].add(word)


for node in graph:
    print(node, ':', ', '.join(graph[node]))
