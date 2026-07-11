#!/usr/bin/env python3
"""
Inject markdown AST JSON nodes into graphify graph.
Converts markdown AST format to graphify node/edge format.
"""
import json
from pathlib import Path
from collections import defaultdict

SKILLS_ROOT = Path("/root/.config/opencode/skills")
GRAPH_FILE = SKILLS_ROOT / "graphify-out" / "graph.json"

# Community for markdown AST nodes
AST_COMMUNITY = 500

def load_json_ast(filepath):
    """Load a markdown AST JSON file."""
    try:
        return json.loads(filepath.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, FileNotFoundError):
        return None

def ast_to_graphify_nodes(ast_data, source_json_path):
    """Convert AST nodes to graphify node format."""
    nodes = []
    source_md = ast_data.get("source", "")
    
    for node in ast_data.get("nodes", []):
        # Create unique ID for graphify (prefix to avoid conflicts)
        ast_id = node.get("id", "")
        gf_id = f"md_ast_{ast_id}"
        
        # Create graphify node
        gf_node = {
            "id": gf_id,
            "label": node.get("label", ""),
            "file_type": "markdown_ast",
            "source_file": str(source_json_path),
            "source_location": f"node:{ast_id}",
            "_origin": "md_ast",
            "community": AST_COMMUNITY,
            "norm_label": node.get("label", "").lower(),
            # Extra metadata
            "node_type": node.get("type", ""),
            "original_source": source_md,
            "heading_level": node.get("level", None),
        }
        nodes.append(gf_node)
    
    return nodes

def ast_to_graphify_edges(ast_data):
    """Convert AST edges to graphify edge format."""
    edges = []
    
    for edge in ast_data.get("edges", []):
        # Convert IDs to graphify format
        from_id = f"md_ast_{edge.get('from', '')}"
        to_id = f"md_ast_{edge.get('to', '')}"
        
        gf_edge = {
            "source": from_id,
            "target": to_id,
            "relation": edge.get("relation", "related"),
            "confidence": "EXTRACTED",
            "weight": 1.0,
            "confidence_score": 1.0,
            "_origin": "md_ast",
        }
        edges.append(gf_edge)
    
    return edges

def inject_ast_into_graph():
    """Main function to inject AST nodes into graph."""
    # Load current graph
    with open(GRAPH_FILE, 'r', encoding='utf-8') as f:
        graph = json.load(f)
    
    # Collect existing node IDs to avoid duplicates
    existing_ids = {node['id'] for node in graph['nodes']}
    
    # Find all JSON AST files
    json_files = list(SKILLS_ROOT.glob("**/*.json"))
    
    # Filter to markdown AST files (those with "source" and "nodes" keys)
    ast_files = []
    for jf in json_files:
        try:
            data = json.loads(jf.read_text(encoding='utf-8'))
            if 'source' in data and 'nodes' in data:
                ast_files.append(jf)
        except:
            pass
    
    print(f"Found {len(ast_files)} markdown AST JSON files")
    
    # Collect all new nodes and edges
    all_new_nodes = []
    all_new_edges = []
    
    for ast_file in ast_files:
        ast_data = load_json_ast(ast_file)
        if not ast_data:
            continue
        
        nodes = ast_to_graphify_nodes(ast_data, ast_file)
        edges = ast_to_graphify_edges(ast_data)
        
        # Only add nodes that don't already exist
        for node in nodes:
            if node['id'] not in existing_ids:
                all_new_nodes.append(node)
                existing_ids.add(node['id'])
        
        all_new_edges.extend(edges)
    
    print(f"New nodes to inject: {len(all_new_nodes)}")
    print(f"New edges to inject: {len(all_new_edges)}")
    
    # Inject into graph
    graph['nodes'].extend(all_new_nodes)
    graph['links'].extend(all_new_edges)
    
    # Save updated graph
    with open(GRAPH_FILE, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    
    print(f"Updated graph: {len(graph['nodes'])} nodes, {len(graph['links'])} links")
    
    return graph

if __name__ == "__main__":
    inject_ast_into_graph()
