from langchain_neo4j import Neo4jGraph
import sys
import io

# 强制终端使用 utf-8 避免打印 emoji 时报错
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

print("Testing Neo4j connection and APOC plugin...")
try:
    graph = Neo4jGraph(url="bolt://localhost:7687", username="neo4j", password="password")
    # Verify APOC is available by calling a simple APOC procedure
    result = graph.query("CALL apoc.meta.data() YIELD label RETURN count(label) AS c")
    print("✅ APOC plugin is working perfectly! Output:", result)
except Exception as e:
    print("❌ Failed:", e)
