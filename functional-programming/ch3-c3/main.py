def map_keywords(document, document_map):
    document_map_copy = document_map.copy()
    if document in document_map_copy:
        return document_map_copy[document], document_map_copy
    found_keywords = find_keywords(document)
    document_map_copy[document] = found_keywords
    return found_keywords, document_map_copy


def find_keywords(document):
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]
    
    filtered_keywords = []
    for keyword in keywords:
        if keyword in document.lower():
            filtered_keywords.append(keyword)
    return filtered_keywords
