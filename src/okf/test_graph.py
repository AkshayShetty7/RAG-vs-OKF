
from src.okf.graph_engine import (
    ENTITIES_FILE,
    RELATIONSHIPS_FILE,
    load_json,
    KnowledgeGraph,
)

entities = load_json(ENTITIES_FILE)
relationships = load_json(RELATIONSHIPS_FILE)

graph = KnowledgeGraph(entities, relationships)

test_entities = [
    "PAT-001",
    "PAT-007",
    "MED-004",
    "PRO-001",
]

for entity_id in test_entities:
    print("\n" + "=" * 60)
    print(f"GRAPH TRAVERSAL: {entity_id}")
    print("=" * 60)

    results = graph.traverse(entity_id, max_depth=2)

    print(f"Connections found: {len(results)}")

    for result in results[:10]:
        relation = result["relationship"]

        print(
    f"{result['from_entity']} "
    f"--[{relation['relation_type']}]--> "
    f"{result['to_entity']} "
    f"(depth={result['depth']}, "
    f"direction={result['traversal_direction']})"
)
